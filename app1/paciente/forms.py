from django.forms import EmailInput, ModelForm

from paciente.models import Paciente

class PacienteFormulario(ModelForm):
    class Meta:
        model = Paciente
        fields = '__all__'
        widgets = {
            'correo': EmailInput(attrs={'type': 'email'})
        }
