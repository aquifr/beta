from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'^$',
        view=views.index,
        name='index',
    ),
    url(
        regex=r'^(?P<pk>[0-9]+)$',
        view=views.OfferingDetailView.as_view(),
        name='detail',
    ),
]

