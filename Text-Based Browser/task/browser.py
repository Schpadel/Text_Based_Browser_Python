import os
import argparse
import sys
from collections import deque
import requests
from bs4 import BeautifulSoup
from colorama import Fore

# write your code here
parser = argparse.ArgumentParser(description="This program is a simple text based web browser!")

parser.add_argument("directory")

args = parser.parse_args()
print(args.directory)  # works
path = os.path.join(os.getcwd(), args.directory)
print(path)
if not os.access(args.directory, os.F_OK):
    os.mkdir(path)

history_stack = deque()


url = ""

while url != "exit":
    url_old = url
    url = input("Please enter the requested URL: ")

    if url == "exit":
        sys.exit()

    if "https://" not in url:
        url = "https://" + url

    if "." not in url:
        print("Incorrect URL")

    if url == "back":
        url = history_stack.pop()

    if url_old != "":
        history_stack.append(url_old)

    try:
        request = requests.get(url)
    except Exception:
        print("Incorrect URL")
    else:
        if request.ok:
            soup = BeautifulSoup(request.content, "html.parser")
            text = soup.findAll()

            for tag in text:
                if tag.name == "a":
                    print(Fore.BLUE + tag.text.strip())
                else:
                    print(Fore.WHITE + tag.text.strip())

            path_site = os.path.join(path, url.replace(".", "").replace("https://", "").replace("com", "").replace("/", ""))
            with open(path_site, "w") as site_file:
                site_file.write(soup.text)
        elif url == "back":
            print()
        else:
            print("Error no valid website found or Request denied!")

