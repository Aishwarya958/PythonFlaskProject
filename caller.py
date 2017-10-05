#!/usr/bin/python
# This file is a console based app to call the API's

import requests
import json
import sys


class Caller:

    def post_ad(self):
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
        return res.text

        # print '\nThank you for Posting the AD  !'

    def get_ad(self):
        res = requests.get('http://127.0.0.1:8080/showAds')
        print res.text
        return res.json()

    def update_ad(self):

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

