#!/usr/bin/env python
import requests
import yaml
from bs4 import BeautifulSoup

url = raw_input('Please enter a Jenkins job URL: ')

if !url.endswith('/'):
	url += '/'

print 'Retrieving build URLs...'

resp = requests.get(url + 'api/json?tree=allBuilds[url]')

builds = yaml.safe_load(resp.text)

# Only include successful builds
successful_builds = []

for build in builds['allBuilds']:
    resp = requests.get(build['url'] + 'api/json')
    if yaml.safe_load(resp.text)['result'] == 'SUCCESS':
        successful_builds.append(build['url'])
    
data = yaml.safe_load(resp.text)

for page in successful_builds:
    r = requests.get(page)
    soup = BeautifulSoup(r.content)
    if soup.find('table', {'class': 'fileList'}):
        links = soup.find('table', {'class': 'fileList'}).find_all('a')
    for link in links:
        if (link.get('href') != 'artifact/' and
            '/*fingerprint*/' not in link.get('href') and
            '/*view*/' not in link.get('href') and
            '.json' not in link.get('href')):
            print page + link.get('href')
