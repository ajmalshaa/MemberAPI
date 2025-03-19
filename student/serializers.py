from rest_framework import serializers
from .models import *

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

    # def validate(self,data):
    #     print(data['age'])
    #     if data['age']<18:
    #         raise serializers.ValidationError({"age":"age must be greater than 18"})

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterActivity
        fields = ['id','Type','Subject','Comment','DueDate']

    
class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model= MemberDetails
        
        fields=['MemberName','MemberEmail','MemberID']

class MemberDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model= MemberDetails
        fields='__all__'

class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model= Loan
        fields='__all__'

class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model= Offer
        fields='__all__'