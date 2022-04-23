from __future__ import print_function
import requests
proxies = {
  'http': 'http://127.0.0.1:10800',
  'https': 'http://127.0.0.1:10800',
}
parameters = {'q' : 'Python', 'client' : 'Firefox'}
# 国内访问需要代理
response = requests.get('http://www.google.com/search', params=parameters ,proxies=proxies)
print('actual URL:', response.url)
