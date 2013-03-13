from hosts.imagehost import *
import json
from libposter.encode import multipart_encode
import urllib

POST_URL = "http://imm.io/store/"

class Immio(Imagehost):
    """imm.io"""
    def __init__(self):
        super().__init__();
        self.POST_URL = POST_URL

    def _handle_server_answer(self, answer):
        jansw = json.loads(answer)
        if !jansw["success"]:
            return ImagehostError(json.dumps(janw["payload"]))
        return jansw["payload"]["uri"]
