from caller import Caller
import unittest
import mock


def mocked_request(*args, **kwargs):
    class MockResponse:
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

    def setUp(self):
        self.c = Caller()

    @mock.patch('requests.get', side_effect=mocked_request)
    def test_get_ad(self, m):
        print '\n---Test Get Ad---'
        response_data =  self.c.get_ad()
        self.assertEquals(response_data, {"get_ad": "OK"})


    @mock.patch('requests.post', side_effect=mocked_request)
    def test_post_ad(self, m):
        print '\n---Test Post Ad---'
        response_data =  self.c.post_ad()
        self.assertEquals(response_data, {"post_ad": "OK"})

    @mock.patch('requests.delete', side_effect=mocked_request)
    def test_delete_ad(self, m):
        print '\n---Test Delete Ad---'
        response_data =  self.c.delete_ad()        
        self.assertEquals(response_data, {"delete_ad": "OK"})

    @mock.patch('requests.put', side_effect=mocked_request)
    def test_update_ad(self, m):
        print '\n---Test Update Ad--'
        response_data =  self.c.update_ad()
        self.assertEquals(response_data, {"update_ad": "OK"})

    def tearDown(self):
        del self.c

if __name__ == '__main__':
  unittest.main()     
       
