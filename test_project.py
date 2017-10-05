import project
import unittest
import tempfile
import os
import json
import mock



class TestProject(unittest.TestCase):

    def setUp(self):
        self.db_fd, project.app.config['DATABASE'] = tempfile.mkstemp()
        project.app.testing = True
        self.app = project.app.test_client()
        with project.app.app_context():
            project.init_db()

   
    def test_post_ad(self):
        post_ad_data = {
            'firstname': 'Aishwarya',
            'title': 'Mobile',
            'category': 'Electro',
            'description': 'Lenovo',
            'phone': 20,
            }
        headers = {'Content-Type': 'application/json'}
        rv = Mock(spec=Responseaiaishwarya
aiiiii)
        rv = self.app.post('/postAd', data=json.dumps(post_ad_data), 
                                      headers=headers)
        self.assertEqual(rv.status_code,200)

    def test_delete_ad(self):
        delete_ad_data = {'firstname': 'Aishwarya', 'title': 'Bottle'}
        headers = {'Content-Type': 'application/json'}
        rv = self.app.delete('/deleteAd', data=json.dumps(delete_ad_data), 
                              headers=headers)
        self.assertEqual(rv.status_code,200)
    
    def test_get_ad(self):        
        rv = self.app.get('/showAds')
        self.assertEqual(rv.status_code,200)
    
    def test_update_ad(self):
       new_ad_data = {
            'firstname': 'Ash',
            'title': 'Chair',
            'category': 'HouseHold',
            'description': 'White',
            'phone': 9922564632}

       fname = 'Aishwarya'
       title = 'Bottle'     
        
       rv = self.app.put('/updateAd/{}/{}'.format(fname, title), data=json.dumps(new_ad_data),
                                          headers={'Content-Type': 'application/json'})
       self.assertEqual(rv._content,200)
    
    def tearDown(self):

        os.close(self.db_fd)
        os.unlink(project.app.config['DATABASE'])

   

if __name__ == '__main__':
  unittest.main()     
       
