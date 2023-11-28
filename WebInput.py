import requests

url = ''
data = {
    'username': 'your_username',
    'password': 'your_password',
    'other_field': 'other_value'
}

response = requests.post(url, data=data)

print(response.text)
