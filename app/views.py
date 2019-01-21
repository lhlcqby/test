from django.db.models import Avg, Min, Max, Count, Sum, Q, F
from django.http import HttpResponse
from django.shortcuts import render
from app.models import Student
# Create your views here.
def hello(request):
    # 渲染页面
    # 取数据库 （这里不用SQL ） 用模型
    return HttpResponse('hello')


def add_stu(request):
    #   实现插入数据
    # 实现的第一中方法
    # Student.objects.create(s_name='小明')
    # 实现的第二种方法
    stu = Student()
    stu.s_gender = 1
    stu.s_name = '11小花233'
    stu.save()
    return HttpResponse('创建学生成功')


def del_stu(request):
    #  实现删除
    # 1 获取删除对象    filter(条件)
    # 2 实现删除方法    delete()
    Student.objects.filter(id=3).delete()                               # filter 过滤
    return HttpResponse('删除了。加油啊龙皇')


def up_stu(request):
    # 实现更新
    # 1 获取 filter  2 更新 update()  注意：这里改了什么数据才改， 其他没有设置就不改
    # 第一种方法
    # Student.objects.filter(id=1).update(s_name='土猪')
    # 第二种   save()方法 还会更新修改时间
    stu = Student.objects.filter(id=1).first()
    stu.s_name = '慌张'
    stu.save()
    return HttpResponse('更新成功了啊2')


def sel_stu(request):
    #   查询学生信息
    stus = Student.objects.all()
    for stu in stus:
        print(stu.s_name,stu.s_gender)
    # print(stus)
    #  查询id = 4 的学生
    stu = Student.objects.filter(id=4).first()
    print(stu)
    print('-------------------------')
    #1. get（） 取唯一的一个对象
    #2 。get()  条件必须成立      上面的filter如果条件没有，返回为空
    stu = Student.objects.get(id=4)     # 与前面的方法一样 但只能取唯一一个
    print(stu)
    # 过滤出不满足条件的
    stus = Student.objects.filter(s_gender=1)
    print(stus)
    stus = Student.objects.exclude(s_gender=0)
    print('=========')
    print(stus)
    # 排序
    stus = Student.objects.order_by('-id')    # 加  “-” 就降序
    print(stus)
    # 取出对象中的某个字段
    stus = Student.objects.all().values('s_name','s_age')
    print(stus)
    stus = Student.objects.all().values()           #  工作中比较有用 据说获取时间快
    print('++++++++++++++++')
    print(stus)     #    <QuerySet [{'s_name': '11小花233'}, {'s_name': '小花233'}, {'s_name': '慌张'}]>
    a = Student.objects.filter(s_name='tuzhu').exists()
    # if stus: 这种不用exist 也可以
    print('---------------=-------------')
    print(a)
    # 判断查询结果是否存在
    b = Student.objects.filter(s_gender=1).count()
    b = Student.objects.filter(s_gender=1)
    print(len(b))
    # print(len(b))
    # contains  包含 模糊查询
    # 字段__运算符
    stus = Student.objects.filter(s_name__contains= '花')
    print(stus)
    # like '小%’
    # startwith    endswith
    stus = Student.objects.filter(s_name__startswith='小')
    stu2 = Student.objects.filter(s_name__endswith='张')
    print('------------------------')
    print(stus)
    print(stu2)
    #   sql :  where id in (1,3,4,5,6)
    #  取得id在范围内的数据       pk （ primary key ）
    #  id  和 pk  是同样的
    stus = Student.objects.filter(id__in=[1,2,3,4,5,6])
    print(stus)
    stus = Student.objects.filter(pk__in=[1,2,3,4,5,6])
    print(stus)

    #  gte大于等于  ( greater than  equal  )  gt     lt 小于 (less than ) lte
    #  这里的  ， 为并且操作
    stus = Student.objects.filter(s_age__gte=18,s_age__lt=20)
    print(stus)
    #  这里加filter 都是且的操作  （这种一般不好）
    stus = Student.objects.filter(s_age__gte=18).filter(s_age__lt=20)
    print(stus)

    # 聚合函数        Avg  Max  Min Sum Count
    age_avg = Student.objects.all().aggregate(Avg('s_age'))
    print(age_avg)
    age_sum = Student.objects.all().aggregate(Sum('s_age'))
    print(age_sum)
    #  查询年龄小于19 或者大于21岁 Q()
    stu2 = Student.objects.filter(Q(s_age__lt=18)|Q(s_age__gte=20))   # 或者
    stu2 = Student.objects.filter(Q(s_age__lt=18)&Q(s_age__gte=20))   # 并且

    print(stu2)
    stu2 = Student.objects.filter(~Q(s_age__lt=18))
    print(stu2)

    #  查询物理成绩大约数学成绩的学生
    #  方法1
    # stus = Student.objects.all()
    # print('-----------成绩比较-----------')
    # for stu in stus:
    #     if (stu.wuli > stu.math):
    #         print(stu.s_name)
    stus = Student.objects.filter(wuli__gt=F('math'))     #  F  可以对两个数据的对比
    print(stus)



    return HttpResponse('查询所有信息')