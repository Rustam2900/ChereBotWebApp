import aiohttp

from aiogram import Router, types
from aiogram.fsm.context import FSMContext
from aiogram.filters import CommandStart
from aiogram.utils.i18n import gettext as _

from bot.api import check_user_registration, check_company_registration
from bot.header.register import RegisterFormUser
from bot.keyboard.k_button import lang_change, main_menu

router = Router()


@router.message(CommandStart())
async def start_(message: types.Message, state: FSMContext):
    telegram_id = message.from_user.id

    async with aiohttp.ClientSession() as session:
        is_user_registered = await check_user_registration(session, telegram_id)
        is_company_registered = await check_company_registration(session, telegram_id)

    if not (is_user_registered or is_company_registered):
        # await message.answer(_("Assalom botga xush kelibsiz tilni tanlang"), reply_markup=lang_change())
        await state.set_state(RegisterFormUser.CHOOSE_LANGUAGE)
        await message.answer(("Assalomu aleykum, Привет"))
        await message.answer(
            ("Tilni tanlang, Выберите язык"),
            reply_markup=lang_change())
    else:
        await message.answer(text="Bo‘limni tanlang 〽️:", reply_markup=main_menu())
