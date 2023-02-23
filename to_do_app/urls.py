from django.urls import path
from to_do_app.views.base import to_do_view
from to_do_app.views.delete_paragraph import delete_paragraph
from to_do_app.views.add_paragraph import add_paragraph
from to_do_app.views.add_paragraph import paragraph_view

urlpatterns = [
    path('', to_do_view, name='index'),
    path('to_do_list/', to_do_view),
    path('to_do_list/add/', add_paragraph, name='add_paragraph'),
    path('to_do_list/<int:pk>', paragraph_view, name='paragraph_detail'),
    path('to_do_list/delete/<int:pk>', delete_paragraph, name='delete_par')
]
