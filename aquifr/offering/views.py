from django.http import HttpResponse
from django.views.generic import DetailView

from .models import Offering

# Index view. Currently displays nothing of interest.
def index(request):
	return HttpResponse("This is the offerings index.")

# Detail view for a single offering. Eventually, this will
# be where investors view the details of a prospectus, reach
# to founders, and decide to invest.
class OfferingDetailView(DetailView):
    model = Offering

