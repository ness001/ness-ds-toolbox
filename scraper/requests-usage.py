import requests
url = 'https://www.dow.com/en-us/pdp.acusol-497n.182480z.html'
response = requests.get(url)
response.text # return html