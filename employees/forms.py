from django import forms

from employees.models import Department


class AddEmployeesForm(forms.Form):
    name = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Enter your name here',
                                                                        'class':'form-control col-lg-4'}))
    email = forms.EmailField(required=True, label='E-mail', widget=forms.TextInput(attrs={'placeholder': 'Enter your e-mail here',
                                                                                          'class': 'form-control col-lg-4'}))
    department = forms.ModelChoiceField(queryset = Department.objects.filter())

class ExcludeEmployeeForm(forms.Form):
    email = forms.CharField(required=True,  label='E-mail', widget=forms.TextInput(attrs={'placeholder': 'Enter employee e-mail here',
                                                                        'class': 'form-control col-lg-4'}))

class AddDepartment(forms.Form):
    department = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Enter department name here',
                                                                        'class': 'form-control col-lg-4'}))