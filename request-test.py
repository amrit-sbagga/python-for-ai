import requests

response = requests.get("https://api.github.com");
print(response.status_code) # print 200
# print(response.json()) # print json response
# print(response.content) # print content response
