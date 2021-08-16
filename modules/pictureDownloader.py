LICNECE = """
Copyright © 2021 Drillenissen#4268 - logicguy.mailandcontact@gmail.com
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

__version__ = "1.0"
__author__  = "Drillenissen#4268"

import modules.utilities as utilities

from bs4 import BeautifulSoup
import requests
import shutil
import os

def main():
    utilities.clear()

    URL = input(" [?] Album or picture URL: ")
    print("")

    if "album" in URL:
        html = requests.get(URL).text
        soup = BeautifulSoup(html, 'html.parser')

        title = soup.title.text

        children = [f'https://www.pornhub.com{i.find("a")["href"]}' for i in soup.find("ul", "photosAlbumsListing").children if i != "\n"]

    else:
        children = [URL,]

    indx = 1
    for i in children:
        html = requests.get(i).text
        soup = BeautifulSoup(html, 'html.parser')

        try:
            img = soup.find("div", "centerImage").find("img")["src"]
        except TypeError:
            img = soup.find("div", "centerImage").find("video").find("source")["src"]
        title = soup.title.text
        album = soup.find("div", {"id" : "thumbSlider"}).find("h2").text[8:]#.find("ul")#.children[1]

        if not os.path.isdir(f"Pictures/{title}"):
            os.mkdir(f"Pictures/{title}")

        r = requests.get(img, stream = True)
        r.raw.decode_content = True

        with open(f"Pictures/{title}/{album} - {i.split('/')[-1]}.{img.split('.')[-1]}".replace("\\", ""),'wb') as f:
            shutil.copyfileobj(r.raw, f)

        print(f" [+] Downloaded 'Pictures/{title}/{album} - {i.split('/')[-1]}.{img.split('.')[-1]}', {indx}/{len(children)} - {indx / len(children) * 100:.2f}%   ", end = "\r")

        indx += 1

        print("")
