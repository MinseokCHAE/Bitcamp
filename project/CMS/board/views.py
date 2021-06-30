from django.shortcuts import render
from django.urls import path
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Board
from .serializers import BoardSerializer


class Boards_post(APIView):
    def post(self, request):
        data = request.data['body']
        serializer = BoardSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'result': f'Posting Success, {serializer.data.get("title")}'}, status=201)
        return Response(serializer.errors, status=400)


class Boards_get(APIView):
    def get(self, request):
        pass


@csrf_exempt
def board_list(request):
    if request.method == 'GET':
        board = Board.objects.all()
        serializer = BoardSerializer(board, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = BoardSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
