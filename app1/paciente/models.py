from django.db import models


# Create your models here.
class PersonalMed(models.Model):
    apellido = models.CharField(max_length=255)
    nombre = models.CharField(max_length=255)
    especialidad = models.CharField(max_length=255)
    predeterminada = models.BooleanField(default=True)

    def __str__(self):
        return f'id:{self.id}, nombre: {self.apellido} {self.nombre}, especialidad:{self.especialidad}'

class Antecedentes(models.Model):
    ant_personal = models.CharField(max_length=200)
    ant_genetico = models.CharField(max_length=200)
    predeterminado = models.BooleanField(default=True)

    def __str__(self):
        return f'id:{self.id},ant_personal:{self.ant_personal}, ant_genetico:{self.ant_genetico}'


class Paciente(models.Model):
    apellidos = models.CharField(max_length=255)
    nombres = models.CharField(max_length=255)
    cedula = models.CharField(max_length=10)
    sexo = models.CharField(max_length=20)
    fecha_nac = models.DateField(default=True)
    est_civil = models.CharField(max_length=30)
    correo = models.CharField(max_length=255)
    num_telef = models.CharField(max_length=10)
    tipo_sangre = models.CharField(max_length=4)
    antecedentes = models.ForeignKey(Antecedentes, on_delete=models.SET_NULL, null=True)
    personal_med = models.ForeignKey(PersonalMed, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'id:{self.id}, nombre: {self.apellidos} {self.nombres}'