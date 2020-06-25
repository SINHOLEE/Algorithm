from github_com.kennethreitz import requests

assert requests.get('https://github.com').status_code == 200
