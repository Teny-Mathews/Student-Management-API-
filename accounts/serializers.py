from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username','first_name','last_name','email','password','phone_no']


    def create(self,validate_data):
        u=User.objects.create_user(**validate_data)
        u.save()
        return u