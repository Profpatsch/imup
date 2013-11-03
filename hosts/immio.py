#!/usr/bin/env python2
# −*− coding: UTF−8 −*−
from hosts.imagehost import *
import json

POST_URL = "http://imm.io/store/"

class Immio(Imagehost):
    """imm.io"""
    def __init__(self):
        super(Immio, self).__init__()
        self.POST_URL = POST_URL

    def _handle_server_answer(self, answer):
        jansw = answer.json()
        if not (jansw["success"]):
            raise ImagehostError(json.dumps(jansw["payload"]))
        return jansw["payload"]["uri"]
