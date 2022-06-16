
from urllib import request
from rest_framework.response import Response
from api.serializers import SkillSerializer,ProjectSerializer,EmailSerializer,ContactSerializer
from api.models import Skill, Project,Contact
from rest_framework.decorators import api_view
from django.core.exceptions import ValidationError
from rest_framework import status
from api.bot.chat import get_response
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseServerError
# @api_view(['GET'])
# def skills(request, *args,**kwargs):
#     skills = Skill.objects.all()
#     serializer= SkillSerializer(skills, many=True)
#     return Response(serializer.data)



# @api_view(['POST'])
# def skill_create(request, *args,**kwargs):
#     serializer= SkillSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     else:
#         return Response(serializer.errors)
    
# @api_view(['GET', 'PUT', 'DELETE'])    
# def skill(request, pk):
#     try:
#         book = Skill.objects.get(pk=pk)
#     except:
#         return Response({'error':'Book does not exist'}, status=status.HTTP_404_NOT_FOUND)
#     if request.method=='GET':
  
#         serializer= SkillSerializer(book)
#         return Response(serializer.data)
    
#     if request.method=="PUT":
#         serializer= SkillSerializer(book, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response( serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

#     if request.method=="DELETE":
#         book.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
            

from rest_framework.views import APIView

class SkillList(APIView):
    
    def get(self, request):
        skills = Skill.objects.all()
        serializer= SkillSerializer(skills, many=True)
        return Response(serializer.data)


class SkillCreate(APIView):
    
    def post(self, request):
        serializer= SkillSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
        
class SkillView(APIView):
    def get_book_by_pk(self, pk):
        try:
            book = Skill.objects.get(pk=pk)
            return book
        except:
            return Response({'error':'Book does not exist'}, status=status.HTTP_404_NOT_FOUND)
    def get(self, request, pk):
        book= self.get_book_by_pk(pk)
        serializer= SkillSerializer(book)
        return Response(serializer.data)
    
    def put(self, request, pk):
        book= self.get_book_by_pk(pk)
        serializer= SkillSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response( serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        book= self.get_book_by_pk(pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
    
    
class ProjectList(APIView):
    
    def get(self, request):
        skills = Project.objects.all()
        serializer= ProjectSerializer(skills, many=True)
        return Response(serializer.data)


class ProjectCreate(APIView):
    
    def post(self, request):
        serializer= ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
   
class ProjectView(APIView):
    def get_project_by_pk(self, pk):
        try:
            book = Project.objects.get(pk=pk)
            return book
        except:
            return Response({'error':'Book does not exist'}, status=status.HTTP_404_NOT_FOUND)
    def get(self, request, pk):
        book= self.get_project_by_pk(pk)
        serializer= ProjectSerializer(book)
        return Response(serializer.data)
    
    def put(self, request, pk):
        project= self.get_project_by_pk(pk)
        serializer= ProjectSerializer(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response( serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        project= self.get_project_by_pk(pk)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
class PredictionView(APIView):
    def post(self, request):
        text=request.data
        response=get_response(text['message'])
  
        message={"message":response}
    
        return Response(message)
        
        
class SendEmailView(APIView):
    def post(self,request):
        subject = request.data['subject']
        message = request.data['message']
        email = request.data['emailAddress']
        serializer= EmailSerializer(data=request.data)
        print('valid?', serializer.is_valid(), serializer.errors)
        if serializer.is_valid(raise_exception=True):
            try:
                send_mail(subject=subject, message=message, from_email=settings.EMAIL_HOST_USER, recipient_list=[email], fail_silently=False)
                return Response({"success":True})
            except Exception as e:
                return  Response({'Exception: ', str(e)},status=status.HTTP_400_BAD_REQUEST)
            
            
            
class ContactCreate(APIView):
    def post(self, request):
        # title= request.data['title']
        # description= request.data['description']
        # logoLink=request.data['logoLink']
        serializer= ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
class ContactList(APIView):
    def get(self, request):
        contacts = Contact.objects.all()
        serializer= ContactSerializer(contacts, many=True)
        return Response(serializer.data)
