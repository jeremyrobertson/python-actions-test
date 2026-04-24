import requests


def verify_example_com():
    """Make a request to example.com and verify the response is 200."""
    response = requests.get('https://example.com')
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    return response


def handler(event, context):
    print('Hello World')
    verify_example_com()
    return event