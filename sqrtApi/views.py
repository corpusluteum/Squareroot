from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from sqrtApi.tasks import squareRootProcess, takesRoot
from sqrtApi.models import SqrtNumber
from sqrtApi.serializers import PostSerializer
from sqrtApi.forms import SqrtRequestForm

def home(request):

    form = SqrtRequestForm()
    if request.method == "POST":
        form = SqrtRequestForm(request.POST)
        if form.is_valid():
            new = form.cleaned_data
            squareRootProcess.delay(new['number'])
    return render(
        request,
        'home.html',
        {
            'form': form,
        }
    )

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


