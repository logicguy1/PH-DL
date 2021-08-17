LICNECE = """
Copyright © 2021 Drillenissen#4268 - logicguy.mailandcontact@gmail.com
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

__version__ = "1.0"
__author__  = "Drillenissen#4268"

import modules.utilities as utilities
from contextlib import contextmanager
import sys, os
import youtube_dl
import time
from pynotifier import Notification
import os
import shutil

@contextmanager
def suppress_stdout():
    with open(os.devnull, "w") as devnull:
        old_stdout = sys.stdout
        sys.stdout = devnull
        try:  
            yield
        finally:
            sys.stdout = old_stdout

def main():
    utilities.clear()
    url = input(" [?] Video URL: ")

    print(" [+] Downloading stand by\n")

    with suppress_stdout():
        ydl = youtube_dl.YoutubeDL({'outtmpl': 'Video Downloads/%(uploader)s - %(title)s - %(id)s.%(ext)s'}) # If anyone knows how to mute the output of this send help :,)

    with ydl:
        result = ydl.extract_info(
            url,
            download = True
        )

    Notification(
    	title='Download Complete',
    	description='Finished downloading video',
    	duration=5,
    	urgency='normal'
    ).send()

    print(f"\n [!] Finished downloading '{result['title']}'")
    inp = input(" [?] Do you want to keep the video? (Y/n) ")

    if "y" in inp.lower() or inp == "":
        utilities.display_categories() # Show the avaliable categories to the user

        while True:
            category = input("\n [?] Category: ")

            if not os.path.exists(f"Videos/{category}"):
                inp = input(f" [?] Are you sure you want to create a new category named '{category}'? (Y/n) ")
                if "y" in inp.lower() or inp == "":
                    os.mkdir(f"Videos/{category}")
                    break

            else:
                break

        shutil.move(
            f"Video Downloads/{result['uploader']} - {result['title']} - {result['id']}.mp4",
            f"Videos/{category}/{result['uploader']} - {result['title']} - {result['id']}.mp4"
        )

    else:
        os.remove(f"Video Downloads/{result['uploader']} - {result['title']} - {result['id']}.mp4")


#https://www.pornhub.com/view_video.php?viewkey=ph5e80ec51bc6b5
