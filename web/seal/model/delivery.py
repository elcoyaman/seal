from django.db import models
from seal.model import Student, Practice
from seal.utils import managepath
from seal.model.teacher import Teacher

class Delivery(models.Model):
    """Delivery class.
    
    It is the object or artifact that the Student presents as his work for a
    given assignment. In this case it is considered required to be a zip 
    package.
     
    """
    file = models.FileField(upload_to=managepath.get_instance().get_delivery_path())
    student = models.ForeignKey(Student)
    practice = models.ForeignKey(Practice)
    deliverDate = models.DateField()
    deliverTime = models.TimeField(auto_now=True)
    corrector = models.ForeignKey(Teacher, null=True, blank=True)
    
    def __str__(self):
        """Stringify the Delivery"""
        return (str(self.practice) + " - " + str(self.student) + " - " + str(self.deliverDate))
    
    def get_correction(self):
        if self.correction_set.exists():
            return self.correction_set.all()[0]
        else:
            return None
    
    def get_automatic_correction(self):
        if(self.automaticcorrection_set.all().exists()):
            return self.automaticcorrection_set.all()[0]
        else:
            return None
    
    class Meta:
        ordering = ('-deliverDate', '-deliverTime')
