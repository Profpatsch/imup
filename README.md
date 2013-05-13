imup
====

usage: `imup.py [-h] [-i hostname] [-v] [-V] filename`

Takes a filename to an image, uploads it to the specified image host (random
if none given) and returns the link to the uploaded image.

    positional arguments:
      filename

    optional arguments:
      -h, --help            show this help message and exit
      -i hostname, --imagehost hostname
                            Specify the image host. One of: immio
      -v, --verbose
      -V, --version         show program's version number and exit

But, what can I do with it?
---------------------------

> “Logic will get you from A to Z; imagination will get you everywhere.”
> 
> — Albert Einstein

It’s entirely up to you, but try the following:

    % import ~/Pictures/screenshot.jpg && imup ~/Pictures/screenshot.jpg | \
        xclip -selection clipboard

Then select what you want to make a screenshot of, wait a few seconds and paste 
your clipboard into a chat with a friend (Ctrl+v). Voilà.

Best served as shortcut.


I want another filehost!
------------------------

No worries, thought about that.

Due to imup’s modular nature it’s rather simple (if you know python):

1) Open `hosts/__init__.py` and add the line

    import <filehost name>

2) Create a file `<filehost name>.py` in `hosts`.

3) Create a class that extends `Imagehost` from `hosts/imagehost.py`.

4) If the API has a simble POST functionality, overwrite 
   `_handle_server_answer(self, answer)`.

5) If it’s slightly more complicated, overwrite more functions of `Imagehost`.

6) ???

7) PROFIT!

Look at `imagehost.py`, I documented everything (of which there isn’t much, 
really).

Have fun!
