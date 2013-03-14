#!/usr/bin/env python2
# −*− coding: UTF−8 −*−
from libposter.encode import multipart_encode

import urllib2
import mimetypes as mt
import re
import logging as log

POST_URL = None

class Imagehost(object):
    """Abstract base class for image hosts."""
    def __init__(self):
        self.fn = None
        self.POST_URL = POST_URL

    def get_link(self, filename):
        """Upload image to this image host and return a link to it.
        
        Error:
            ImagehostError
            FiletypeError (image not accepted)
            URLError (Couldn’t contact server.)
        """
        self.fn = filename
        if not self.file_is_image():
            raise FiletypeError("File is no image!")
        log.info("Uploading image…")
        answer = self._request_post();
        log.info("Image uploaded, evaluating server response…")
        link = self._handle_server_answer(answer)
        return link

    def file_is_image(self):
        """Checks if file is an image MIME-type"""
        type, _ = mt.guess_type(self.fn, strict=False)
        if type:
            if re.match(r"image/", type):
                return True
        return False

    def _request_post(self):
        """Post the image to the URL specified in self.POST_URL
        
        Returns: Server answer (str)
        Error: URLError
        """
        with open(self.fn, 'rb') as f:
            datagen, headers = multipart_encode({'image': f})
            # Post image to host
            req = urllib2.Request(self.POST_URL, datagen, headers)
            answer = urllib2.urlopen(req)
            return answer.read()

    def _handle_server_answer(self, answer):
        """Handles the strings returned by the server, mostly JSON or XML.
        Most likely needs to be implemented by each image host module in a
        different way.
        
        Input: Server answer
        Returns: Link to image
        Error: ImagehostError
        """
        pass

class FiletypeError(Exception): pass
class ImagehostError(Exception): pass
