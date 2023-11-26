from django.urls import path
from . import views

urlpatterns = [
	path('', views.apiOverview, name="api-overview"),
	path('todoList/', views.todoList, name="todo-list"),
	path('todoDetail/<str:pk>/', views.todoDetail, name="todo-detail"),
	path('todoCreate/', views.todoCreate, name="task-create"),

	path('todoUpdate/<str:pk>/', views.todoUpdate, name="todo-update"),
	path('todoDelete/<str:pk>/', views.todoDelete, name="todo-delete"),
]

##taskCreate/,taskList etc are the addresses we have to specify while fetching the information