from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
from rest_framework.views import APIView
from django.utils import timezone
# Create your views here.
# @api_view(['GET'])
# def student(request):
#     std_data= Student.objects.all()
#     serializer=StudentSerializer(std_data, many=True)
#     return Response({'status': status.HTTP_200_OK,'data': serializer.data})

class StudentAPI(APIView):

    def get(self, request):
        std_data= Student.objects.all()
        serializer=StudentSerializer(std_data, many=True)
        return Response({'status': status.HTTP_200_OK,'data': serializer.data})
    
    def post(self, request):
        add_data=request.data 
        serializer=StudentSerializer(data=add_data)
        if not serializer.is_valid():
            return Response({'status': status.HTTP_400_BAD_REQUEST,'data':serializer.errors})
        serializer.save()
        return Response({'status': status.HTTP_200_OK,'message':'Saved successfully','data': serializer.data})
    
    def patch(self, request):
        try:
            
            student_id = request.data.get('id')
            if not student_id:
                
                return Response({'status': status.HTTP_400_BAD_REQUEST, 'message': 'ID is required to update the student.'})

            try:
                
                update_data = Student.objects.get(id=student_id)
            except Student.DoesNotExist:
                
                return Response({'status': status.HTTP_404_NOT_FOUND, 'message': 'Student not found.'})

            serializer = StudentSerializer(update_data, data=request.data, partial=True)
            if not serializer.is_valid():
                return Response({'status': status.HTTP_400_BAD_REQUEST, 'message': serializer.errors})
            
            serializer.save()
            return Response({'status': status.HTTP_200_OK, 'message': 'Updated successfully', 'data': serializer.data})
        
        except Student.DoesNotExist:
            
            return Response({'status': status.HTTP_404_NOT_FOUND, 'message': 'Student not found.'})
        except Exception as e:
            
            return Response({'status': status.HTTP_400_BAD_REQUEST, 'message': f'Something went wrong: {str(e)}'})
        

    def delete(self, request):
        try:
            del_item= Student.objects.get(id=request.data.get('id'))
            del_item.delete()
            return Response({'status': status.HTTP_200_OK, 'message': f'item deleted successfully'})
        except Exception as e:
            return Response({'status': status.HTTP_405_METHOD_NOT_ALLOWED,'message': e.message})


class LogAPI(APIView):

    def get(self, request):
        try:
            log_activity= MasterActivity.objects.filter(ActivityType='LogActivity') 
            
            serializer= ActivitySerializer(log_activity,many=True)
            return Response({'status': status.HTTP_200_OK,'data': serializer.data})
        except Exception as e:
            return Response({'status': status.HTTP_405_METHOD_NOT_ALLOWED,'message': e.message})
        

class TaskAPI(APIView):

    def get(self, request):
        try:
            today= timezone.now().date()
            tasks= MasterActivity.objects.filter(ActivityType='Task',DueDate__gte=today) 
            
            serializer= ActivitySerializer(tasks,many=True)
            return Response({'status': status.HTTP_200_OK,'data': serializer.data})
        except Exception as e:
            return Response({'status': status.HTTP_405_METHOD_NOT_ALLOWED,'message': e.message})

class OverdueTaskAPI(APIView):

    def get(self, request):
        
        
        try:
            today= timezone.now().date()
            tasks= MasterActivity.objects.filter(ActivityType='Task',DueDate__lte=today) 
            
            serializer= ActivitySerializer(tasks,many=True)
            return Response({'status': status.HTTP_200_OK,'data': serializer.data})
        except Exception as e:
            return Response({'status': status.HTTP_405_METHOD_NOT_ALLOWED,'message': str(e)})

class MembersAPI(APIView):

    def get(self, request):
        try:
            
            members= MemberDetails.objects.all()
            
            serializer= MemberSerializer(members,many=True)
            return Response({'status': status.HTTP_200_OK,'data': serializer.data})
        except Exception as e:
            return Response({'status': status.HTTP_405_METHOD_NOT_ALLOWED,'message': e.message})
        

class MemberDetailsAPI(APIView):
    
    def get(self, request,memberId):

        
        try:
            print(request.data)
            members= MemberDetails.objects.get(MemberID=memberId)
            
            serializer= MemberDetailsSerializer(members)
            return Response({'status': status.HTTP_200_OK,'data': serializer.data})
        except Exception as e:
            return Response({'status': status.HTTP_405_METHOD_NOT_ALLOWED,'message': e.message})
        
class LoanDetailsAPI(APIView):

    def get(self, request,memberid):
        
        try:
            
            #memberid= request.data.get('memberid')
            print(memberid)
            Loans= Loan.objects.filter(Member=memberid)
            
            serializer= LoanSerializer(Loans,many=True)
            return Response({'status': status.HTTP_200_OK,'data': serializer.data})
        
        except Exception as e:
            return Response({'status': status.HTTP_405_METHOD_NOT_ALLOWED,'message': e.message})
        
    def post(self,request,):
        add_data=request.data
        serializer=LoanSerializer(data=add_data)
        if not serializer.is_valid():
            return Response({'status': status.HTTP_400_BAD_REQUEST,'data':serializer.errors})
        serializer.save()
        return Response({'status': status.HTTP_200_OK,'message':'Saved successfully','data': serializer.data})
    
    def patch(self, request):
        try:
            member_id = request.data.get('Member')
            if not member_id:
                
                return Response({'status': status.HTTP_400_BAD_REQUEST, 'message': 'ID is required to update the Loan details.'})

            try:
                
                update_data = Loan.objects.get(Member=member_id)
            except Loan.DoesNotExist:
                
                return Response({'status': status.HTTP_404_NOT_FOUND, 'message': 'Loan details not found.'})

            serializer = LoanSerializer(update_data, data=request.data, partial=True)
            if not serializer.is_valid():
                return Response({'status': status.HTTP_400_BAD_REQUEST, 'message': serializer.errors})
            
            serializer.save()
            return Response({'status': status.HTTP_200_OK, 'message': 'Updated successfully', 'data': serializer.data})
        
        except Loan.DoesNotExist:
            
            return Response({'status': status.HTTP_404_NOT_FOUND, 'message': 'Loan not found.'})
        except Exception as e:
            
            return Response({'status': status.HTTP_400_BAD_REQUEST, 'message': f'Something went wrong: {str(e)}'})
        

    def delete(self, request,memberid):
        try:
            del_item= Loan.objects.get(id=request.data.get('id'))
            del_item.delete()
            return Response({'status': status.HTTP_200_OK, 'message': f'item deleted successfully'})
        except Exception as e:
            return Response({'status': status.HTTP_405_METHOD_NOT_ALLOWED,'message': e.message})
