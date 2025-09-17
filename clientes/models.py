from django.db import models

class Cliente(models.Model):
    cliente_id = models.AutoField(primary_key=True, db_column='cliente_id')
    nombre = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    telefono = models.CharField(max_length=30)

    class Meta:
        db_table = 'clientes'
        managed = False  # <-- descomenta si YA existe la tabla y no quieres migrarla

    def __str__(self):
        return f"{self.cliente_id} - {self.nombre}"
