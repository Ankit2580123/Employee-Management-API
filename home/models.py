from django.db import models

# Create your models here.

# class Department(models.Model):
#     department_name=models.CharField(max_length=50)

#     def __str__(self) -> str:
#         return self.department_name

# class Role(models.Model):
#     role_name=models.CharField(max_length=50)

#     def __str__(self) -> str:
#         return self.role_name
    
class Employee(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length = 254,unique=True)
    department=models.CharField(max_length=50,blank=True, null=True,)
    role=models.CharField(max_length=50,blank=True,null=True)
    # department=models.ForeignKey(Department, related_name='depart', blank=True, null=True, on_delete=models.CASCADE)
    # role=models.ForeignKey(Role, related_name='role', blank=True, null=True, on_delete=models.CASCADE)

    date_joined=models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = "Employee"
        ordering=['name']

        
