from django.db import models


class Department(models.Model):
    #id is autogenerated
    name = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=300, null=False)
    location = models.CharField(max_length=50, null=True)
    pin_code = models.CharField(max_length=10, default="522613")
    date_created = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(null=True)


# class Employee(models.Model):
#     name = models.CharField(max_length=100, null=False)
#     dob = models.DateField(null=False)
#     salary = models.IntegerField(null=False)
#     address = models.CharField(max_length=200, null=False)
#     date_created = models.DateTimeField(auto_now=True)
#     date_updated = models.DateTimeField(null=True)
#     department = models.ForeignKey(Department, on_delete=models.CASCADE)










