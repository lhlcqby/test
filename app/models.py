from django.db import models

# Create your models here.
# [02/Jan/2019 15:11:38] "GET / HTTP/1.1" 404 2026

class Student(models.Model):
    objects = None
    s_name = models.CharField(max_length=10,unique=True)
    s_age = models.IntegerField(default=20)   # default 为默认值
    s_gender = models.BooleanField(default=0)
    create_time = models.DateTimeField(auto_now_add=True)   # 有时分秒 auto_now_add 默认字段赋值为最新的时间
    # create_time = models.DateField     这个没有时分秒
    update_time = models.DateTimeField(auto_now=True)          # auto_now  修改数据时。字符更新时间
    math = models.DecimalField(max_digits=3,decimal_places=1,null=True)                          # DecimalField() 可以限制长度
    wuli = models.DecimalField(max_digits=3,decimal_places=1,null=True)
    class Meta:
        db_table = 'student'
