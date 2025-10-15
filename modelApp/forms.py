from django import forms
from django.core import validators

from modelApp.models import Empleado

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['nombre', 'telefono', 'email']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),

        }

    nombre = forms.CharField(
        min_length=5,
        max_length=20,
        validators=[
            validators.MinLengthValidator(5),
            validators.MaxLengthValidator(20),
        ],
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )

    def clean_nombre(self):
        inputNombre = self.cleaned_data['nombre']
        if inputNombre == "Luis":
            raise forms.ValidationError("No se aceptan mas Luis")
        return inputNombre