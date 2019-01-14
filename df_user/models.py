from django.db import models

# Create your models here.
class UserInfo(models.Model):
    uname=models.CharField(verbose_name="用户名",max_length=20)
    upwd=models.CharField(verbose_name="密码",max_length=40)
    uemail=models.CharField(verbose_name="电子邮箱",max_length=30)
    ushou=models.CharField(verbose_name="收件人",max_length=20,default="")
    uaddress=models.CharField(verbose_name="收件地址",max_length=100,default="")
    uyoubian=models.CharField(verbose_name="邮编",max_length=6,default="")
    uphone=models.CharField(verbose_name="电话号码",max_length=15,default="")

    class Meta:
        verbose_name="用户信息"
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.uname


