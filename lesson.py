import datetime

class lesson:

    def __init__(self):
        self.date = None   #DateTime
        self.length = None   #int
        self.online = None   #boolean
        self.studentName = None  #string
        self.subject = None  #string
        self.rate = None     #int
        self.pay = None      #double
        self.earned = None   #double
        self.mileage = None  #double
    
    def setDate(self,date):
        self.date = date
    
    def setLength(self,length):
        self.length = length

    def setOnline(self,online):
        self.online = online

    def setSubject(self,subject):
        self.subject = subject

    def setRate(self,rate):
        self.rate = rate
    
    def setEarned(self,earned):
        self.earned = earned
