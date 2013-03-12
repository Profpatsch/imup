import mimetypes as mt
import re

class Imagehost:
    def __init__(self):
        self.fn = None
    def get_link(self, filename):
        """Upload image to this image host and return a link to it."""
        self.fn = filename
        pass
    def file_is_image(self):
        """Checks if file is an image MIME-type"""
        type, _ = mt.guess_type(self.fn, strict=False)
        if type:
            if re.match(r"image/", type):
                return True
        return False

class FiletypeError(Exception):
    pass
