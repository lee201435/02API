import json
import redis
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ViewSetMixin

from api import models
from api.untils.reponse import ResponseDict
# 与redis相连，建立一个连接
CONN = redis.Redis(host='192.168.11.100', port='6379')
USE_ID = 1  # 虚拟一个用户


class ShopCarView(ViewSetMixin, APIView):   # 购物车视图

    def list(self, request, *args, **kwargs):   # 购物车展示
        res = ResponseDict()  # 实例化一个响应返回值的对象
        try:
            keys = settings.COURSE_KRY % (USE_ID, '*')   # 从全局里拿到一个拼接字符串的key
            keys_list = CONN.keys(keys)   # 取到redis里的所有key
            course_list = []
            for key in keys_list:
                # 获得redis里的数据
                temp = {
                    'course_id': CONN.hget(key, 'course_id').decode('utf-8'),
                    'img': CONN.hget(key, 'img').decode('utf-8'),
                    'course_name': CONN.hget(key, 'course_name').decode('utf-8'),
                    'default_price_id': CONN.hget(key, 'default_price_id').decode('utf-8'),
                    'pricepolicy_dict': json.loads(CONN.hget(key, 'pricepolicy_dict').decode('utf-8')),
                }
                course_list.append(temp)
            res.data = course_list
        except Exception as e:
            res.get_error('获取失败')
        return Response(res.dict)

    def create(self, request, *args, **kwargs):   # 添加课程到购物车
        res = ResponseDict()
        try:
            course_id = self.request.data.get('course_id')
            pricepolicy_id = self.request.data.get('pricepolicy_id')
            # 从数据库里取得当前课程的对象
            course = models.Course.objects.filter(id=course_id).first()
            keys = settings.COURSE_KRY % (USE_ID, course_id)
            if not course:
                res.code = 404
                res.get_error('该课程不存在，请进正规的网页选择课程')
                return Response(res.dict)
            # 从当前数据库里取得当前课程的所有的价格策略
            pre_pricepolicy_allid_queryset = course.price_policy.all()
            pricepolicy_dict = {}
            for item in pre_pricepolicy_allid_queryset:
                temp = {
                    'name': course.name,
                    'id': item.id,
                    'price': item.price,
                    'valid_period': item.valid_period,
                    'valid_period_list': item.get_valid_period_display()
                }
                pricepolicy_dict[item.id] = temp
            if pricepolicy_id not in pricepolicy_dict:
                res.code = 404
                res.get_error('当前课程套餐不存在，请进正规的网页选择课程')
                return Response(res.dict)
            # 添加数据到redis里
            CONN.hset(keys, 'course_id', course_id)
            CONN.hset(keys, 'img', course.course_img)
            CONN.hset(keys, 'course_name', course.name)
            CONN.hset(keys, 'default_price_id', pricepolicy_id)
            CONN.hset(keys, 'pricepolicy_dict', json.dumps(pricepolicy_dict))
            # # # CONN.flushall()

            res.data = '加入购物车成功'
        except Exception as e:
            res.get_error('加入购物车失败')
            res.code = 10004
        return Response(res.dict)

    def update(self, request, *args, **kwargs):   # 修改购物车里的课程
        res = ResponseDict()
        try:
            # 判断得到的数据是否为空，以防报错
            pricepolicy_id = str(request.data.get('pricepolicy_id')) if request.data.get('pricepolicy_id') else None
            course_id = request.data.get('course_id')
            keys = settings.COURSE_KRY % (USE_ID, course_id)
            # 判断redis里是否有当前的数据
            if not CONN.exists(keys):
                res.code = 20000
                res.get_error('当前课程不存在，请重试')
                return Response(res.dict)
            pricepolicy_dict = json.loads(CONN.hget(keys, 'pricepolicy_dict').decode('utf-8'))

            if pricepolicy_id not in pricepolicy_dict:
                res.code = 20001
                res.get_error('当前课程套餐不存在，请重试')
                return Response(res.dict)
            CONN.hset(keys, 'default_price_id', pricepolicy_id)
            res.data = '修改成功'
        except Exception as e:
            res.code = 10005
            res.get_error('修改失败')

        return Response(res.dict)

    def destroy(self, request, *args, **kwargs):   # 删除购物车的课程
        res = ResponseDict()
        try:
            course_id = request.data.get('course_id')
            keys = settings.COURSE_KRY % (USE_ID, course_id)
            if not CONN.exists(keys):
                res.code = 20000
                res.get_error('当前课程不存在，请重试')
                return Response(res.dict)
            # 删除当前选择的数据
            CONN.delete(keys)
            res.data = '删除成功'
        except Exception as e:
            res.code = 20006
            res.get_error('删除失败，请重试')
        return Response(res.dict)
