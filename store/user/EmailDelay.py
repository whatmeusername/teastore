from django.conf import settings
import datetime

class Delay():

    def __init__(self, request):
        self.session = request.session

        delay = self.session.get(settings.DELAY_SESSION_ID)

        if not delay:
            delay = self.session[settings.DELAY_SESSION_ID] = None
        self.delay = delay


    def SetDelay(self):
        time = (datetime.datetime.now()).timestamp()
        self.delay = time
        self.save()


    def TimeDiff(self):

        TimeNow = (datetime.datetime.now()).timestamp()
        TimeBefore = self.delay
        if TimeBefore == None:
            self.SetDelay
            return True
        else:
            result =  (int(TimeNow - TimeBefore))

            if result > 90:
                return True
            else: False

    def GetTimeDiff(self):

        TimeNow = (datetime.datetime.now()).timestamp()
        TimeBefore = self.delay

        result = int(TimeNow - TimeBefore)
        result = 60 - result 

        if result < 0:
            result = 0
            return result
        else:
            return result


    def save(self):
        self.session[settings.DELAY_SESSION_ID] = self.delay
        self.session.modified = True

