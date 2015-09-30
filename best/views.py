from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from models import *
from serializers import *

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

"""
Return all students for a particular group
"""
def group_detail(request, pk):
    if request.method != 'GET':
        return HttpResponse(status=404)

    try:
        group = Group.objects.get(pk=pk)
    except Group.DoesNotExist:
        return HttpResponse(status=404)
        
    group_serializer = GroupSerializer(group)
    data = group_serializer.data

    return JSONResponse(data)

