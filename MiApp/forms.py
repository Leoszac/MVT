from django import forms

    
class escuelaForm(forms.Form):
    taller = forms.CharField(max_length = 100)
    
class profesorForm(forms.Form):
    taller = forms.CharField(max_length = 100)
    nombre = forms.CharField(max_length = 100)
    DNI = forms.IntegerField()


class alumnoForm(forms.Form):
    taller = forms.CharField(max_length = 100)
    nombre = forms.CharField(max_length = 100)
    DNI = forms.IntegerField()
    