import requests
import json
from time import time

def get_snippets(url, n=400):
    headers = {'User-agent': 'creative writing downloader'}
    params = {'limit': n}
    url = url + '.json'
    res = requests.get(url, headers=headers, params=params)
    data = json.loads(res.text)
    snippets = data[1]['data']['children']
    result = list()
    for snippet in snippets:
        try:
            result.append(snippet['data']['body'])
        except Exception as oops:
            a = oops
    return result



def get_posts():
    url = 'https://www.reddit.com/r/WritingPrompts/top/.json?t=month'
    headers = {'User-agent': 'creative writing downloader'}
    params = {'limit': 400}
    res = requests.get(url, headers=headers, params=params)
    if res.status_code == 200:
        return res.json()
    else:
        print('error', res.json())
        return None


posts = get_posts()
for post in posts['data']['children']:
    snippets = get_snippets('https://www.reddit.com' + post['data']['permalink'])
    print('!snippets:', len(snippets), 'link:', post['data']['permalink'])
    for snippet in snippets:
        if 'I am a bot' in snippet:
            continue
        if len(snippet) < 300:
            continue
        with open('Stories/story_%s.txt' % time(), 'w', encoding='utf-8') as outfile:
            outfile.write(snippet)

















