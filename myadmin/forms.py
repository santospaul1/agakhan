from django import forms
from .models import LeaveType, Employee, Department


class EmployeeForm(forms.Form):
    empcode = forms.CharField(max_length=50)
    firstName = forms.CharField(max_length=100)
    lastName = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    gender = forms.ChoiceField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])
    dob = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    department = forms.ModelChoiceField(queryset=Department.objects.all())
    address = forms.CharField(max_length=255)
    city = forms.CharField(max_length=100)
    country = forms.CharField(max_length=100)
    mobileno = forms.CharField(max_length=10)



class LeaveTypeForm(forms.ModelForm):
    class Meta:
        model = LeaveType
        fields = ['LeaveType', 'Description']

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['department_name', 'department_shortname', 'department_code']
class EmployeeUpdateForm(forms.ModelForm):

  class Meta:
    model = Employee
    fields = ['firstName', 'lastName', 'gender', 'mobileno',
              'address', 'city', 'country', 'department']