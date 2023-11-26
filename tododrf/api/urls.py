from django.urls import path
from . import views
from . import classBasedViews

urlpatterns = [
	path('', views.apiOverview, name="api-overview"),
	path('todoList/', views.todoList, name="todo-list"),
	path('todoDetail/<str:pk>/', views.todoDetail, name="todo-detail"),
	path('todoCreate/', views.todoCreate, name="task-create"),

	path('todoUpdate/<str:pk>/', views.todoUpdate, name="todo-update"),
	path('todoDelete/<str:pk>/', views.todoDelete, name="todo-delete"),

	path('todoListView/', classBasedViews.TodoListView.as_view(), name="todo-list-class-based"),
	path('todoDetailView/<str:pk>/', classBasedViews.TodoDetailView.as_view(), name="todo-detail-class-based"),
	path('todoCreateView/', classBasedViews.TodoCreateView.as_view(), name="todo-create-class-based"),
	path('todoUpdateView/<str:pk>/', classBasedViews.TodoUpdateView.as_view(), name="todo-update-class-based"),
	path('todoDeleteView/<str:pk>/', classBasedViews.TodoDeleteView.as_view(), name="todo-delete-class-based"),
]

##taskCreate/,taskList etc are the addresses we have to specify while fetching the information