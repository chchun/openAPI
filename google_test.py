import requests

api_key = 'AIzaSyDkkOFihPG6JlmCToD8LxhjuZUcTrW-UAs'


def build_payload(query, target, source):
    """
    Builds a dictionary of parameters as payload
    for the HTTP request.
    """
    payload = {
        'q': query,
        'target': target,
        'key': api_key,
        'source': source
    }

    return payload

def handle_response(response):
        """
        Returns a Translation object.
        """
        if response.status_code in [400, 402, 404, 500]:
            exceptions(response)

        try:
            print(response.json())
            response = response.json()['data']['translations'][0]
            print(response)
        # when 'data' cannot be retrieved possibly due to a 403
        except KeyError:
            exceptions(response)

def exceptions(response):
        raise Exception(response.status_code, response.json()['error']['message'])

def main():
    query = 'Hello, world!'
    target = 'ko'
    source = 'en'

    url = 'https://www.googleapis.com/language/translate/v2?'

    try:
        payload = build_payload(query, target, source)
        print(payload)
        response = requests.get(url, params=payload)
        print(response)
        handle_response(response)

    except TypeError:
        return '[query] and [target] parameters are required.'


if __name__ == '__main__':
    main()
