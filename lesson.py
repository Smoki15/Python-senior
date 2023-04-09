import requests

try:
    html = requests.get('https://www.googleeeeeeeecom/search?q=coffee')
    print(html.status_code)
except Exception as error:
    print('This website is not exist :(')
    print(error)

try:
    value = 14/0
    print(value)
except Exception as error:
    print(error)