from features.services.baseService import BaseService


class RandomUserService(BaseService):

    BASE_URI = 'https://randomuser.me/api/'

    def getRandomUser(self):
        return self.doGetRequest(self.BASE_URI).json()['results'][0]