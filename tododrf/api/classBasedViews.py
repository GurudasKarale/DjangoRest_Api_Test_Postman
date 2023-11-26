from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import TaskSerializer
from .models import Task

class TodoListView(APIView):
    def get(self,request):
        tasks = Task.objects.all().order_by('-id')
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

class TodoCreateView(APIView):
    def post(self,request):

        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)

class TodoDetailView(APIView):
    def get(self,request,pk):
        tasks = Task.objects.get(id=pk)
        serializer = TaskSerializer(tasks,many=False)
        return Response(serializer.data)

class TodoUpdateView(APIView):
    def patch(self,request,pk):
        task = Task.objects.get(id=pk)
        serializer = TaskSerializer(instance=task, data=request.data)

        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)

class TodoDeleteView(APIView):
    def delete(self,request,pk):
        task = Task.objects.get(id=pk)
        task.delete()

        return Response('Item succsesfully delete!')