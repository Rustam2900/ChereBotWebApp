import re

from aiogram import Router, types, F
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from bot.api import create_company, create_user
from bot.keyboard.k_button import contact_user, main_menu, person, person_ru


class RegisterForm(StatesGroup):
    company_name = State()
    company_employee_name = State()
    company_contact = State()
    employee_number = State()
    lifetime = State()


router = Router()


@router.message(F.text == '🇺🇿')
async def lang_uz(message: types.Message):
    await message.answer(text='Harakatni tanlang 〽️:', reply_markup=person())


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
    await state.update_data(employee_number=message.text)
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

    response_message = await create_company(
        telegram_id=message.from_user.id,
        company_name=data['company_name'],
        company_employee_name=data['company_employee_name'],
        company_contact=data['company_contact'],
        employee_number=data['employee_number'],
        lifetime=data['lifetime']

    )
    result = (f"Kompaniya nomi: {data['company_name']}\n\n"
              f"Xodimlar soni: {data['employee_number']}\n\n"
              f"Davomiylik: {data['lifetime']} kun\n\n"
              f"Kompaniya xodimining ismi: {data['company_employee_name']}\n\n"
              f"Kontakt ma'lumotlari: {data['company_contact']}",
              "sizga maslahat bergan suvimiz")

    await message.answer(f"{result}\n\n{response_message}",
                         reply_markup=main_menu())

    await state.clear()


class RegisterFormUser(StatesGroup):
    name = State()
    contact = State()
    add_contact = State()


@router.message(F.text == 'jismoniy shaxs')
async def physical_person(message: types.Message, state: FSMContext):
    await state.set_state(RegisterFormUser.name)
    await message.answer(text="Ismingizni kiriting:")


@router.message(F.text == 'юридическое лицо')
async def physical_person(message: types.Message, state: FSMContext):
    await state.set_state(RegisterFormUser.name)
    await message.answer(text="Введите ваше имя:")


@router.message(RegisterFormUser.name)
async def process_user_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(RegisterFormUser.contact)
    await message.answer(text="Kontakt ma'lumotlarini kiriting:", reply_markup=contact_user())


@router.message(RegisterFormUser.contact)
async def process_user_contact(message: types.Message, state: FSMContext):
    contact = message.contact.phone_number
    await state.update_data(contact=contact)
    await state.set_state(RegisterFormUser.add_contact)
    await message.answer(text="Qo'shimcha kontakt ma'lumotlarini kiriting:\n\n"
                              "+998 (93) 068 29 11")


@router.message(RegisterFormUser.add_contact)
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
              f"qo'shimcha contact {user_data['add_contact']}")

    await message.answer(f"{result}\n\n{response_message}",
                         reply_markup=main_menu())
    await state.clear()


