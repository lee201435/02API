from api import models, serializers
from rest_framework.views import APIView
from api.untils.reponse import ResponseDict
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ViewSetMixin


class CourseView(ViewSetMixin, APIView):

    def list(self, request, *args, **kwargs):
        ret = ResponseDict()
        try:
            course_queryset = models.Course.objects.all()
            page = PageNumberPagination()
            course_list = page.paginate_queryset(course_queryset, request, self)
            course_new = serializers.CourseSerializer(course_list, many=True)
            ret.data = course_new.data
        except Exception as e:
            ret.get_error(e)
        return Response(ret.dict)

    def retrieve(self, request, pk, *args, **kwargs):
        ret = ResponseDict()
        try:
            course = models.Course.objects.filter(id=pk, degree_course__isnull=True).first()
            course_new = serializers.CourseDetailSerializer(course)
            ret.data = course_new.data
        except Exception as e:
            ret.get_error(e)
        return Response(ret.dict)






