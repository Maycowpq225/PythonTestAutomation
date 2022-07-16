import requests


class BaseService():

    def doGetRequest(self, url):
        return requests.get(url)

    def doGetRequestPayload(self, url, payload):
        return requests.get(url, params=payload)

    def doGetRequestHeaders(self, url, headers):
        return requests.get(url, headers=headers)

    def doGetRequestHeadersAndPayload(self, url, headers, payload):
        return requests.get(url, headers=headers, params=payload)

