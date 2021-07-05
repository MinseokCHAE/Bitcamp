from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import api_view, parser_classes
from rest_framework import serializers
from rest_framework import status
from django.http.response import JsonResponse, HttpResponse, Http404
from .models import Member
from .serializers import MemberSerializer


@api_view(['GET', 'POST', 'DELETE'])
@parser_classes([JSONParser])
def members(request):
    if request.method == 'GET':
        all_members = Member.objects.all()
        serializer = MemberSerializer(all_members, many=True)
        return Response(data=serializer.data, status=201)
    elif request.method == 'POST':
        data = request.data['body']
        pk = data['userid']
        user_input_password = data['password']
        member = Member.objects.get(pk=pk)
        if member is not None:
            if user_input_password == member.password:
                return Response({'result': 'Login Success'}, status=201)
            else:
                return Response({'result': 'Incorrect Password'}, status=201)
        else:
            JsonResponse({'result': 'No Info'}, status=201)
        return HttpResponse(status=104)
    elif request.method == 'DELETE':
        serializer = MemberSerializer()
        return JsonResponse(serializer.data, safe=False)

@api_view(['GET', 'PUT', 'DELETE'])
def member(request, pk):
    if request.method == 'GET':
        serializer = MemberSerializer()
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'PUT':
        serializer = MemberSerializer()
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'DELETE':
        serializer = MemberSerializer()
        return JsonResponse(serializer.data, safe=False)
