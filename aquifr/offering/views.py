from django.http import HttpResponse
from django.views.generic import DetailView

# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Offering
from .serializers import OfferingSerializer

from .models import Offering

# Index view. Currently displays nothing of interest.
def index(request):
	return HttpResponse("This is the offerings index.")

# Detail view for a single offering. Eventually, this will
# be where investors view the details of a prospectus, reach
# to founders, and decide to invest.
class OfferingDetailView(DetailView):
    model = Offering

    def get(self, request, pk):
        try:
            offering = Offering.objects.get(pk=pk)
        except Offering.DoesNotExist:
            return HttpResponse(status=404)

        serializer = OfferingSerializer(offering)
        return JsonResponse(serializer.data)
