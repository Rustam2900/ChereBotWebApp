import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher, Router
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from bot.config import BOT_TOKEN
from bot.header.start import router as router_start
from bot.header.register import router as router_register
from bot.header.orders import router as router_orders
from bot.utils import i18n
# from aiogram_i18n import I18nMiddleware
router = Router()
router.include_router(router_start)
router.include_router(router_register)
router.include_router(router_orders)

bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))


async def main() -> None:
    dp = Dispatcher()

    # i18n = I18nMiddleware(domain="chere_bot", path="locales")
    # dp.message.middleware(i18n)
    # dp.update.outer_middleware.register(i18n.I18Middleware())

    dp.include_router(router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
