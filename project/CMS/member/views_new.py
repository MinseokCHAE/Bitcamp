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
        new_member = request.data['body']
        serializer = MemberSerializer(data=new_member)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'result': f'Welcome, {serializer.data.get("name")}'}, status=201)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        serializer = MemberSerializer()
        return JsonResponse(serializer.data, safe=False)


@api_view(['GET',  'DELETE'])
def member(request, pk):
    if request.method == 'GET':
        serializer = MemberSerializer()
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'DELETE':
        Member.objects.get(userid=pk).delete()
        return JsonResponse({'result': 'Remove Success'}, status=201)


@api_view(['PUT'])
def member_modify(request):
    data = request.data['body']
    update_member = data['user']
    pk = update_member['userid']
    member = Member.objects.get(pk=pk)
    user_change_password = update_member['password']
    serializer = MemberSerializer(member, data=data['user'], partial=True)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse({'result': f'Update Success , {serializer.data.get("name")}'}, status=201)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login(request):
    try:
        data = request.data['body']
        pk = data['userid']
        user_input_password = data['password']
        member = Member.objects.get(pk=pk)
        if user_input_password == member.password:
            serializer = MemberSerializer(member, many=False)
            return JsonResponse(data=serializer.data, safe=False)
        else:
            return JsonResponse({'result': 'PASSWORD-FAIL'}, status=201)
    except Member.DoesNotExist:
        return JsonResponse({'result': 'USERNAME-FAIL'}, status=201)
