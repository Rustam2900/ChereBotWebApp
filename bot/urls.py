from django.urls import path
from bot.views import (BotUserApiView,
                       BotCompanyApiView, BotCompanyOrderCreateView)

urlpatterns = [
    path('botcompany/', BotCompanyApiView.as_view()),
    path('botuser/', BotUserApiView.as_view()),
    path('order-company/<int:bot_company_id>/', BotCompanyOrderCreateView.as_view(), name='order-company-create'),
]
