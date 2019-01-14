from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
from hashlib import sha1
from .models import UserInfo
from df_goods.models import GoodsInfo
# Create your views here.
#注册界面
def register(request):
    return render(request,"df_user/register.html")

#注册界面 点击提交之后的方法
def register_handle(request):
    #接收用户输入
    post=request.POST
    uname=post.get("user_name")
    upwd=post.get("pwd")
    ucpwd=post.get("cpwd")
    uemail=post.get("email")
    if upwd != ucpwd:  #密码不一致
        return redirect("/user/register")
    s1=sha1()
    s1.update(upwd.encode("utf8"))
    unewpwd=s1.hexdigest()   #加密之后的密码

    #保存数据库
    user=UserInfo()
    user.uname=uname
    user.upwd=unewpwd
    user.uemail=uemail
    user.save()
    #跳转到登录界面
    return redirect("/user/login")

def login(request):
    #获取本地浏览器保存的用户名记录
    uname=request.COOKIES.get("uname","")
    context={'title':'用户登录','error_name':0,'error_pwd':0,'uname':uname}
    return render(request,"df_user/login.html",context)

def login_handle(request):
    # 接收用户输入
    post = request.POST
    uname=post.get("username")
    upwd=post.get("pwd")
    jizhu=post.get("jizhu",0)
    #根据用户名查询用户
    users=UserInfo.objects.filter(uname=uname)
    if len(users)>0:
        #先判断用户存在,再判断密码是否正确
        s1 = sha1()
        s1.update(upwd.encode("utf8"))
        unewpwd = s1.hexdigest()  # 加密之后的密码
        if unewpwd==users[0].upwd:    #说明密码正确
            red=HttpResponseRedirect("/goods")
            #设置登录带的Cookie值 浏览器缓存记录  判断是否记住用户名
            if jizhu!=0:
                red.set_cookie("uname",uname)
            else:
                red.set_cookie("uname","",max_age=-1)
            request.session["user_id"]=users[0].id
            request.session["user_name"]=users[0].uname
            return red
        else:
            context={'title':'用户登录','error_name':0,'error_pwd':1,'uname':uname}
            return render(request,"df_user/login.html",context)
    else:
        context = {'title': '用户登录', 'error_name': 1, 'error_pwd': 0, 'uname': uname}
        return render(request, "df_user/login.html", context)

from .isLogin import isLogin

@isLogin
def info(request):
    user_email=UserInfo.objects.get(id=request.session['user_id']).uemail
    user_address = UserInfo.objects.get(id=request.session['user_id']).uaddress
    user_name = UserInfo.objects.get(id=request.session['user_id']).uname
    #最近浏览记录
    #获取最新浏览信息  id
    goods_ids = request.COOKIES.get('goods_id', '')  # 字符串结构
    good_ids_list=goods_ids.split(",")   #转换成列表结构[1,2,3]
    goods_list=[]
    try:
        if len(good_ids_list)>0:
            for good_id in good_ids_list:
                good=GoodsInfo.objects.get(id=int(good_id))
                goods_list.append(good)
    except:
        goods_list=[]
    context={'title':'用户中心','user_name':user_name,'user_email':user_email,
             'user_address':user_address,'goods_list':goods_list}
    return render(request,'df_user/user_center_info.html',context)

def loginout(request):
    request.session.flush()
    return redirect('/user/login')