#!/usr/bin/python
# UnitTest the Caller
from caller import Caller
import unittest
import mock


def mocked_request(*args, **kwargs):
    '''Return a response when a particular url is called.The response is 
     mocked i.e we define the expected response without actually returning 
     the url's response.
     '''   
    class MockResponse:
        '''Renders the function of the actual Response object'''
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data
        
        @property
        def text(self):
            return self.json_data
        
    if args[0] == "http://127.0.0.1:8080/showAds":
        return MockResponse({"get_ad": "OK"}, 200)

    elif args[0] == "http://127.0.0.1:8080/postAd":
        return MockResponse({"post_ad": "OK"}, 200)

    elif args[0] == "http://127.0.0.1:8080/deleteAd":
        return MockResponse({"delete_ad": "OK"}, 200)

    elif args[0] == "http://127.0.0.1:8080/updateAd/ash/b":
        return MockResponse({"update_ad": "OK"}, 200)
    else:
        return MockResponse(None, 404)

class TestCaller(unittest.TestCase):
    ''' Tests the functons of caller.py'''
    def setUp(self):
        self.c = Caller()

    # Annotation to mock responses 
    @mock.patch('requests.get', side_effect=mocked_request)
    def test_get_ad(self, m):
        '''Actually calls the get_ad function from caller.py executes it line
        by line and the return statement returns the mocked response'''
        print '\n---Test Get Ad---'
        response_data =  self.c.get_ad()
        self.assertEquals(response_data, {"get_ad": "OK"})


    @mock.patch('requests.post', side_effect=mocked_request)
    def test_post_ad(self, m):
        '''Actually calls the post_ad function from caller.py executes it line
        by line and the return statement returns the mocked response'''
        print '\n---Test Post Ad---'
        response_data =  self.c.post_ad()
        self.assertEquals(response_data, {"post_ad": "OK"})

    @mock.patch('requests.delete', side_effect=mocked_request)
    def test_delete_ad(self, m):
        '''Actually calls the delete_ad function from caller.py executes it line
        by line and the return statement returns the mocked response'''
        print '\n---Test Delete Ad---'
        response_data =  self.c.delete_ad()        
        self.assertEquals(response_data, {"delete_ad": "OK"})

    @mock.patch('requests.put', side_effect=mocked_request)
    def test_update_ad(self, m):
        '''Actually calls the update_ad function from caller.py executes it line
        by line and the return statement returns the mocked response'''
        print '\n---Test Update Ad--'
        response_data =  self.c.update_ad()
        self.assertEquals(response_data, {"update_ad": "OK"})

    def tearDown(self):
        del self.c

if __name__ == '__main__':
  unittest.main()     
       
