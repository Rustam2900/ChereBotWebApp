import re
import aiohttp

from aiogram import Router, types, F
from aiogram.fsm.state import StatesGroup, State

from aiogram.fsm.context import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from asgiref.sync import sync_to_async

from bot.api import create_company, create_user, BASE_URL
from bot.filters.states import RegisterFormUser, RegisterForm, RegisterFormUserBot
from bot.keyboard.k_button import contact_user, main_menu, lang_change, person, person_ru

# from aiogram.utils.i18n import gettext as _

router = Router()


@router.message(F.text == '🇺🇿')
async def lang_uz(message: types.Message):
    await message.answer(text='Harakatni tanlang 〽️:', reply_markup=person())


# @router.message(RegisterFormUser.CHOOSE_LANGUAGE,
#                 lambda message: message.text in ["🇺🇿 UZ", "🇷🇺 RU"])
# async def process_language(message: types.Message, state: FSMContext):
#     user_language = 'uz' if message.text == "🇺🇿 UZ" else 'ru'
#     await state.update_data(language=user_language)
#     user_data = await state.get_data()
#     await state.set_state(RegisterFormUser.NAME)
#     await message.answer(text=' ', reply_markup=person())
#     await message.answer("yuridik shaxs  jismoniy shaxs?")
#
#
# @router.message(RegisterFormUser.CHOOSE_LANGUAGE,
#                 lambda message: message.text not in ["🇺🇿 UZ", "🇷🇺 RU"])
# async def process_language(message: types.Message, state: FSMContext):
#     await message.answer(
#         ("Tilni tanlang, Выберите язык"),
#         reply_markup=lang_change()
#     )


@router.message(F.text == '🇷🇺')
async def lang_ru(message: types.Message):
    await message.answer(text='Выберите действие 〽️:', reply_markup=person_ru())


@router.message(F.text == 'yuridik shaxs')
async def legal_entity(message: types.Message, state: FSMContext):
    await state.set_state(RegisterForm.company_name)
    await message.answer('Company nomini kiriting:')


@router.message(RegisterForm.company_name)
async def process_company_name(message: types.Message, state: FSMContext):
    await state.update_data(company_name=message.text)
    await state.set_state(RegisterForm.company_employee_name)
    await message.answer("companiya xodimining ismini kiriting:")


@router.message(RegisterForm.company_employee_name)
async def process_employee_number(message: types.Message, state: FSMContext):
    await state.update_data(company_employee_name=message.text)
    await state.set_state(RegisterForm.company_contact)
    await message.answer(text="company contactni kiriting", reply_markup=contact_user())


@router.message(RegisterForm.company_contact)
async def process_company_contact(message: types.Message, state: FSMContext):
    contact = message.contact.phone_number
    await state.update_data(company_contact=contact)
    await state.set_state(RegisterForm.employee_number)
    await message.answer(text="companiya xodimining soni kiriting:")


@router.message(RegisterForm.employee_number)
async def process_employee_number(message: types.Message, state: FSMContext):
    await state.update_data(employee_number=int(message.text))
    await state.set_state(RegisterForm.lifetime)
    await message.answer(text="Buyurtmani Davomiligi(kun):")


@router.message(RegisterForm.lifetime)
async def process_lifetime(message: types.Message, state: FSMContext):
    await state.update_data(lifetime=int(message.text))
    data = await state.get_data()

    employees = data['employee_number']
    days = data['lifetime']
    water_per_day_per_employee = 2  # 1 xodim uchun kuniga 2 litr suv
    workdays_per_week = 5

    if days < 7:
        total_workdays = days
    else:
        weeks = days // 7
        remaining_days = days % 7
        total_workdays = weeks * workdays_per_week + min(remaining_days, workdays_per_week)

    total_water_per_day = employees * water_per_day_per_employee
    total_water_needed = total_water_per_day * total_workdays
    total_water_needed = total_water_needed // 20

    await message.answer(f"Sizga maslahat: {total_water_needed} ta 20 L suv buyurtma bersangiz bo'ladi.")

    # Inline tugmalar
    inline_kb = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Buyurtma berish", callback_data="order"),
            InlineKeyboardButton(text="Bekor qilish", callback_data="cancel")
        ]
    ])
    response_message = await create_company(
        telegram_id=message.from_user.id,
        company_name=data['company_name'],
        company_employee_name=data['company_employee_name'],
        company_contact=data['company_contact'],
        employee_number=data['employee_number'],
        lifetime=data['lifetime']
    )
    await state.update_data(total_water_needed=total_water_needed)
    await state.update_data(company_id=response_message.get('company_id'))  # Assuming the response includes company_id
    # Javobni foydalanuvchiga yuborish
    await message.answer(
        f"Kompaniya nomi: {data['company_name']} \n"
        f"Xodimlar soni: {data['employee_number']} \n"
        f"Davomiylik: {data['lifetime']} kun \n"
        f"Kompaniya xodimining ismi: {data['company_employee_name']} \n"
        f"Kontakt ma'lumotlari: {data['company_contact']} \n\n"
        f"Sizga maslahat bergan suvimiz: {total_water_needed} ta 20 L \n\n"
        f"{response_message}",
        reply_markup=inline_kb
    )

    await state.clear()


# @router.callback_query(lambda c: c.data in ["order", "cancel"])
# async def process_order_or_cancel(callback_query: types.CallbackQuery, state: FSMContext):
#     if callback_query.data == "order":
#         # Buyurtmani tasdiqlash jarayoni
#         await callback_query.message.answer("Buyurtmangiz qabul qilindi!", reply_markup=main_menu())
#     elif callback_query.data == "cancel":
#         # Buyurtmani bekor qilish
#         await callback_query.message.answer("Buyurtma bekor qilindi.", reply_markup=main_menu())
#
#     await callback_query.answer()

@router.callback_query(lambda c: c.data in ["order", "cancel"])
async def process_order_or_cancel(callback_query: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    print("###############")
    print(data)
    print("###############")
    if callback_query.data == "order":
        # Buyurtmani tasdiqlash va API orqali yaratish
        response_message = await create_order_company(
            bot_company_id=data['company_id'],
            product_name="20 L",
            quantity=data['total_water_needed']
        )
        await callback_query.message.answer(response_message, reply_markup=main_menu())
    elif callback_query.data == "cancel":
        await callback_query.message.answer("Buyurtma bekor qilindi.", reply_markup=main_menu())

    await callback_query.answer()


async def create_order_company(bot_company_id, product_name, quantity):
    url = f"{BASE_URL}/order-company/{int(bot_company_id)}"
    headers = {
        'Content-Type': 'application/json'
    }
    data = {
        "product_name": product_name,
        "quantity": quantity
    }
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(url, headers=headers, json=data) as response:
                if response.status == 201:
                    return "Buyurtmangiz muvaffaqiyatli yaratildi!"
                else:
                    return f"Error: {response.status}"
    except Exception as e:
        print(e)
        return f"Error: {str(e)}"


@router.message(F.text == 'jismoniy shaxs')
async def physical_person(message: types.Message, state: FSMContext):
    await state.set_state(RegisterFormUserBot.name)
    await message.answer(text="Ismingizni kiriting:")


@router.message(F.text == 'юридическое лицо')
async def physical_person(message: types.Message, state: FSMContext):
    await state.set_state(RegisterFormUserBot.name)
    await message.answer(text="Введите ваше имя:")


@router.message(RegisterFormUserBot.name)
async def process_user_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(RegisterFormUserBot.contact)
    await message.answer(text="Kontakt ma'lumotlarini kiriting:", reply_markup=contact_user())


@router.message(RegisterFormUserBot.contact)
async def process_user_contact(message: types.Message, state: FSMContext):
    contact = message.contact.phone_number
    await state.update_data(contact=contact)
    await state.set_state(RegisterFormUserBot.add_contact)
    await message.answer(text="Qo'shimcha kontakt ma'lumotlarini kiriting:\n\n"
                              "+998 (93) 068 29 11")


@router.message(RegisterFormUserBot.add_contact)
async def process_user_add_contact(message: types.Message, state: FSMContext):
    add_contact = message.text

    # Validatsiya uchun regex
    if not re.fullmatch(r'[+\d() -]+', add_contact):
        await message.answer(
            "Iltimos, kontakt ma'lumotlarini to'g'ri formatda kiriting \n\n "
            "(faqat raqamlar, +, (), va - ishlatilishi mumkin):\n\n"
            "+998 (93) 068 29 11")
        return

    await state.update_data(add_contact=add_contact)
    user_data = await state.get_data()

    response_message = await create_user(
        telegram_id=message.from_user.id,
        name=user_data['name'],
        contact=user_data['contact'],
        add_contact=user_data['add_contact']
    )

    result = (f"ismiz: {user_data['name']} \n\n"
              f"contact: {user_data['contact']} \n\n"
              f"qo'shimcha contact: {user_data['add_contact']}")

    await message.answer(f"{result}\n\n{response_message}",
                         reply_markup=main_menu())
    print("#####################")
    print(result)
    print("#####################")
    await state.clear()
