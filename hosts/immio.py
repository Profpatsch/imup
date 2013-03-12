import imagehost
import json
from ..libposter.encode import multipart_encode
from ..libposter.streaminghttp import register_openers
import urllib2

class Immio(Imagehost):
    def get_link(self, filename):
        self.fn = filename
        if self.file_is_image()



