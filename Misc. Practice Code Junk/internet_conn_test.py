'''
date: 18/7/19
@auhtor: me(Madhav Sharma)
Reason for making this? My internet isn't working and I recently read the book Automate the Boring Stuff with Python
It's simple  trust me...
'''

try:
    from urllib.error import URLError
    from urllib.request import urlopen
#python 2 urllib fallback
except ImportError:
    from urllib2 import URLError, urlopen 

def can_I_google_now():
    try:
        urlopen("http://www.google.com", timeout=2)
        print("WhoHoo!!! You have internet access...(unlike me when I wrote this code.)")
    except URLError as idkwhatError:
        print("F...\nYou Don't have Internet Access!\nBecause of %s" %idkwhatError.reason)
        
can_I_google_now()