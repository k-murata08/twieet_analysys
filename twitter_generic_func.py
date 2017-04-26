#!/usr/bin/env python
# -*- coding: utf-8 -*-

from requests_oauthlib import OAuth1Session
import json
import const as C


def get_followers(user_id, users_count):
    url = "https://api.twitter.com/1.1/followers/list.json?"
    params = {
        "user_id": user_id,
        "count": users_count
        }
    oath = create_oath_session(C.OATH_KEY_DICT)
    responce = oath.get(url, params = params)
    if responce.status_code != 200:
        print "Error code: %d" %(responce.status_code)
        return None
    followers = json.loads(responce.text, 'utf-8')
    return followers['users']


def get_follower_ids(user_id, users_count):
    url = "https://api.twitter.com/1.1/followers/ids.json?"
    params = {
        "user_id": user_id,
        "count": users_count
        }
    oath = create_oath_session(C.OATH_KEY_DICT)
    responce = oath.get(url, params = params)
    if responce.status_code != 200:
        print "Error code: %d" %(responce.status_code)
        return None
    follower_ids = json.loads(responce.text, 'utf-8')
    return follower_ids['ids']


# user_idのユーザがフォローしているユーザ
def get_friends(user_id, users_count):
    url = "https://api.twitter.com/1.1/friends/list.json?"
    params = {
        "user_id": user_id,
        "count": users_count
        }
    oath = create_oath_session(C.OATH_KEY_DICT)
    responce = oath.get(url, params = params)
    if responce.status_code != 200:
        print "Error code: %d" %(responce.status_code)
        return None
    friends = json.loads(responce.text, 'utf-8')
    return friends['users']


def get_friend_ids(user_id, users_count):
    url = "https://api.twitter.com/1.1/friends/ids.json?"
    params = {
        "user_id": user_id,
        "count": users_count
        }
    oath = create_oath_session(C.OATH_KEY_DICT)
    responce = oath.get(url, params = params)
    if responce.status_code != 200:
        print "Error code: %d" %(responce.status_code)
        return None
    friend_ids = json.loads(responce.text, 'utf-8')
    return friend_ids['ids']


def get_user_profile(user_id):
    url = "https://api.twitter.com/1.1/users/show.json?"
    params = {
        "user_id": user_id
        }
    oath = create_oath_session(C.OATH_KEY_DICT)
    responce = oath.get(url, params = params)
    if responce.status_code != 200:
        print "Error code: %d" %(responce.status_code)
        return None
    profile = json.loads(responce.text, 'utf-8')
    return profile


# クエリを飛ばす時にしか使わない
def create_oath_session(oath_key_dict):
    oath = OAuth1Session(
    oath_key_dict["consumer_key"],
    oath_key_dict["consumer_secret"],
    oath_key_dict["access_token"],
    oath_key_dict["access_token_secret"]
    )
    return oath