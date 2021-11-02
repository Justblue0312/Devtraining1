from bs4 import BeautifulSoup
import requests

url = 'http://45.79.43.178/source_carts/wordpress/wp-login.php'

payload = {
    'log': 'admin',
    'pwd': '123456aA'
}


with requests.Session() as s:
    # post data to form
    p = s.post(url, data=payload)
    soup = BeautifulSoup(p.content, "html.parser")
    name = soup.find('span', class_='display-name')
    print(name.contents[0])
