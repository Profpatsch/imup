#!/usr/bin/env python2
# −*− coding: UTF−8 −*−
import os
import re
import logging as log
import mimetypes

import requests

POST_URL = None


class Imagehost(object):
    """Abstract base class for image hosts."""
    def __init__(self):
        self.fn = None
        self.POST_URL = POST_URL

    def get_link(self, filename):
        """Upload image to this image host and return a link to it.

        Raises:
            ImagehostError
            FiletypeError (image not accepted)
            requests.exceptions.ConnectionError (Couldn’t contact server.)
        """
        self.fn = filename
        if not os.path.exists(self.fn):
            raise IOError("File doesn’t exist!")
        is_image, filetype = self.file_is_image()
        if not is_image:
            if filetype is None:
                raise FiletypeError("File is no image.")
            else:
                raise FiletypeError("File is no image, its Mimtype is {0}!"
                        .format(filetype))

        log.info("Uploading image…")
        answer = self._request_post()
        log.info("Image uploaded, evaluating server response…")
        link = self._handle_server_answer(answer)
        return link

    def file_is_image(self):
        """Checks if file is an image)MIME-type.

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
        """Post the image to the URL specified in self.POST_URL.

        Returns: requests.Response
        Raises: requests.exceptions.ConnectionError
        """
        with open(self.fn, 'rb') as f:
            r = requests.post(self.POST_URL, files={'image': (self.fn, f)})
            return r

    def _handle_server_answer(self, response):
        """Handles the strings returned by the server, mostly JSON or XML.
        Most likely needs to be implemented by each image host module in a
        different way.

        Args: requests.Response
        Returns: Link to image
        Error: ImagehostError
        """
        pass

class FiletypeError(IOError):
    """Filetype the server can't handle."""
    pass
class ImagehostError(Exception):
    """General error to be used when the image host returns an error."""
    pass
