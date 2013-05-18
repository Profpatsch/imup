#!/usr/bin/env python2
# −*− coding: UTF−8 −*−
from libposter.encode import multipart_encode

import urllib2
import mimetypes
import re
import logging as log
import os

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
        if not os.path.exists(self.fn):
            raise IOError("File doesn’t exist!")
        is_image, filetype = self.file_is_image()
        if not is_image:
            if filetype is None:
                raise FiletypeError("File is no image.")
            else:
                raise FiletypeError("File is no image, it’s Mimtype is {0}!"
                        .format(filetype))

        log.info("Uploading image…")
        answer = self._request_post()
        log.info("Image uploaded, evaluating server response…")
        link = self._handle_server_answer(answer)
        return link

    def file_is_image(self):
        """Checks if file is an image MIME-type.

        Returns: (bool, mimestring)
        """
        type, _ = mimetypes.guess_type(self.fn, strict=False)
        if type is None:
            import subprocess
            try:
                p = subprocess.Popen(["xdg-mime", "query", "filetype", self.fn], stdout=subprocess.PIPE)
                out, _ = p.communicate()
                type = out.strip()
            except OSError:
                return (False, None)
        if re.match(r"image/", type):
            return (True, None)
        else:
            return (False, type)

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

class FiletypeError(IOError): pass
class ImagehostError(Exception): pass
