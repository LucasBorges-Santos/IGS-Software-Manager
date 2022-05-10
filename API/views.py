from employees.models import *
from django.http import JsonResponse
from django.core.serializers import serialize
import json

def get_employees(request):
    if 'id' in request.GET.keys():
        employee_queryset = Employee.objects.filter(id=request.GET['id'])
    else:
        employee_queryset = Employee.objects.all()

    serialized_employees = serialize('json', list(employee_queryset), fields=('name', 'email','department', 'id'))
    
    return JsonResponse(
        json.loads(serialized_employees), 
        status=202, 
        safe=False
    )


def create_employee(request):
    try:
        new_employee = Employee()
        new_employee.dict_to_obj(request.GET)
        new_employee.clean_fields()
        new_employee.save()

        new_employee_serialize = serialize('json', list(Employee.objects.filter(id=new_employee.id)), fields=('name', 'email','department', 'id'))

        print(new_employee_serialize)
        return JsonResponse(
            json.loads(new_employee_serialize), 
            status=200,
            safe=False
        )

    except Exception as e:
        return JsonResponse(
            {'error': str(e)}, 
            status= 400
        )  

def delete_employee(request):
    employee_queryset = Employee.objects.filter(id=request.GET['id'])
    
    if employee_queryset.count() > 0:
        employee_queryset.delete()
        return JsonResponse(
            {'id': request.GET['id']}, 
            status= 200
        )
    else:
        return JsonResponse(
            {'id': False}, 
            status= 200
        )