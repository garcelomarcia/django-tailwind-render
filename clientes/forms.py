# clientes/forms.py
from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ["nombre", "email", "telefono"]
        # (opcional) también puedes usar widgets aquí campo por campo

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        base = "block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-600 focus:ring-2 focus:ring-blue-600"
        for f in self.fields.values():
            f.widget.attrs.update({
                "class": base,
                "placeholder": f.label,
            })
