from django.test import TestCase

class myData():
    
    def __init__(self,emails,first_name,last_name,sign_in_date,purchase_count,created=None):

        self.emails = emails
        self.first_name = first_name
        self.last_name = last_name
        self.sign_in_date = sign_in_date
        self.purchase_count = purchase_count