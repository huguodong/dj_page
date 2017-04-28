from django.shortcuts import render
from  demo.models import *


# Create your views here.
# Create your views here.
def index(request):
    # u = user()
    # u.UserName='admin'
    # u.UserPwd='123'
    # u.UserEmail='ad2ad@qq.com'
    # u.Phone='12333333333'
    # u.save()
    userlist = user.objects.all()
    # print userlist
    # for i in userlist:
    #     print  i.UserName
    return render(request, 'index.html', locals())

