import requests

def status(url):

    try:
        if 'http' not in url:
            newURL = 'http://' + url
            status = requests.get(newURL)
        else:
            status = requests.get(url)
        return status.status_code
    except:
        return 'Could not make connection'
