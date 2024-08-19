import asyncio
# from aiogram.utils.i18n import gettext as _

from aiogram import Router, types, F, Bot

from bot.conustant import BACK, SETTINGS, LANG_CHANGE, MY_ORDERS, WEB_ORDERS
from bot.keyboard.k_button import main_menu, settings, \
    lang_change_settings, web
from bot.api import get_product, fetch_user_orders
from datetime import datetime, timedelta

latest_notification_task = None

router = Router()

x = get_product()


@router.message(F.text == WEB_ORDERS)
async def web_orders_(message: types.Message):
    await message.answer(text="webapp buyurtma berish", reply_markup=web())


@router.message(F.text == BACK)
async def back_(message: types.Message):
    await message.answer(text='Bo‘limni tanlang 〽️:', reply_markup=main_menu())


@router.message(F.text == SETTINGS)
async def settings_help(message: types.Message):
    await message.answer(text='Harakatni tanlang 〽️:', reply_markup=settings())


@router.message(F.text == LANG_CHANGE)
async def lang_chan(message: types.Message):
    await message.answer(text='Tilni tanlang 〽️:', reply_markup=lang_change_settings())


@router.callback_query(lambda c: c.data == 'back')
async def back_(callback_query: types.CallbackQuery):
    await callback_query.message.answer(text="Tanlashiz mumkin 〽️", reply_markup=keyboard)
    await callback_query.answer()


def format_time(time_string):
    time_format = "%Y-%m-%dT%H:%M:%S.%f%z"
    original_time = datetime.strptime(time_string, time_format)
    adjusted_time = original_time + timedelta(hours=11, minutes=5)
    return adjusted_time.strftime("%Y-%m-%d %H:%M")


async def send_periodic_notifications(chat_id, order_time, bot: Bot):
    start_time = datetime.strptime(order_time, "%Y-%m-%dT%H:%M:%S.%f%z")
    while True:
        await asyncio.sleep(60)
        elapsed_time = datetime.now(start_time.tzinfo) - start_time
        elapsed_minutes = int(elapsed_time.total_seconds() // 60)
        await bot.send_message(chat_id,
                               text=f"Assalom, siz buyurtma berganingizga {elapsed_minutes} minut bo'ldi. Suvingiz tugamadimi? Bizning vazifamiz eslatib turish.")
        if elapsed_minutes >= 60:
            break


@router.message(F.text == MY_ORDERS)
async def my_orders(message: types.Message, bot: Bot):
    global latest_notification_task

    telegram_id = message.from_user.id
    orders = await fetch_user_orders(telegram_id)
    if orders and len(orders) > 0:
        orders = sorted(orders, key=lambda x: x['create_at'], reverse=True)
        latest_order = orders[0]
        order_info = (
            f"Vaxti: {format_time(latest_order['create_at'])}, \n\n"
            f"Mahsulot: {latest_order['product_name']}, \n\n"
            f"Miqdori: {latest_order['amount']}"
        )
        await message.answer(text=f"Sizning oxirgi buyurtmangiz:\n\n{order_info}")

        if latest_notification_task:
            latest_notification_task.cancel()

        latest_notification_task = asyncio.create_task(
            send_periodic_notifications(message.chat.id, latest_order['create_at'], bot))
    else:
        await message.answer(text="Siz hali hech nima buyurtma qilmagansiz.")
