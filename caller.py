#!/usr/bin/python
# This file is a console based app to call the API's

import requests
import json
import sys


class Caller:
    '''This class Consumes the Server Side Rest API.'''

    def post_ad(self):
        '''This function accepts the PostAD data from the user,makes a dictonary
        of the values and calls the server url /postAd with the parameters: 
        dictonary of the values and the header.The response returned by the
        server is printed on the console and returned.  
       '''

        post_ad_data = {}
        firstname = raw_input('Enter firstname: ')
        title = raw_input('Enter the Title: ')
        category = raw_input('Enter the Category: ')
        description = raw_input('Enter Description: ')
        phone = int(raw_input('Enter Phone Number: '))

        post_ad_data = {
            'firstname': firstname,
            'title': title,
            'category': category,
            'description': description,
            'phone': phone,
            }

        headers = {'Content-Type': 'application/json'}

        res = requests.post('http://127.0.0.1:8080/postAd',
                            data=json.dumps(post_ad_data),
                            headers=headers)

        print 'Ad Posted Successfully'
        print res.text        
        print '\nThank you for Posting the AD  !'
        return res.text

    def get_ad(self):
        '''Calls the /showAds url which returns all the posted Ads'''

        res = requests.get('http://127.0.0.1:8080/showAds')
        print res.text
        return res.json()

    def update_ad(self):
        '''Accepts the firstname of the user and the title of the Ad which the 
        user wants to edit, then it accepts the new Ad data and forms a 
        dictonary of all the values and passes this to the /updateAd/fname
        /title url along with header.The response returned is printed.
        '''

        fname = raw_input('Enter firstname of ad to update : ')
        title = raw_input('Enter the Title of ad to update: ')
        print 'Enter the new data'
        new_ad_data = {}
        new_firstname = raw_input('Enter firstname: ')
        new_title = raw_input('Enter the Title: ')
        category = raw_input('Enter the Category: ')
        description = raw_input('Enter Description: ')
        phone = int(raw_input('Enter Phone Number: '))

        new_ad_data = {
            'firstname': new_firstname,
            'title': new_title,
            'category': category,
            'description': description,
            'phone': phone,
            }

        headers = {'Content-Type': 'application/json'}
        res = \
            requests.put('http://127.0.0.1:8080/updateAd/{0}/{1}'.format(fname,
                         title), data=json.dumps(new_ad_data),
                         headers=headers)

        print res.text
        return res.json()

    def delete_ad(self):
        '''Accepts the firstname of the user and the title of the Ad which the 
        user wants to delete and forms a 
        dictonary of the values and passes this to the /deleteAd url along
        with header.The response returned is printed.
       '''       
        delete_ad_data = {}
        firstname = raw_input('Enter firstname: ')
        title = raw_input('Enter the Title: ')

        delete_ad_data = {'firstname': firstname, 'title': title}
        headers = {'Content-Type': 'application/json'}

        res = requests.delete('http://127.0.0.1:8080/deleteAd',
                              data=json.dumps(delete_ad_data),
                              headers=headers)
        print res.text
        return res.json()


if __name__ == '__main__':

    c = Caller()
    while True:
        print '----MENU----'
        print '''
1.PostAD
2.GetAd
3.UpdateAd
4.Delete Ad
5.Exit'''
        n = int(raw_input('Enter your choice: '))
        # Call the respective methods
        if n == 1:
            c.post_ad()

        if n == 2:
            c.get_ad()

        if n == 3:
            c.update_ad()

        if n == 4:
            c.delete_ad()

        if n == 5:
            sys.exit(0)
        else:
            pass

