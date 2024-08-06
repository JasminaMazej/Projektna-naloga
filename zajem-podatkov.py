import re
import requests

#nekaj poskusam

def html(url_link):
    """poišče html, podane spletne strani in ga vrne kot niz"""
    html = requests.get(url_link)
    return html.text

#poskus = html('https://www.bolha.com/avto-oglasi')
#print(poskus)

