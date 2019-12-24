from django.db import models


class Main(models.Model):
    # 图片名称
    name = models.CharField(max_length=128)
    # 图片链接
    img = models.CharField(max_length=512)

    class Meta:
        abstract = True


class MainWheel(Main):
    """首页轮播"""

    class Meta:
        db_table = 'main_wheel'


class MainNav(Main):
    """首页导航"""

    class Meta:
        db_table = 'main_nav'


class FoodType(models.Model):
    """商品类型表"""
    # 类型编号
    type_no = models.CharField(max_length=512, null=False)
    # 类型名称
    type_name = models.CharField(max_length=128, null=False)
    # 子分类名称(分类名称:分类id)
    child_type_name = models.CharField(max_length=512, default='全部分类:0')
    # 分类排序
    type_sort = models.IntegerField(default=1)

    class Meta:
        db_table = 'food_type'


class Goods(models.Model):
    """商品表"""
    # 商品编号
    goods_no = models.CharField(max_length=128, unique=True, null=False)
    # 商品名称
    goods_name = models.CharField(max_length=128, unique=True, null=False)
    # 商品图片
    goods_img = models.CharField(max_length=512, null=True)
    # 商品价格
    price = models.FloatField(default=0)
    # 商品计量单位
    unit = models.CharField(max_length=32, null=True)
    # 商品类型名称
    goods_type_name = models.CharField(max_length=128, null=True)
    # 所属分类id
    category = models.ForeignKey(FoodType, on_delete=models.CASCADE)
    # 所属分类的id
    childid = models.CharField(max_length=128)
    # 商品库存数量
    total = models.IntegerField(default=0)
    # 商品销量
    sale_num = models.IntegerField(default=0)

    class Meta:
        db_table = 'goods'


class MainShow(models.Model):
    """首页商品"""
    # 图片链接
    img = models.CharField(max_length=512)
    # 商品名称
    goods_name = models.CharField(max_length=128, unique=True, null=False)
    # 商品价格
    price = models.FloatField(default=0)
    # 商品计量单位
    unit = models.CharField(max_length=32, null=True)
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE)

    class Meta:
        db_table = 'main_show'
