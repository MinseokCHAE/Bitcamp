from django.shortcuts import render
from django.urls import path
from django.http import HttpResponse, JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Member
from .serializers import MemberSerializer


class Members_post(APIView):
    def post(self, request):
        data = request.data['body']
        serializer = MemberSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'result': f'WELCOME, {serializer.data.get("name")}'}, status=201)
        return Response(serializer.errors, status=400)


class Members_get(APIView):
    def get(self, request):
        pass


class Members_login(APIView):
    def post(self, request):
        data = request.data['body']
        pk = data['userid']
        user_input_password = data['password']
        member = self.get_object(pk)
        if user_input_password == member.password:
            return Response({'result': 'Login Success'}, status=201)
        return HttpResponse(status=104)

    @staticmethod
    def get_object(pk):
        try:
            return Member.objects.get(pk=pk)
        except Member.DoesNotExist:
            raise Http404


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
