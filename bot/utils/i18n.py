# from aiogram import BaseMiddleware
# from aiogram.types import Update
# from django.utils.translation import activate
# from django.conf import settings
# from typing import Callable, Dict, Awaitable, Any
# from bot.models import BotUser, BotCompany
# from asgiref.sync import sync_to_async
#
#
# class I18Middleware(BaseMiddleware):
#     async def __call__(self, handler: Callable[[Update, Dict[str, Any]], Awaitable[Any]],
#                        event: Update,
#                        data: Dict[str, Any]
#                        ) -> Any:
#         # Extract user ID from the event
#         telegram_id = None
#         if hasattr(event, 'message') and event.message:
#             telegram_id = event.message.from_user.id
#         elif hasattr(event, 'callback_query') and event.callback_query:
#             telegram_id = event.callback_query.from_user.id
#         elif hasattr(event, 'edited_message') and event.edited_message:
#             telegram_id = event.edited_message.from_user.id
#         # Add more checks if you need to handle more update types
#
#         if telegram_id:
#             try:
#                 # Retrieve the user from the database
#                 user = await sync_to_async(BotUser.objects.get)(telegram_id=telegram_id)
#             except BotUser.DoesNotExist:
#                 user = None
#
#             if user is None:
#                 try:
#                     # Retrieve the company from the database
#                     company = await sync_to_async(BotCompany.objects.get)(telegram_id=telegram_id)
#                 except BotCompany.DoesNotExist:
#                     company = None
#             else:
#                 company = None
#         else:
#             user = None
#             company = None
#
#         if user is not None:
#             activate(user.language)
#         elif company is not None:
#             activate(company.language)
#         else:
#             activate(settings.LANGUAGE_CODE)
#
#         return await handler(event, data)
