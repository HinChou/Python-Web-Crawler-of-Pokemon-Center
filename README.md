# Python-Web-Crawler-of-Pokemon-Center 
* forked from shawncxc/py_crawler


I do some modifications on crawler.py. Regardless the syntax between Python 2.x and Python 3.x, the main change are below:

1. Added a exception handling of URLError
2. Deleted some redundant rows, like simplifying the data fetching using urllib module.

For 2nd point, I am wondering why there are lot of codes pass the "http.client.HTTPResponse" object, which is the result of urllib.urlopen(), to .read(), before passing them to the BeautifulSoup(). I think it may be a kind of legacy from the very beginning BeautifulSoup() which is not as good as the BeautifulSoup() in BS4. Right now, BeautifulSoup() function can handle the http response object for the URL requested smoothly.

Another choice is using .read() for a plain text webpage with regular expression to obtain the useful data. This can be done without using BeautifulSoup().
