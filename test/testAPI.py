import urllib.request
import urllib.parse, urllib.error
import time;
from random import randint
import requests
import json
from datetime import date, timedelta, datetime
import traceback


class TestAPI:
    '''This Class lets you test the Flask Article API by submitting some test Articles, 
        Authors, Regions'''
    
    
    def __init__(self, url = "http://161.35.201.165:5555/articles", title = "Sample Article", article = "Hello, this is a test"):
        
        self.url = url
        #self.request_payload = {"article":article, "region":region}
        self.request_payload = {'title': title , 'content': article}
        #self.request_payload = {'title': title , 'content': article}
        
        
    def _post_request(self):
        try:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
            r = requests.post(self.url, json=self.request_payload)
            return r.status_code
            
     
        except (urllib.error.HTTPError, urllib.error.URLError) as e:
            print(e)
        
            
        
    def _get_request(self):

        try:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
            user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0'
            headers={'User-Agent':user_agent} 
        
            r = requests.get(self.url)
            return r.status_code

        except (urllib.error.HTTPError, urllib.error.URLError) as e:
            print(e)
            print(traceback.print_exc())

   
    def _get_response(self):
        
        response = {}
        
        try:
            response = self._get_request()
            print(response)
            return response

        except Exception as e:
            print(e)
            
    
    def test_get(self):
        print("I will now make the specified request")
        result = self._get_response()
        return result
    
    def test_post(self):
        print("I will now post your payload")
        result = self._post_request()
        return result
    

if __name__ == "__main__":

    bla_get = TestAPI()
    response = bla_get.test_get()
    print(response)
