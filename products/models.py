from django.db import models
from django.forms import CharField, ImageField
from core.models import TimeStampedModel


class Brand(TimeStampedModel):
    name = models.CharField(max_length=40)


class Photo(TimeStampedModel):
    image = models.ImageField()
    product = models.ForeignKey("Product", on_delete=models.CASCADE)


# Create your models here.
class Product(TimeStampedModel):

    brand = models.ForeignKey(
        "Brand", on_delete=models.CASCADE
    )  # 일대다 관계일 경우 포린키사용, 매개변수 1은 대상 클래스, 2는 on_delete -> 브랜드가 없어지면 함께 삭제=CASCADE 없어져도 그대로 = SET_NULL
    name_en = models.CharField(max_length=120)
    name_ko = models.CharField(max_length=120)
    model_number = models.CharField(max_length=80)
    released = models.DateField()
    color = models.CharField(max_length=120)
    released_price = models.PositiveIntegerField()  # 양수만 하면 positiveintegerField
