import requests


def client():
    # In development, add superuser credentials for username and password. DO NOT USE THIS TEST IN PRODUCTION !
    credentials = {'username': 'bawo', 'password': 'password1'}
    response = requests.post('http://127.0.0.1:8000/api/rest-auth/login/', data=credentials)
    print(f'Status Code: {response.status_code}')
    # Expected Response: Status Code: 200
    response_data = response.json()
    print(response_data)
    # Expected Response: {'key': '9928393ccede.....'}


if __name__ == '__main__':
    client()
