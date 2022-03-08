# 前后端API
--------
## 前端部分
#### 1. 获取头像   
**get_uicons()** 前端请求全部可用头像图片的函数    
调用的axios模块：http-hip.js   
使用的函数：axiosHip.get()   
接口url：'/hipud/get_uicons/'   
传参：无


------------
## 后端部分（供前端）
#### 1. 获取头像
**get_uicons()** 将存储在后端的全部可用头像的url发送给前端   
请求url：'http://192.168.xxx.xxx:8000/hipud/get_uicons/'   
传参：无   
返回数据：json，列表包含对象格式[{..},{..}]

键名     | 值
-------- | -------------
index    | 图片在数据库内的主键索引值
iconurl  | 图片src地址



--------------
## 后端部分（自用）
#### 1. 更新数据库头像   
**update_icons()** 将media文件夹内的新头像记录到数据库中   
请求url：'http://192.168.xxx.xxx:8000/hipud/update_icons/'   
传参：无   
返回数据：HttpResponse，成功提示信息
