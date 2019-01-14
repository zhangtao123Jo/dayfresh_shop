#coding=utf-8
from django.http import HttpResponseRedirect

#登录就跳转用户中心,否则跳转登录

def isLogin(func):
    def login_fun(request,*args,**kwargs):
        if request.session.get('user_id'):
            return func(request,*args,**kwargs)
        else:
            red=HttpResponseRedirect("/user/login")
            red.set_cookie('url',request.get_full_path)
            return red
    return login_fun
