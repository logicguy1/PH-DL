LICNECE = """
Copyright © 2021 Drillenissen#4268 - logicguy.mailandcontact@gmail.com
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

__version__ = "1.0"
__author__  = "Drillenissen#4268"

import modules.utilities as utilities

import os
import shutil
import random

def shuffle(): # Shuffle all the files in the folder by adding 4 random numbers infront of the file name
    utilities.display_categories()
    category = input(' [?] Category: ')
    print("") # Add newline

    path = os.walk(f"Videos/{category}") # Get all the files in the folder
    for root, dirs, files in path:
        for i in files:
            shutil.move( # Rename the file
                f"Videos/{category}/{i}",
                f"Videos/{category}/{random.randint(1000, 9999)} # {i}"
            )
            print(f" [+] Videos/{category}/{random.randint(1000, 9999)} # {i}") # Print the result for debugging and updating the user on whats going on

def unshuffle(): # Used to unshuffle the whole list, will preserve file names of those who does not have the numbers in thir name
    utilities.display_categories()
    category = input(' [?] Category: ')
    print("")

    path = os.walk(f"Videos/{category}") # Get all the files in the path
    for root, dirs, files in path:
        for i in files:
            if "#" in i[:7]: # Check if the # is within the first 6 chareters of the filename
                shutil.move( # Rename the file
                    f"Videos/{category}/{i}",
                    f"Videos/{category}/{i[6:].strip()}"
                )
                print(f" [+] Videos/{category}/{i[7:]}")

def main():
    utilities.clear()

    print(" [1] Shuffle    [2] Unshuffle \n")

    inp = input(">>> ")

    if inp == "1":
        shuffle()
    elif inp == "2":
        unshuffle()
    else:
        print(" [!] Invalid option")
