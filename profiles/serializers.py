from rest_framework import serializers
from .models import *


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        #fields = '__all__'
        fields = ['username','first_name','email','store','profile_status','profile_photo','date_joined','last_login']