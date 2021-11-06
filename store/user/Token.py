from django.core.signing import TimestampSigner, SignatureExpired
from datetime import timedelta

class TokenCreator():

    def __init__(self):
        self.signer = TimestampSigner()
        self.TokenLifeTime = timedelta(minutes=15)
        

    def CreateActivationLink(self, email, FirstName, LastName, password):

        ActivationToken = {

            'main': {'email': email, 'password': password}, 
            'Name': {'FirstName': FirstName, 'LastName':LastName}
            
            }

        ActivationToken = self.signer.sign_object(ActivationToken)

        return ActivationToken


    def CreateForReSendPage(self, email, FirstName, LastName, password):

        link = {'EmailSend': email, 'FirstNameSend': FirstName, 'LastNameSend': LastName, 'PasswordSend': password}

        link = self.signer.sign_object(link)

        return link


    def UnsignToken(self, token):
        try:
            Object = self.signer.unsign_object(token, max_age = self.TokenLifeTime)
            return Object
        except SignatureExpired:
            return False