from django.urls import path
from bot.views import (BotUserApiView,
                       OrderCompanyApiView, BotCompanyApiView)

urlpatterns = [
    path('botcompany/<int:telegram_id>', BotCompanyApiView.as_view()),
    path('botuser/', BotUserApiView.as_view()),
    path('order-company/<int:telegram_id>', OrderCompanyApiView.as_view()),
]
