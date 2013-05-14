#!/usr/bin/env python
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
            datagen, headers = multipart_encode({'image': f})
            headers['Authorization'] = 'Client-ID ' + CLIENT_ID
            req = urllib2.Request(self.POST_URL, datagen, headers)
            answer = urllib2.urlopen(req)
            return answer.read()

    def _handle_server_answer(self, answer):
        jansw = json.loads(answer)
        if jansw["status"] == 200:
            return jansw["data"]["link"]
        else:
            return ImagehostError(json.dumps(jansw["data"]))
