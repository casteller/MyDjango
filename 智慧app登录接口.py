import requests
class Login(object):
    def login(self,username):
        url ='http://10.206.4.70:35000/a/sys/user/validateLogin.ws'
        payload = {'loginName':username,'pwd':'1qaz2edc3tgb','key':'1571210600675','license':'067cb1a85231cac42337b430afd98408'}
        req= requests.post(url,data=payload)
        userName = req.json()['userName']
        mobile=req.json()['mobile']
        return userName,mobile

if __name__=='__main__':
    p=Login()
    try:
        path = r'C:/Users/Administrator/Desktop/username.txt'
        with open(path,'r')as f:
            names = f.read().splitlines()
            for name in  names:
                print(p.login(name))
    except:
        pass

