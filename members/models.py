from django.db import models

# Create your models here.
from django.db import models


# Create your models here.
class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.IntegerField(null=True)
    joined_date = models.DateField(null=True)

    # 在admin的Members数据列表中用此处设定的数据替换: Member object(1..n)
    def __str__(self):
        return f"{self.firstname} {self.lastname}"
