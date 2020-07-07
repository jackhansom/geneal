from django.db import models


class Person(models.Model):
    first_name = models.CharField("first_name", max_length=120)
    middle_names = models.CharField("middle_names", null=True,
                                    max_length=120)
    last_name = models.CharField("last_name", null=True,
                                 max_length=120)
    born = models.DateField(null=False)
    died = models.DateField(null=True)
    father = models.ForeignKey('self', on_delete=models.SET_NULL,
                               null=True,
                               related_name='%(class)s_father')
    mother = models.ForeignKey('self', on_delete=models.SET_NULL,
                               null=True,
                               related_name='%(class)s_mother')

    def __str__(self):
        return f"{self.first_name} {self.middle_names} {self.last_name}"
