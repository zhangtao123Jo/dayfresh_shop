
from django.conf.urls import url
# import df_goods.views
from .import views
urlpatterns = [
    url(r'^$',views.index),
    #第一个参数代表类型typeid(类型id)  第二个参数代表分页  第三个参数代表排序
    url(r'^typelist_(\d+)_(\d+)_(\d+)$',views.goodlist),
    url(r'^(\d+)$',views.detail),
]