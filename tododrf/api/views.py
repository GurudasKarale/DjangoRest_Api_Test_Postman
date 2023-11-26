from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer

from .models import Task
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'Function Based':[ {
		'List':'/todoList/',
		'Detail View':'/todoDetail/<str:pk>/',
		'Create':'/todoCreate/',
		'Update':'/todoUpdate/<str:pk>/',
		'Delete':'/todoDelete/<str:pk>/'}
		],
		'Class Based': [{
			'List': '/todoListView/',
			'Detail View': '/todoDetailView/<str:pk>/',
			'Create': '/todoCreateView/',
			'Update': '/todoUpdateView/<str:pk>/',
			'Delete': '/todoDeleteView/<str:pk>/'}
		]
		}

	return Response(api_urls)

@api_view(['GET'])
def todoList(request):
	tasks = Task.objects.all().order_by('-id')
	serializer = TaskSerializer(tasks, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def todoDetail(request, pk):
	tasks = Task.objects.get(id=pk)
	serializer = TaskSerializer(tasks, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def todoCreate(request):
	serializer = TaskSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['PATCH'])
def todoUpdate(request, pk):
	task = Task.objects.get(id=pk)
	serializer = TaskSerializer(instance=task, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def todoDelete(request, pk):
	task = Task.objects.get(id=pk)
	task.delete()

	return Response('Item succsesfully delete!')
