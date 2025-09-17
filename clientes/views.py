from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Cliente
from .forms import ClienteForm

def home(request):
    from django.http import HttpResponse
    return HttpResponse("Hello, world!")

class ClienteList(ListView):
    model = Cliente
    template_name = 'clientes/list.html'
    context_object_name = 'clientes'
    paginate_by = 10
    ordering = ['cliente_id']

    # Búsqueda simple ?q=
    def get_queryset(self):
        qs = super().get_queryset().order_by(*self.ordering)
        q = self.request.GET.get('q')
        if q:
            qs = qs.filter(nombre__icontains=q) | qs.filter(email__icontains=q)
        return qs

class ClienteCreate(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'clientes/form.html'
    success_url = reverse_lazy('clientes:list')

    def form_valid(self, form):
        messages.success(self.request, "Cliente creado correctamente.")
        return super().form_valid(form)

class ClienteUpdate(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'clientes/form.html'
    success_url = reverse_lazy('clientes:list')

    def form_valid(self, form):
        messages.success(self.request, "Cliente actualizado correctamente.")
        return super().form_valid(form)

class ClienteDelete(DeleteView):
    model = Cliente
    template_name = 'clientes/confirm_delete.html'
    success_url = reverse_lazy('clientes:list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Cliente eliminado.")
        return super().delete(request, *args, **kwargs)
