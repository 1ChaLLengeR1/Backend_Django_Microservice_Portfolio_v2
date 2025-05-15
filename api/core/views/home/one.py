from worker.consumer.service.application.home.one import one_application_home_service
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def view_one_home(request):
    user_id = request.GET.get('user_id')
    return Response({
        'result': one_application_home_service('pl')
    })
