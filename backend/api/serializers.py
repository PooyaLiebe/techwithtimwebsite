from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Note


### Object Relational Mapping (ORM) =>  Map Python Object To the Cors Responding Code for Database Making Change


class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User # Create User input Model
    fields = ["id","username","password"] # SQL Database Table
    extra_kwargs = {"password": {"write_only": True}} # Tell Django We want to accept the password when we create user 
    #but we do not want to return password when we giving information about User
    
  def create(self, validated_data):
    user = User.objects.create_user(**validated_data)
    return user
  
  
class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id','title','content','created_at','author']
        extra_kwargs = {'author':{'read_only': True}}