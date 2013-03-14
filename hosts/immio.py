#!/usr/bin/env python
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
        jansw = json.loads(answer)
        if not (jansw["success"]):
            #TODO Split errors.
            return ImagehostError(json.dumps(janw["payload"]))
        return jansw["payload"]["uri"]