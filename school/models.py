from random import choices
from django.db import models

# Create your models here.
class Examscore(models.Model):
    allsubject = (('ຄະນິດສາດ','ຄະນິດສາດ'),
                  ('ວິທະຍາສາດ','ວິທະຍາສາດ'),
                  ('ສິລະປະ','ສິລະປະ'),
                  ('ພາສາອັງກີດ','ພາສາອັງກີດ'),
                  ('ຟີຊີກ','ຟີຊີກ'),
                  ('ຊິວະ','ຊິວະ'),
    )
    
    subject = models.CharField(max_length=50, choices=allsubject, default='math')
    student_name = models.CharField(max_length=50)
    score = models.IntegerField(default=0)
    def __str__(self):
        return self.student_name +'= '+ self.subject +'= '+str(self.score)
    
    
    