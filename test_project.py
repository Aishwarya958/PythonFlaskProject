#!/usr/bin/python
import project
import unittest
import tempfile
import os
import json
import mock



class TestProject(unittest.TestCase):
    ''' Tests the functions of project.py'''
    def setUp(self):
        '''creates a new test client and initializes a new database.Because 
          SQLite3 is filesystem-based we can easily use the tempfile module 
          to create a temporary database and initialize it. The mkstemp()
          function does two things for us: it returns a low-level file 
          handle and a random file name, the latter we use as database name. 
          We just have to keep the db_fd around so that we can 
          use the os.close() function to close the file.'''
       
        self.db_fd, project.app.config['DATABASE'] = tempfile.mkstemp()
        # disable the error catching during request handling
        project.app.testing = True

        #client will give us a simple interface to the application
        self.app = project.app.test_client()

        with project.app.app_context():
            project.init_db()

   
    def test_post_ad(self):
        '''A dictonary of the dummy post ad data is created and postAd 
        url is called.This inserts the data in the dummy database instead
        of the real one.The status_code is checked.By using self.app.post we
        can send an HTTP GET request to the application with the given path. 
        The return value will be a response_class object.
       '''
        post_ad_data = {
            'firstname': 'Aishwarya',
            'title': 'Mobile',
            'category': 'Electro',
            'description': 'Lenovo',
            'phone': 20,
            }
        headers = {'Content-Type': 'application/json'}
        rv = self.app.post('/postAd', data=json.dumps(post_ad_data), 
                                      headers=headers)
        self.assertEqual(rv.status_code,200)

    def test_delete_ad(self):
        '''A dictonary of the dummy delete ad data is created and deleteAd 
        url is called.This delets the data in the dummy database instead
        of the real one.The status_code is checked.
       '''
        delete_ad_data = {'firstname': 'Aishwarya', 'title': 'Bottle'}
        headers = {'Content-Type': 'application/json'}
        rv = self.app.delete('/deleteAd', data=json.dumps(delete_ad_data), 
                              headers=headers)
        self.assertEqual(rv.status_code,200)
    
    def test_get_ad(self):        
        rv = self.app.get('/showAds')
        self.assertEqual(rv.status_code,200)
    
    def test_update_ad(self):
        '''A dictonary of the dummy update ad data is created and updateAd 
        url is called.This updates the data in the dummy database instead
        of the real one.The status_code is checked.
        '''
        new_ad_data = {
            'firstname': 'Ash',
            'title': 'Chair',
            'category': 'HouseHold',
            'description': 'White',
            'phone': 9922564632}

        fname = 'Aishwarya'
        title = 'Bottle'     
        headers = {'Content-Type': 'application/json'}
        rv = self.app.put('/updateAd/{}/{}'.format(fname, title), 
                         data=json.dumps(new_ad_data),headers=headers)
        self.assertEqual(rv._content,200)
    
    def tearDown(self):
        '''delete the database after the test,close the file and
            remove it from the filesystem
        '''
        os.close(self.db_fd)
        os.unlink(project.app.config['DATABASE'])

   

if __name__ == '__main__':
  unittest.main()     
       
