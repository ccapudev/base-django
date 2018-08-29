from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from apps.usuarios.models import Publicacion
from datetime import datetime
from django.utils.timezone import utc
from django.utils import timezone


# Create your views here.
class HomeView(APIView):
	def get(self, request, format='json'):
		p, c = Publicacion.objects.get_or_create(pk=1)
		if request.GET.get("json"):
			return Response({
				"fecha": p.fecha,
				"fecha_modificacion": p.fecha_modificacion,
				"ahora": datetime.utcnow().replace(tzinfo=utc),
				"ahora_timezone": timezone.now(),
			})

		return render(request, 'index.html', dict(
			publi=p
		))
