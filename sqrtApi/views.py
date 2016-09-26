
from rest_framework.decorators import api_view
from sqrtApi.tasks import squareRootProcess
from sqrtApi.models import SqrtNumber
from sqrtApi.serializers import PostSerializer
from rest_framework.response import Response

@api_view(['GET'])
def get_result(request):
    if request.method == 'GET':
        posts = SqrtNumber.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

@api_view(['POST'])
def calculate(request):
    if request.method == "POST":
        squareRootProcess.delay(request.data)
    return Response(request.data)




