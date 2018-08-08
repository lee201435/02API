from api import models, serializers
from rest_framework.views import APIView
from api.untils.reponse import ResponseDict
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ViewSetMixin
from django.http import JsonResponse
from api.untils.reponse import ResponseDict


class Auth(ViewSetMixin, APIView):
    def login(self, request, *args, **kwargs):
        ret = ResponseDict()
        print('用户发来POST请求了', request.body)
        ret.data = '服务器传来了数据'

        return Response(ret.dict)
