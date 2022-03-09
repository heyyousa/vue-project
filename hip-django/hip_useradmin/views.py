from django.shortcuts import render
import os
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from hip_useradmin.models import *
from django.db.models import Q
from django.core import serializers
from django.shortcuts import render, redirect
import json
import socket


# Create your views here.

def get_uicons(request):
    iconslist = Usericons.objects.filter(Q(is_active=True))
    allicons = []

    for i in range(0, len(iconslist)):
        iconsobj = {}
        iconsobj['index'] = iconslist[i].index
        iconsobj['url'] = iconslist[i].iconurl
        allicons.append(iconsobj)

    jsondata = json.dumps(allicons)

    return HttpResponse(jsondata)


def update_icons(request):
    iconfolder = os.path.abspath('media\\img\\usericon\\')
    iconslist = os.listdir(iconfolder)

    # 自动识别后端主机ip给图片url用
    hostname = socket.gethostname()
    hostip = socket.gethostbyname(hostname)

    db_last_icon = Usericons.objects.last()
    # 数据库内icon为空时执行
    if not bool(db_last_icon):
        # 头像根路径
        baseurl = 'http://' + hostip + ':8000/media/img/usericon/'

        for n in range(0, len(iconslist)):
            new_last = Usericons.objects.last()
            if not bool(new_last):
                lindex = "0000000001"
                iconindex = lindex
            else:
                lindex = int(new_last.index)
                lindex += 1
                iconindex = str(lindex).zfill(10)

            iconurl = baseurl + iconslist[n]

            Usericons.objects.create(index=iconindex, iconurl=iconurl)

    return HttpResponse('1')


