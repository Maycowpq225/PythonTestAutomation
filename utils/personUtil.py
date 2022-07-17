from features.services.OneSecmailService import OneSecmailService
from features.services.RandomUserService import RandomUserService
import random


class PersonUtil(object):
    def __init__(self):
        random_user = RandomUserService().getRandomUser()
        self.TITLE = random_user['name']['title']
        self.FIRST_NAME = random_user['name']['first']
        self.LAST_NAME = random_user['name']['last']
        self.EMAIL = random_user['email']
        self.PASSWORD = random.randint(10000000, 99999999)
        self.BIRTH_DATE = random_user['registered']['date']
        self.ADDRESS = random_user['location']['street']['name']
        self.CITY = random_user['location']['city']
        self.STATE = random_user['location']['state']
        self.ZIP_CODE = random.randint(10000, 99999)
        self.MOBILE_PHONE = random.randint(10000000, 99999999)
        self.SECOND_EMAIL = OneSecmailService().generateNewEmail()