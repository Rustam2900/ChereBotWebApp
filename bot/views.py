from django.shortcuts import render
from rest_framework import mixins, generics, status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from bot.models import BotUser, BotCompany, BotCompanyOrder
from bot.serializer import BotUserSerializer, BotCompanySerializer, BotCompanyOrderSerializer


# class BotCompanyApiView(
#     mixins.CreateModelMixin,
#     mixins.RetrieveModelMixin,
#     generics.GenericAPIView
# ):
#     queryset = BotCompany.objects.all()
#     serializer_class = BotCompanySerializer
#     lookup_field = 'telegram_id'
#
#     def get(self, request, *args, **kwargs):
#         if 'telegram_id' in kwargs:
#             return self.retrieve(request, *args, **kwargs)
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


class BotCompanyApiView(
    mixins.CreateModelMixin,
    generics.GenericAPIView
):
    queryset = BotCompany.objects.all()
    serializer_class = BotCompanySerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


# class BotUserApiView(
#     mixins.CreateModelMixin,
#     mixins.RetrieveModelMixin,
#     generics.GenericAPIView
# ):
#     queryset = BotUser.objects.all()
#     serializer_class = BotUserSerializer
#     lookup_field = 'telegram_id'
#
#     def get(self, request, *args, **kwargs):
#         if 'telegram_id' in kwargs:
#             return self.retrieve(request, *args, **kwargs)
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


class BotUserApiView(
    mixins.CreateModelMixin,
    generics.GenericAPIView
):
    queryset = BotUser.objects.all()
    serializer_class = BotUserSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class OrderCompanyApiView(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    generics.GenericAPIView
):
    queryset = BotCompanyOrder.objects.all()
    serializer_class = BotCompanyOrderSerializer
    lookup_field = 'telegram_id'

    def get_queryset(self):
        telegram_id = self.request.query_params.get('telegram_id', None)
        if telegram_id is not None:
            return BotCompanyOrder.objects.filter(bot_company_id__telegram_id=telegram_id)
        return BotCompanyOrder.objects.all()

    def get(self, request, *args, **kwargs):
        if 'telegram_id' in kwargs:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        telegram_id = kwargs.get('telegram_id')
        try:
            company = BotCompany.objects.get(telegram_id=telegram_id)
            order_company = BotCompanyOrder.objects.filter(bot_company_id=company)
            serializer = self.get_serializer(order_company, many=True)
            return Response(serializer.data)
        except BotCompany.DoesNotExist:
            raise ValidationError({'telegram_id': 'Company with this telegram_id does not exist.'})

    def post(self, request, *args, **kwargs):
        telegram_id = request.data.get('bot_company_id')
        if not telegram_id:
            raise ValidationError({'telegram_id': 'This field is required.'})

        try:
            company = BotCompany.objects.get(telegram_id=telegram_id)
        except BotCompany.DoesNotExist:
            raise ValidationError({'telegram_id': 'Company with this telegram_id does not exist.'})

        request.data['bot_company_id'] = company.id

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
