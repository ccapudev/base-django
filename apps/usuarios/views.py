from django.shortcuts import render
from apps.usuarios.models import Publicacion


# Create your views here.
def home(request):
	p, c = Publicacion.objects.get_or_create(pk=1)
	return render(request, 'index.html', dict(
		publi=p
	))
