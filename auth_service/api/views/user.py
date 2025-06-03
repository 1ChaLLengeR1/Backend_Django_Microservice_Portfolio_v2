from rest_framework.decorators import api_view
from rest_framework.response import Response
from auth_service.api.consumer.handler.user import fetch_user_data


@api_view(['GET'])
def get_user_view(request):
    user_id = request.GET.get('user_id')
    task = fetch_user_data(user_id)
    return Response({
        'task_value': task,
        'status': 'Task created'
    })
