import requests

response = requests.get('https://httpbin.org/ip')
print(format(response.json()))


print('Your IP is {0}'.format(response.json()['origin']))
print('Your IP is {0}'.format(response.json()['origin']))

'''
{'origin': '213.57.224.70'}
Your IP is 213.57.224.70

'''