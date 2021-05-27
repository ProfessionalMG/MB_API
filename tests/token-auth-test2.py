import requests


def client():
    token_h = 'Token 905c1f1e5cc0decbb61def6ff5611de867565cb9'
    headers = {'Authorization': token_h}
    response = requests.get('http://127.0.0.1:8000/api/profiles/', headers=headers)
    print(f'Status Code: {response.status_code}')

    response_data = response.json()
    print(response_data)


if __name__ == '__main__':
    client()
