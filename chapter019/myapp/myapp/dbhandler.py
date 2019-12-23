# -*- coding: utf-8 -*-
from django.http import HttpResponse
from mymodel.models import UserInfo


# 数据添加
def add_db(request):
    test1 = UserInfo(name='Python', password='')
    test1.save()
    return HttpResponse("<p>数据添加成功！</p>")


# 数据查询
def query_db(request):
    # 初始化
    response = ""
    response1 = ""

    # 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM
    list = UserInfo.objects.all()
    # 条件过滤
    response2 = UserInfo.objects.filter(id=1)
    # 获取单个对象
    response3 = UserInfo.objects.get(id=1)
    # 限制返回的数据 相当于 SQL 中的 OFFSET 0 LIMIT 2;
    UserInfo.objects.order_by('name')[0:2]
    # 数据排序
    UserInfo.objects.order_by("id")
    # 组合用法
    UserInfo.objects.filter(name="Python").order_by("id")

    # 输出所有数据
    for var in list:
        response1 += var.name + " "
    response = response1
    return HttpResponse("<p>" + response + "</p>")


# 数据更新
def update_db(request):
    # 修改其中一个id=1的name字段，再save，相当于SQL中的UPDATE
    test1 = UserInfo.objects.get(id=1)
    test1.name = 'C++'
    test1.save()

    # 另外一种方式
    # Test.objects.filter(id=1).update(name='Google')

    # 修改所有的列
    # Test.objects.all().update(name='Google')

    return HttpResponse("<p>修改成功</p>")


# 数据删除
def del_db(request):
    # 删除id=1的数据
    test1 = UserInfo.objects.get(id=1)
    test1.delete()

    # 方法二
    # UserInfo.objects.filter(id=1).delete()

    # 删除所有数据
    # UserInfo.objects.all().delete()

    return HttpResponse("<p>删除成功</p>")


# 数据库操作，追加新的用户名
def add_name(var1):
    test1 = UserInfo(name=var1, password='')
    test1.save()
    print("add_name is OK.")
