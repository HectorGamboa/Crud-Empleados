from django import forms
from .models import prueba

class PruebaForm(forms.ModelForm):
    """Form definition for Prueba."""

    class Meta:
        """Meta definition for Pruebaform."""

        model = prueba
        fields = (
            'title',
            'subtitle',
            'cantidad')
        widgets = {
            "title" : forms.TextInput(
            attrs={
                'placeholder' : "Ingresa el titulo"
            }
            )
        }
    def clean_cantidad(self):
        cantidad = self.cleaned_data.get('cantidad')
        if cantidad<5:
            raise forms.ValidationError('Ingrese un numero mayor a 5')
        return cantidad
            #  # TODO Validation
        
            # return cantidad