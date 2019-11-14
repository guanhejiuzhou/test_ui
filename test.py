import sys
print(sys.version)

#-*-coding:utf-8-*-

import requests
import json
import urllib3
urllib3.disable_warnings()


#客户端发送请求到服务端，服务端返回数据
r=requests.post('https://passport.lagou.com/login')
print('返回的响应数据内容：\n{0}'.format(r.text))
print('HTTP协议返回的状态码：\n{0}'.format(r.status_code))
print('返回的Headers信息：\n{0}'.format(r.headers))
print('返回的cookies信息：\n{0}'.format(r.cookies))


'''
#URL参数实战
r=requests.get(
    url='https://cart.taobao.com/trail_mini_cart.htm',
    params={'callback':'MiniCart.setData','t':'1526048972328'}
)
print('请求的URL为：\n{0}'.format(r.url))
print('返回的响应数据内容：\n{0}'.format(r.text))
'''


'''
#添加请求头
r=requests.get(
    url='https://cart.taobao.com/trail_mini_cart.htm',
    params={'callback':'MiniCart.setData','t':'1526048972328'},
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1;WOW64) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/55.0.2883.87 Safari/537.36',
             'Content-Type':'application/json',
             'Referer':'https://shoucang.taobao.com/shop_collect_list.htm?spm=a21bo.2017.1997525053.3.5af911d9sYX701'}
)
print('响应内容：\n{0}'.format(r.text))
'''

'''
#data参数
def getHeaders():
    headers={
        'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1;Win64;x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81Safari/537.36'
    }
    return headers

dict1={'phone':'86134****5195','password':'password','oneMonth':1}

def chouTi():
    r=requests.post(
        url='https://dig.chouti.com/login',
        data=dict1,
        headers=getHeaders(),
        verify=False
    )
    print(json.dumps(r.json(),indent=True))

if __name__=='__main__':
    chouTi()
'''

'''
#json参数
def getHeaders():
    headers={
        'Content-Type':'application/json;charset=UTF-8',
        'Parkingwang-Client-Source':'ParkingwangAPIClientWeb'
    }
dict1={"source":"common","password":""}
def login():
    r=requests.post(
        url='https://passport.lagou.com/login/login.html',
        data=json.dumps(dict1), #对请求参数做序列化处理
        headers=getHeaders()
    )
    print(json.dumps(r.json(),indent=True,ensure_ascii=False))

if __name__=='__main__':
    login()
'''


