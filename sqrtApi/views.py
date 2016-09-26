from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from sqrtApi.tasks import squareRootProcess
from sqrtApi.models import SqrtNumber
from sqrtApi.serializers import PostSerializer
from sqrtApi.forms import SqrtRequestForm

def home(request):
    tmpl_vars = {'form': SqrtRequestForm()}
    (squareRootProcess.delay(tmpl_vars))
    return render(request, 'home.html', tmpl_vars)


@api_view(['GET'])
def post_collection(request):
    if request.method == 'GET':
        posts = SqrtNumber.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def post_element(request, pk):
    try:
        post = SqrtNumber.objects.get(pk=pk)
    except SqrtNumber.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)


