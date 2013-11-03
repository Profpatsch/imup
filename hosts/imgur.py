#!/usr/bin/env python2
# encoding: utf-8
from hosts.imagehost import *
import json

POST_URL = "https://api.imgur.com/3/upload"
CLIENT_ID = "e7cd5fb500df8a7"


class Imgur(Imagehost):
    """imgur.com"""
    def __init__(self):
        super(Imgur, self).__init__()
        self.POST_URL = POST_URL

    def _request_post(self):
        with open(self.fn, 'rb') as f:
            headers = {'Authorization': 'Client-ID ' + CLIENT_ID}
            r = requests.post(POST_URL,
                    files={'image': (self.fn, f)}, headers=headers)
            return r

    def _handle_server_answer(self, answer):
        jansw = answer.json()
        if jansw["status"] == 200:
            return jansw["data"]["link"]
        else:
            return ImagehostError(json.dumps(jansw["data"]))
