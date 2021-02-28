from django.urls import path
from . import views

urlpatterns = [
	path('', views.apiOverview, name="api-overview"),
	path('taskList/', views.taskList, name="task-list"),
	path('taskDetail/<str:pk>/', views.taskDetail, name="task-detail"),
	path('taskCreate/', views.taskCreate , name="task-create"),

	path('taskUpdate/<str:pk>/', views.taskUpdate, name="task-update"),
	path('taskDelete/<str:pk>/', views.taskDelete, name="task-delete"),
]

##taskCreate/,taskList etc are the addresses we have to specify while fetching the information