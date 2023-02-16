import os
import argparse
import requests

banner = """  ______     __  ______     __                  __ 
 /_  __/  __/ /_/ ____/  __/ /__________ ______/ /_
  / / | |/_/ __/ __/ | |/_/ __/ ___/ __ `/ ___/ __/
 / / _>  </ /_/ /____>  </ /_/ /  / /_/ / /__/ /_  
/_/ /_/|_|\__/_____/_/|_|\__/_/   \__,_/\___/\__/  

"""

os.system("clear")
print(banner)
parser = argparse.ArgumentParser(description='TxtExtract - Extract text from an image using OCR')
parser.add_argument('-f', '--file', type=str, help='Path to the image file to extract text from')
parser.add_argument('-u', '--url', type=str, help='URL of the image file to extract text from')
args = parser.parse_args()

if not (args.file or args.url):
    parser.print_help()
    exit()

url = "https://ocr-extract-text.p.rapidapi.com/ocr"

headers = {
    "X-RapidAPI-Key": "18140c0733msh4177590f10ca716p1ba0c8jsnd344b761be19",
    "X-RapidAPI-Host": "ocr-extract-text.p.rapidapi.com"
}

if args.url:
    # If the URL argument is provided, send a GET request with the URL as a parameter
    querystring = {"url": args.url}
    response = requests.get(url, headers=headers, params=querystring)
else:
    # If the file argument is provided, read the file and send it as a file in the request payload
    with open(args.file, 'rb') as f:
        payload = {'image': f}
        response = requests.post(url, headers=headers, files=payload)

# Parse the JSON response and print only the "text" field
response_json = response.json()
print(response_json["text"])
