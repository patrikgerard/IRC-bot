#!/usr/bin/env python3

import os
import sys
import requests
import pprint
from random import randrange

USERNAME = USERNAME-TO-SEARCH-FOR
base_url = 'https://www.reddit.com/'
data = {'grant_type': 'password', 'username': YOUR-USERNAME,  'password': YOUR-PASSWORD}
auth = requests.auth.HTTPBasicAuth('QjUisJgCq1Z3TA', 'WXjMHSiyKPd652LqoEbBwctVeb2SbA')
comments_req = 50

def get_token():
	r = requests.post(base_url + 'api/v1/access_token',
          data=data,
          headers={'user-agent': 'APP-NAME by REDDIT-USERNAME'},
		  auth=auth)
	d = r.json()
	return 'bearer ' + d['access_token']


def get_random_reddit_comment(token):
	base_url = 'https://oauth.reddit.com'
	headers = {'Authorization': token, 'User-Agent': 'APP-NAME by REDDIT-USERNAME'}
	response = requests.get(base_url + '/api/v1/me', headers=headers)


	if response.status_code == 200:
		payload = {'username': USERNAME,'limit': comments_req, 'sort': 'top'}
		response = requests.get(base_url + '/user/username/comments', headers = headers, params = payload)
		
		comments = response.json()
		comments = comments['data']['children']
		comments = [comment['data']['body'].replace("\n", "") for comment in comments]
		
		dumb_comment = ""
		index = True
		
		for letter in comments[randrange(comments_req)]:
			if index:
				dumb_comment += letter.upper()
			else:
				dumb_comment += letter.lower()
			if letter != ' ':
				index  = not index
		return dumb_comment





def main():

	token = get_token()
	comment = get_random_reddit_comment(token)
	print(comment)




if __name__ == '__main__':
	main()
