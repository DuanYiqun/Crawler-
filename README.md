# crawler for taobao
taobao.py :  Simeple program to search key words and get product information from taobao.com

### dependency
```sh
python 3.5, selenium, pandas.
You should also install wevdriver for chrom/fox/xxx and assign the path of the driver to selenium
```
### usage:
```sh
python taobao.py
```
you can preset what kind of keywords of a product in .py file for crawler

# Simple script crawler to search similar images on google image enging. 

## Dependency:
    selenium
    urllib
    python 3.6
    chromewebdriver

## How to use it
    Change the file path to be downloaded to your file path
    filePath = "/Users/duanyiqun/Downloads/download.jpeg"
    Change path to chromedriver
    chromedriver = "/Users/duanyiqun/anaconda3/envs/crawler/chromedriver"
    Set output dir
    OUTPUT_DIR = '/Users/duanyiqun/Downloads/testfile.txt'
    python google_similar_tools.py
    
    because this uses selenium to imitate scroll of a mouse, so I think currently I didn't meet anti-crawler problem form google. 
