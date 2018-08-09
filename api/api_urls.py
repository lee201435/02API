from django.conf.urls import url
from api.views import course, auth, shopCar
urlpatterns = [
    url(r'course/$', course.CourseView.as_view({'get': 'list'})),
    url(r'coursedetail/(?P<pk>\d+)/$', course.CourseView.as_view({'get': 'retrieve'})),
    url(r'auth/', auth.Auth.as_view({'post': 'login'})),
    url(r'shopcar/$', shopCar.ShopCarView.as_view(
        {
            'post': 'create',
            'delete': 'destroy',
            'put': 'update',
            'get': 'list',
        })),

]
