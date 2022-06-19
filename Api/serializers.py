from .models import  Teacher,Student,Quiz,Result,Assignment,Classes,Notifications,Contact
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'
        depth=2

class QuizSerializertwo(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'
        depth=2

class PostQuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'



class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classes
        fields = '__all__'
        depth=1

class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = '__all__'
        depth=2
        
class PostResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = '__all__'
        
class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = '__all__'
        depth=2


class PostAssignmentSerializertwo(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = '__all__'






class PostAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = '__all__'
        

        


# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password',)
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user
#login
class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Invalid Details.")
##user
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'

##Notification
class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Notifications
        fields='__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model=Contact
        fields='__all__'