from django.db import models
from seal.model.delivery import Delivery

class Autocheck(models.Model):
    """
    
    Autocheck objects are the entities which represents the automatic check that
    SEAL can run on the deliveries made by the Students.
    
    """
    
    STATUS_STRINGS = {-1:"failed", 0:"pending", 1:"successfull"}
    
    delivery = models.ForeignKey(Delivery)
    captured_stdout = models.CharField(max_length=10240)
    exit_value = models.IntegerField()
    status = models.IntegerField()
    
    def __str__(self):
        """Stringify the Autocheck"""
        return ("Autocheck | exit value: " + str(self.exit_value) + " - status: " + self.status)
    
    def get_status(self):
        """Returns a status raw value as a human readable value"""
        return Autocheck.STATUS_STRINGS[self.status]
