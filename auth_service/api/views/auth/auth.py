from rest_framework.decorators import api_view
from rest_framework.response import Response
from auth_service.api.consumer.service.application.home.one import one_application_home_service


@api_view(['POST'])
def view_auth(request):
    user_id = request.GET.get('user_id')
    return Response({
        'result': one_application_home_service('pl')
    })
