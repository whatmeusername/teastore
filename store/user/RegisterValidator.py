from django.core.validators import EmailValidator, RegexValidator
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password


class Validator():
    """
    contains validators for checking password and email values.

    """

    def __init__(self):
        self.ResultDict = {}
        self.email_validator = EmailValidator(message= 'Ошибка в почте. Проверьте правильность почты ')
        self.regex_validator_password = RegexValidator(r'^[a-zA-Z0-9]*$', message = 'Пароль должен состоять из букв A-Z и цифр')
        self.regex_validator_firstname = RegexValidator(r'^[a-zA-Zа-яА-Я]*$', message = 'Имя может состоять только из русских и английских букв')
        self.regex_validator_lastname = RegexValidator(r'^[a-zA-Zа-яА-Я]*$', message = 'Фамилия может состоять только из русских и английских букв')

    def validate_email(self, email):

        try:
            self.email_validator(email)
            self.ResultDict['email'] = True
        except ValidationError as error:
            self.ResultDict['email'] = str(' '.join(error))

    def validate_password(self, password):

        try:
            validate_password(password = password, user = None)
            try:
                self.regex_validator_password(password)
                self.ResultDict['password'] = True
            except ValidationError as error:
                self.ResultDict['password'] = str(' '.join(error))

        except ValidationError as error:
            self.ResultDict['password'] = str(' '.join(error))

    def validate_similarity(self, password, password_repeat):

        if password == password_repeat:
            self.ResultDict['password_repeat'] = True
        else:
            self.ResultDict['password_repeat'] = 'Повтор не сходится с паролем'


    def validate_name(self, FirstName, LastName):

        if FirstName != None:
            try:
                self.regex_validator_firstname(FirstName)
                self.ResultDict['FirstName'] = True
            except ValidationError as error:
                self.ResultDict['FirstName'] = str(' '.join(error))

        if LastName != None:
            try:
                self.regex_validator_lastname(LastName)
                self.ResultDict['LastName'] = True
            except ValidationError as error:
                self.ResultDict['LastName'] = str(' '.join(error))

        

    def get_result(self):
        return self.ResultDict

    


