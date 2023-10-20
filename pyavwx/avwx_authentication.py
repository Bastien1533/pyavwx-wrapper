from requests.auth import AuthBase


def format_auth_header(api_key):
    return {"Authorization": api_key}


class AvwxApiAuth(AuthBase):
    def __init__(self, api_key):
        self.api_key = api_key

    def __call__(self, request):
        request.headers.update(format_auth_header(self.api_key))
        return request
