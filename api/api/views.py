from worker.consumer.handler.user import fetch_user_data
from rest_framework.decorators import api_view
from rest_framework.response import Response


# @api_view(['GET'])
# def get_user_view(request):
#     user_id = request.GET.get('user_id')
#     task = fetch_user_data.delay(user_id)
#     return Response({
#         'task_id': task.id,
#         'status': 'Task created'
#     })

@api_view(['GET'])
def get_user_view(request):
    user_id = request.GET.get('user_id')
    task = fetch_user_data(user_id)
    return Response({
        'task_value': task,
        'status': 'Task created'
    })
