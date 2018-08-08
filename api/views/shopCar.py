from rest_framework.viewsets import ViewSetMixin
import json
from api import models
from api.untils.reponse import ResponseDict
from rest_framework.response import Response
from rest_framework.views import APIView

SHOPPING_CAR = {

}


class ShopCarView(ViewSetMixin, APIView):

    def create(self, request, *args, **kwargs):
        res = ResponseDict()
        # receive_data = request.body
        # print('****', receive_data.decode('utf8'))
        # dic = json.loads(receive_data)
        # user_id = dic['user_id']
        user_id = 1
        # choice_course_id = dic['course_id']
        # choice_pricepolicy_id = dic['pricepolicy_id']
        choice_course_id = self.request.data.get('course_id')
        choice_pricepolicy_id = self.request.data.get('pricepolicy_id')

        course = models.Course.objects.filter(id=choice_course_id).first()
        pre_pricepolicy_allid_obj = course.price_policy.all().values('id', 'price', 'valid_period')
        if course:
            print(6)
            for item in pre_pricepolicy_allid_obj:
                if choice_pricepolicy_id not in (item['id'],):
                    res.get_error('当前价格的课程已下架')
                    print(5)
                else:
                    SHOPPING_CAR[user_id] = {choice_course_id: {'title': course.name,
                                                                'price': item['price'],
                                                                'price_list': [
                                                                    {item['valid_period']: item['price'], },
                                                                ]}}
                print(4)
                res.dara = '已添加到购物车'
                return Response(res)
        # res.get_error('该课程已下架')
        # return Response(res)
