import requests

def status(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0'}
    try:
        if 'http' not in url:
            newURL = 'http://' + url
            status = requests.get(newURL, headers=headers)
        else:
            status = requests.get(url, headers=headers)

        return status.status_code
    except:
        
        return 'Could not make connection'

def appendPrefix(url):
    if 'http' not in url:
        newURL = 'http://' + url
        return newURL
    else:
        return url