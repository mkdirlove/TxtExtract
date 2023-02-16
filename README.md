<h1 align="center">
  <br>
  <a href="https://github.com/mkdirlove/TxtExtract"><img src="https://github.com/mkdirlove/TxtExtract/blob/main/logo.png" alt="TxtExtract"></a>
  <br>
  Extract text from an image using OCR.
  <br>
</h1>

#### Installation

Copy-paste this into your terminal:

```
git clone https://github.com/mkdirlove/TxtExtract.git
```
```
cd TxtExtract
```
```
python3 TxtExtract.py -h
```

#### Usage
```
  ______     __  ______     __                  __ 
 /_  __/  __/ /_/ ____/  __/ /__________ ______/ /_
  / / | |/_/ __/ __/ | |/_/ __/ ___/ __ `/ ___/ __/
 / / _>  </ /_/ /____>  </ /_/ /  / /_/ / /__/ /_  
/_/ /_/|_|\__/_____/_/|_|\__/_/   \__,_/\___/\__/  


usage: TextExtractor.py [-h] [-f FILE] [-u URL]

TxtExtract - Extract text from an image using OCR

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  Path to the image file to extract text from
  -u URL, --url URL     URL of the image file to extract text from
```
#### Sample Usage #1

Extract text from image url

```
python3 TextExtractor.py -u https://qph.cf2.quoracdn.net/main-qimg-60dad75c0dddf8f4aa1a95040d7c3ca5-pjlq
```

#### Sample Usage #2

Extract text from image file

```
python3 TextExtractor.py -f /home/user/Pictures/image.png
```
