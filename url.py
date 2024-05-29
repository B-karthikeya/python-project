import pyshorteners

def short_url(url):
    shortener = pyshorteners.Shortener()
    a = shortener.tinyurl.short(url)
    return a

print("enterurl")
url_data = input()

print(short_url(url_data))