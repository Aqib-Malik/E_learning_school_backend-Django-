from functools import partial
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http import Http404, JsonResponse
from django.db import IntegrityError
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .models import Teacher,Student,Classes,Assignment
from .serializers import *
from rest_framework import generics, permissions
from rest_framework import viewsets,status
from rest_framework.decorators import api_view
# Create your views here.
from rest_framework.response import Response
from knox.models import AuthToken
from rest_framework.filters import SearchFilter
from rest_framework.views import APIView

class TeacherViewset(viewsets.ModelViewSet):
    queryset=Teacher.objects.all()
    serializer_class=TeacherSerializer 


class QuizViewset(viewsets.ModelViewSet):
    queryset=Quiz.objects.all()
    serializer_class=QuizSerializer 
    filter_backends=[SearchFilter]
    search_fields = ['classs__class_name']
    

class PostQuizViewset(viewsets.ModelViewSet):
    queryset=Quiz.objects.all()
    serializer_class=PostQuizSerializer 
    filter_backends=[SearchFilter]
    search_fields = ['classs__class_name']



@api_view(['GET', 'PUT', 'DELETE'])
def up_quiz(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        quiz = Quiz.objects.get(pk=pk)
    except quiz.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PostQuizSerializer(quiz)
        return Response(serializer.data)

    elif request.method == 'PUT':
        
        serializer = PostAssignmentSerializertwo(quiz, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        quiz.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AssignmentViewset(viewsets.ModelViewSet):
    queryset=Assignment.objects.all()
    serializer_class=AssignmentSerializer 
    filter_backends=[SearchFilter]
    search_fields = ['classs__class_name']



class PostAssignmentViewsetTwo(viewsets.ModelViewSet):
    queryset=Assignment.objects.all()
    serializer_class=PostAssignmentSerializertwo
    filter_backends=[SearchFilter]
    search_fields = ['classs__class_name']




@api_view(['GET', 'PUT', 'DELETE'])
def up_assign(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        assign = Assignment.objects.get(pk=pk)
    except assign.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PostAssignmentSerializertwo(assign)
        return Response(serializer.data)

    elif request.method == 'PUT':
        
        serializer = PostAssignmentSerializertwo(assign, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        assign.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class PostAssignmentViewset(viewsets.ModelViewSet):
    queryset=Assignment.objects.all()
    serializer_class=PostAssignmentSerializer 
    filter_backends=[SearchFilter]
    search_fields = ['classs__class_name']


class StudentViewset(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer 

class SearchClassStudentsViewset(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    filter_backends=[SearchFilter]
    search_fields = ['classs__class_name'] 


class ClassViewset(viewsets.ModelViewSet):
    queryset=Classes.objects.all()
    serializer_class=ClassSerializer
    filter_backends=[SearchFilter]
    search_fields = ['class_name']


class ResultViewset(viewsets.ModelViewSet):
    queryset=Result.objects.all()
    serializer_class=ResultSerializer 
    filter_backends=[SearchFilter]
    search_fields = ['student_id__user__id']

class PostResultViewset(viewsets.ModelViewSet):
    queryset=Result.objects.all()
    serializer_class=PostResultSerializer 
    filter_backends=[SearchFilter]
    search_fields = ['student_id__user__id']


class NotificationViewset(viewsets.ModelViewSet):
    queryset=Notifications.objects.all()
    serializer_class=NotificationSerializer 

class ContactViewsetTwo(viewsets.ModelViewSet):
    queryset=Contact.objects.all()
    serializer_class=ContactSerializer
    filter_backends=[SearchFilter]
    search_fields = ['Name']


################knox
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        print(request.data)
        dat={
            'username':request.data['username'],
            
            'email':request.data['email'],
            'password':request.data['password'],
            # 'is_active':True,
            
        }
        serializer = self.get_serializer(data=dat)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
   
        #print(us)
        user = User.objects.get(username=request.data['username'])
        user.is_active = False
        user.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })


class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        print("((((((((((()))))))))))))))")
        print(UserSerializer(user, context=self.get_serializer_context()).data['id'])
        student = Student.objects.get(user=UserSerializer(user, context=self.get_serializer_context()).data['id'])
        print("<<<<<<<<<<<<<",student)
        print(student.id)
        print(student.classs.class_name)
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1],
            "class":student.classs.class_name
        })


class TeacherLoginAPI(generics.GenericAPIView):
    serializer_class = LoginUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        print("((((((((((()))))))))))))))")
        print(UserSerializer(user, context=self.get_serializer_context()).data['id'])
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1],
        })




    




