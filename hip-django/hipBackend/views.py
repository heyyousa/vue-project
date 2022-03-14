from django.shortcuts import render, redirect
import xlrd

def indexpage(request):
    return render(request,'index.html')


# 处理核酸表函数
# def dealexcel (request):
