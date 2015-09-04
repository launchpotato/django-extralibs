import json
import requests
import re


def get_instagram_followers(username):
    response = requests.get('https://instagram.com/%s/' % username)
    return re.search(r'followed_by":{"count":(\d+)}', response.content).groups()[0]


def get_facebook_likes(username):
    response = requests.get('https://graph.facebook.com/%s' % username)
    data = json.loads(response.content)
    return data['likes']
