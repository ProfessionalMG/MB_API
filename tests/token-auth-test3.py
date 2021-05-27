import requests


def client():
    data = {
        'username': 'testman',
        'email': 'testman@testmail.co.za',
        'password1': 'gamagang123',
        'password2': 'gamagang123',
    }

    response = requests.post('http://127.0.0.1:8000/api/rest-auth/registration/', data=data)
    print(f'Status Code: {response.status_code}')

    response_data = response.json()
    print(response_data)


if __name__ == '__main__':
    client()
