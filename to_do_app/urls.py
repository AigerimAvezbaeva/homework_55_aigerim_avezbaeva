from django.urls import path
from to_do_app.views.base import to_do_view
from to_do_app.views.to_do_view import add_paragraph, paragraph_view, update_toDo, delete_toDo, tdp_confirm_delete

urlpatterns = [
    path('', to_do_view, name='index'),
    path('to_do_list/', to_do_view),
    path('to_do_list/add/', add_paragraph, name='add_paragraph'),
    path('to_do_list/<int:pk>', paragraph_view, name='paragraph_detail'),
    path('to_do_list/<str:pk>/update/', update_toDo, name='todo_update'),
    path('to_do_list/<int:pk>/delete/', delete_toDo, name='delete_par'),
    path('to_do_list/<int:pk>/confirm_delete/', tdp_confirm_delete, name='confirm_delete')
]
