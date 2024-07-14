from django.urls import path
from public.views import publics, public_detail, public_form

urlpatterns = [
    path('publics/', publics, name='publics'),
    path('public/<int:public_id>',public_detail, name='public_detail'),
    path('public_form/', public_form, name='public_form'),

]