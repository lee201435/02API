import os

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "s11luffycity.settings")
    import django
    django.setup()

from api import models
choice_course_id = 1
choice_pricepolicy_id = 1
course = models.Course.objects.filter(id=choice_course_id).first()
pre_pricepolicy_allid_obj = course.price_policy.all().values('id', 'price', 'valid_period')

for item in pre_pricepolicy_allid_obj:
    if choice_pricepolicy_id not in (item['id'],):
        print(666)
    print(item['price'])

