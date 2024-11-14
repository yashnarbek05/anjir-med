from django.db import models


class Examination(models.Model):
    doctor = models.ForeignKey('users.Doctor', on_delete=models.SET_NULL, null=True)
    patient = models.ForeignKey('users.Patient', on_delete=models.CASCADE)
    diagnosis = models.TextField(null=True, blank=True)
    analysis = models.FileField(upload_to='analysis/')
    visible = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.doctor} | {self.patient}"