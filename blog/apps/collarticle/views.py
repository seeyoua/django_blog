from  rest_framework.views import APIView
from  rest_framework import status
from celery_task.count.tasks import add_together
from rest_framework.response import Response

# Create your views here.

class CountView(APIView):

    def get(self,request):
        result= add_together.delay(1, 2)
        print(result)
        return Response({"message":"ok","status":status.HTTP_200_OK})








