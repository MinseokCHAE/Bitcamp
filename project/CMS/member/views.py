from django.shortcuts import render
from django.urls import path
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Member
from .serializers import MemberSerializer


class Auth(APIView):
    def get(self, request):
        serializer = MemberSerializer(data=request)
        if serializer.is_valid():
            serializer.save()
        return Response({'result': 'WELCOME'})


@csrf_exempt
def member_list(request):
    if request.method == 'GET':
        member = Member.objects.all()
        serializer = MemberSerializer(member, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MemberSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
