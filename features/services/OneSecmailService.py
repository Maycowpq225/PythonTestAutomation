from features.services.baseService import BaseService


class OneSecmailService(BaseService):

    BASE_URI = 'https://www.1secmail.com/api/v1/'

    def generateNewEmail(self):
        payload = {'action': 'genRandomMailbox',
                   'count': '1'}
        return self.doGetRequestPayload(self.BASE_URI, payload).json()[0]
