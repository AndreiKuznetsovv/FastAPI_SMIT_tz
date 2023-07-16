import requests

API_URI = 'http://localhost:8080/calculate'


def test_request(cargo_type: str, date: str, declared_cost: float):
    test_request1 = requests.get(f'{API_URI}',
                                 headers={'cargo_type': cargo_type, 'date': date, 'declared_cost': declared_cost})

    return f'{test_request1.status_code}\n{test_request1.text}'


print(test_request(cargo_type='Glass', date='2020-06-01'))
