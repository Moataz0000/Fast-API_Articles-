import requests




class CallAPI:
    
    @staticmethod
    def getMethod(url):
        request = requests.get(url=url)
        print(request.json())
        
    
    @staticmethod
    def postMethod(url, data):
        request = requests.post(url=url, json=data)
        response = request.json()
        print(response)
        
    @staticmethod
    def putMethod(url, Newdata):
        request = requests.put(url=url, json=Newdata)
        print(request.json())
        
    @staticmethod    
    def deleteMethod(url):
        request = requests.delete(url=url)
        print(request.json())
        
        
data = {
    "title": "New Post",
    "content": "The content!"
}

data2 = {
    "title": "Update Post",
    "content": "The content!"
}

url = 'http://127.0.0.1:8000/posts/0/'


call = CallAPI()
call.postMethod(url='http://127.0.0.1:8000/posts/', data=data)
call.deleteMethod(url=url)