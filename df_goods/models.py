from django.db import models
from tinymce.models import HTMLField
# Create your models here.

#商品的分类
class TypeInfo(models.Model):
    ttitle=models.CharField(verbose_name="商品分类",max_length=20)
    isDelete=models.BooleanField(verbose_name="是否删除",default=False)

    class Meta:
        verbose_name = "商品分类表"
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.ttitle

#商品表
class GoodsInfo(models.Model):
    gtitle=models.CharField(verbose_name="商品名称",max_length=20)
    #存储图片位置
    gpic=models.ImageField(upload_to="df_goods")
    gprice=models.DecimalField(max_digits=5,decimal_places=2,verbose_name="商品价格")
    isDelete=models.BooleanField(verbose_name="是否删除",default=False)
    #单位
    gunit=models.CharField(verbose_name="商品单位",default="500g",max_length=20)
    #人气点击量
    gclick=models.IntegerField(verbose_name='点击量')
    #简介
    gjianjie=models.CharField(verbose_name='商品简介',max_length=200)
    #库存
    gkucun=models.IntegerField(verbose_name='库存')
    #详细介绍
    gcontent=HTMLField()
    #商品类型
    gtype=models.ForeignKey(TypeInfo,verbose_name="商品类型")

    class Meta:
        verbose_name="商品表"
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.gtitle