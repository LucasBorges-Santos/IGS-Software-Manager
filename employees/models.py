from django.db import models
from django.db.models import CheckConstraint, Q


class Department(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    email = models.EmailField(unique=True, null=False, blank=False)
    department = models.ForeignKey(Department, null=False, blank=False, on_delete=models.CASCADE) 

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def dict_to_obj(self, obj_dict): 
        for key in obj_dict: 
            if self._meta.get_field(key).get_internal_type() == 'ForeignKey':
                setattr(self, key, classes[key.capitalize()].objects.filter(id=obj_dict[key]).first())
            else:
                setattr(self, key, obj_dict[key])

    def __str__(self):
        return self.name

    class Meta:
        constraints = [
            CheckConstraint(
                check=~Q(name=''), 
                name='name_not_empty'),
            CheckConstraint(
                check=~Q(email=''), 
                name='email_not_empty'),
            CheckConstraint(
                check=~Q(department=''), 
                name='department_not_empty'),
        ]


classes = {
    'Department': Department,
    'Employee': Employee,
}
