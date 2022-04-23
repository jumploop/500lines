from __future__ import print_function
import requests
parameters = {'q' : 'Python', 'client' : 'Firefox'}
response = requests.get('http://www.google.com/search', params=parameters)
print('actual URL:', response.url)
