from api import models

# ORM练习
# a. 查看所有学位课并打印学位课名称以及授课老师
# obj_list1 = models.DegreeCourse.objects.all()
#
# for item in obj_list1:
#     print(item.name, '----', item.teachers.all().first().name)
#
# # b. 查看所有学位课并打印学位课名称以及学位课的奖学金
# obj_list2 = models.DegreeCourse.objects.values_list('name', 'scholarship__value')
# for item in obj_list2:
#     print(item[0], item[1])
#
# # c. 展示所有的专题课  models.Course.objects.filter(degree_course__isnull=True)
# obj_l = models.Course.objects.filter(degree_course__isnull=True)
# for obj in obj_l:
#     print(obj.name)
#
# # d. 查看id=1的学位课对应的所有模块名称
# obj = models.DegreeCourse.objects.filter(id=1).first()
# print(obj.course_set.all())
#
# # e. 获取id=1的专题课，并打印：课程名、级别(中文)、why_study、what_to_study_brief、所有recommend_courses
# obj1 = models.Course.objects.filter(id=1).first()
# print(obj1.name)
# print(obj1.get_level_display())
# print(obj1.coursedetail.why_study)
# print(obj1.coursedetail.what_to_study_brief)
# for i in obj1.coursedetail.recommend_courses.all():
#     print(i)
#
# # f. 获取id=1的专题课，并打印该课程相关的所有常见问题
# obj2 = models.Course.objects.filter(degree_course__isnull=True, id=1).first()
# print(obj2.asked_question.all())
# for i in obj2.asked_question.all():
#     print(i.question)
#     print(i.answer)
#
# # g. 获取id=1的专题课，并打印该课程相关的课程大纲
# obj3 = models.CourseDetail.objects.filter(course__id=1, course__degree_course__isnull=True).values_list('courseoutline__content')
# for i in obj3:
#     print(i[0])
#
# # h. 获取id=1的专题课，并打印该课程相关的所有章节
# obj_ls = models.Course.objects.filter(degree_course__isnull=True, id=1).values_list('coursechapters__name')
# for i in obj_ls:
#     print(i[0])
# # i. 获取id=1的专题课，并打印该课程相关的所有课时----for i in obj:
# obj_list3 = models.CourseChapter.objects.filter(course__id=1, course__degree_course__isnull=True)
# for obj in obj_list3:
#     print(obj.name)
#     session_list = obj.coursesections.all()
#     for item in session_list:
#         print(item.name)
# # j.  获取id=1的专题课，并打印该课程相关的所有的价格策略
# obj4 = models.Course.objects.filter(degree_course__isnull=True, id=1).first()
# print(obj4.price_policy.all()[0])


# 二、基于django rest framework 写路飞的接口（作业一+rest framework 序列化）
# - 课程列表API
# - 课程详细API

# from rest_framework.views import APIView
# from rest_framework.response import Response
# from app01 import serializers
# from django.http import JsonResponse
# import json


# Create your views here.



