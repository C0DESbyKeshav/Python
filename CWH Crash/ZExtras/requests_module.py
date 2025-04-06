# The requests module in Python is used to make HTTP requests, which means it allows your Python program to communicate with websites and web services over the internet.

# What is an HTTP request?
# When you visit a website, your browser sends a request to the website's server, asking for a page. The server then responds with the webpage's content. This process follows the HTTP (HyperText Transfer Protocol). The requests module allows Python to do the same thing programmatically.

# Why use requests?
# To fetch data from a website (like downloading a webpage or API data).
# To send data to a website (like submitting a form or logging in).
# To interact with web services (like getting weather data, stock prices, etc.).

# Common Types of Requests
# 1. GET Request – Used to request data from a website.
# 2. POST Request – Used to send data to a website.
# 3. PUT Request – Used to update existing data.
# 4. DELETE Request – Used to delete data.

# for more info use chatgpt 
# do not stop learning.....

import requests 
from bs4 import BeautifulSoup
url = "https://codesbykeshav.blogspot.com/"
r = requests.get(url)
# print(r.text)

soup = BeautifulSoup(r.text, 'html.parser')
print(soup.prettify())
for heading in soup.find_all("h2"):
    print(heading.text)
    
# url = "https://jsonplaceholder.typicode.com/posts"
# data = {
#     "title": 'Keshav',
#     "body": 'Mandal',
#     "userId": 12,
#   }
# headers =  {
#     'Content-type': 'application/json; charset=UTF-8',
#   }
# response = requests.post(url, headers=headers, json=data)
# print(response.text)
