import requests

with open('test_image.png', 'rb') as file:
    files = {'image': file}
    response = requests.post('http://127.0.0.1:8080/upload', files=files)
print(response.json())

response = requests.get('http://127.0.0.1:8080/image/test_image.png', headers={'Content-Type': 'image'})
print(response.status_code)

response = requests.delete('http://127.0.0.1:8080/delete/test_image.png', headers={'Content-Type': 'image'})
print(response.status_code)

response = requests.get('http://127.0.0.1:8080/image/test_image.png', headers={'Content-Type': 'image'})
print(response.status_code)