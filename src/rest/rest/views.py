from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from pymongo import MongoClient
from django.http import HttpResponse
from django.views import View
import os

# Initialize MongoDB connection
mongo_host = os.getenv('MONGO_HOST', 'localhost')
mongo_port = os.getenv('MONGO_PORT', '27017')
mongo_uri = f"mongodb://{mongo_host}:{mongo_port}"
client = MongoClient(mongo_uri)
db = client['test_db']
todos_collection = db.todos

class TodoListView(APIView):
    def get(self, request):
        try:
            todos = list(todos_collection.find({}, {'_id': 0}))
            return Response(todos, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def post(self, request):
        try:
            data = request.data
            todos_collection.insert_one(data)
            return Response({"message": "Todo added successfully"}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class WelcomeView(View):
    def get(self, request):
        return HttpResponse("Welcome to the Django API")
