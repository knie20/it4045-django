__author__ = 'Andrew'
import requests

r1 = requests.get("http://localhost:8000/foo/")

print r1.status_code
print r1.text

r2 = requests.post("http://localhost:8000/foo/")
print r2.status_code
print r2.text


