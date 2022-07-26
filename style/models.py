from django.db import models
from django.forms import CharField, ImageField
from core.models import TimeStampedModel
from products.models import Product
from users.models import User

# Create your models here.

class StyleImage(TimeStampedModel):
    image=models.ImageField(upload_to='style/%Y/%m/%d')
    style=models.ForeignKey("Style", on_delete=models.CASCADE)



class Style(TimeStampedModel):
    user = models.ForeignKey(User, verbose_name="사용자", on_delete=models.CASCADE)
    title=models.CharField(max_length=50, verbose_name='post')
    products=models.ManyToManyField("products.Product", related_name='products') # related_name은 역참조용, 즉 Product모델에서 Product.<related_name>을 쓰면  <이름>_set 대신에 역참조가 가능해짐
    
    def __str__(self):
        return '{}의 STYLE'.format(self.user)
    def count_products(self):
        return self.products.count()
    
    count_products.short_description='상품 태그 수'