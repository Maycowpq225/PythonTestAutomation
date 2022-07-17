from features.services.OneSecmailService import OneSecmailService
from features.services.RandomUserService import RandomUserService


class PersonUtil(object):
    def __init__(self):
        random_user = RandomUserService().getRandomUser()
        self.TITLE = random_user['name']['title']
        self.FIRST_NAME = random_user['name']['first']
        self.LAST_NAME = random_user['name']['last']
        self.EMAIL = random_user['email']
        self.PASSWORD = random_user['login']['password']
        self.BIRTH_DATE = random_user['registered']['date']
        self.ADDRESS = random_user['location']['street']['name']
        self.CITY = random_user['location']['city']
        self.STATE = random_user['location']['state']
        self.ZIP_CODE = random_user['location']['postcode']
        self.COUNTRY = random_user['location']['country']
        self.MOBILE_PHONE = random_user['cell']
        self.SECOND_EMAIL = OneSecmailService().generateNewEmail()