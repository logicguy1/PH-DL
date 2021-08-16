LICNECE = """
Copyright © 2021 Drillenissen#4268 - logicguy.mailandcontact@gmail.com
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

__version__ = "1.0"
__author__  = "Drillenissen#4268"

import os

def clear(): # Used to clear the screen
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""
 ██████╗ ██╗  ██╗      ██████╗ ██╗
 ██╔══██╗██║  ██║      ██╔══██╗██║
 ██████╔╝███████║█████╗██║  ██║██║
 ██╔═══╝ ██╔══██║╚════╝██║  ██║██║
 ██║     ██║  ██║      ██████╔╝███████╗
 ╚═╝     ╚═╝  ╚═╝      ╚═════╝ ╚══════╝
""")

def display_categories(aditionalInfo = True): # Displays the categories
    if aditionalInfo: # Usefull in the categorie editor where we dont need to additional information it pastes to the console
        print("\n [+] Current categories:\n")

    categories = [f" [-] {x[0][7:]}" for x in os.walk("Videos/")][1:]
    print("\n".join(categories))

    if aditionalInfo:
        print("\n [+] Type any of the above (case insentensive) or a new category and it will be created for you")

def install(package): # Used to install packages
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
