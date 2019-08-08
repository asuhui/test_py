#coding:utf-8
#导入request库
import  requests

#请求URL
url = "http://192.1.8.49:8080/E6300"
#请求数据
data = {
    "username":"admin",
    "password":"admin"
 }
#发送请求,一般还需要提供header信息，此处为demo，暂不关注
reponse1 = requests.post(url=url,data=data)
res_json = reponse1.json()
print(res_json)
flag =  reponse1.status_code == 200  and res_json["status"] == 200  and res_json["msg"]=="login sucesss"
#假如http code为200，status为“200” msg为“login sucesss”则测试通过
if flag:
    print("pass")
else:
    print("fail")