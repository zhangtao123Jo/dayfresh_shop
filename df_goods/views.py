from django.shortcuts import render,HttpResponse
from .models import GoodsInfo,TypeInfo
from django.core.paginator import Paginator
# Create your views here.
#查询每类商品中点击量最高和最新的的四个数据
def index(request):
    #负责查询页面中要展示的内容 最新的四种  和点击量最高的四种  每类商品查询两次
    fruit=GoodsInfo.objects.filter(gtype_id=1).order_by("-id")[:4]
    fruit2=GoodsInfo.objects.filter(gtype_id=1).order_by("-gclick")[:4]
    fish = GoodsInfo.objects.filter(gtype_id=2).order_by("-id")[:4]
    fish2 = GoodsInfo.objects.filter(gtype_id=2).order_by("-gclick")[:4]
    meat = GoodsInfo.objects.filter(gtype_id=3).order_by("-id")[:4]
    meat2 = GoodsInfo.objects.filter(gtype_id=3).order_by("-gclick")[:4]
    egg = GoodsInfo.objects.filter(gtype_id=4).order_by("-id")[:4]
    egg2 = GoodsInfo.objects.filter(gtype_id=4).order_by("-gclick")[:4]
    vegetable = GoodsInfo.objects.filter(gtype_id=5).order_by("-id")[:4]
    vegetable2 = GoodsInfo.objects.filter(gtype_id=5).order_by("-gclick")[:4]
    frozen = GoodsInfo.objects.filter(gtype_id=6).order_by("-id")[:4]
    frozen2 = GoodsInfo.objects.filter(gtype_id=6).order_by("-gclick")[:4]

    return render(request,"df_goods/index.html",locals())

#商品列表界面
def goodlist(request,typeid,pageid,sort):
    '''
    负责展示某类商品的信息
    三个参数
    :param typeid: 商品类型id
    :param pageid: 页码
    :param sort: 排序条件  1->id排序 2->价格排序  3->人气排序 点击量
    '''
    #获取最新发布的商品
    newlist=GoodsInfo.objects.filter(gtype_id=typeid).order_by("-id")[:2]
    #根据条件查询所有的商品
    if sort=='1':   #按照id来查最新数据
        goodList=GoodsInfo.objects.filter(gtype_id=typeid).order_by("-id")
    elif sort=='2':  #按照价格排序
        goodList = GoodsInfo.objects.filter(gtype_id=typeid).order_by("gprice")
    elif sort=='3':    #按点击量排序
        goodList = GoodsInfo.objects.filter(gtype_id=typeid).order_by("-gclick")

    #进行分页
    paginator=Paginator(goodList,per_page=5)  #每页的个数
    #根据页码生成goodList
    goodList=paginator.page(int(pageid))
    pindexlist=paginator.page_range

    #获取商品类型
    gtype=TypeInfo.objects.get(id=typeid).ttitle

    pageid=int(pageid)
    typeid=typeid
    sort=sort
    return render(request,"df_goods/list.html",locals())

#商品详情页面
def detail(request,good_id):
    g=GoodsInfo.objects.get(id=good_id)
    g.gclick=g.gclick+1
    #保存修改后的结果
    g.save()

    gtype=TypeInfo.objects.get(id=g.gtype_id).ttitle
    #最新插入的两个商品
    newlist = GoodsInfo.objects.filter(gtype_id=g.gtype_id).order_by("-id")[:2]

    response= render(request,"df_goods/detail.html",locals())
    #使用cookie记录最新浏览的商品id
    #获取cookies
    goods_ids=request.COOKIES.get('goods_id','')  #字符串
    goods_id=good_id #获取点击商品的id
    #判断COOKIES中浏览商品的列表是否为空
    if goods_ids != "":
        #分割原来浏览过的字符串   转换为列表
        goods_id_list=goods_ids.split(",")
        #判断当前商品是否存在列表中
        if goods_id_list.count(goods_id)>=1:
            #说明已经存在   就移除这一条 添加到第一条
            goods_id_list.remove(goods_id)
        goods_id_list.insert(0,goods_id)
        #浏览记录不能超过5个
        if len(goods_id_list)>5:
            del goods_id_list[5]
        #拼接新的id到原来的cookies中
        goods_ids = ",".join(goods_id_list)
    else:
        goods_ids=goods_id
        #设置到cookie当中 [1,2,3] -->  1,2,3
    response.set_cookie("goods_id",goods_ids)

    return response
