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
Return all plans and students for a particular group
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

    course_id = group.section.course.id
    instructor_id = group.section.instructor.id
    plans = Plan.objects.filter(course_id=course_id).filter(instructor_id=instructor_id)
    plans_serializer = PlanSerializer(plans, many=True)
    data['plans'] = plans_serializer.data
    return JSONResponse(data)

