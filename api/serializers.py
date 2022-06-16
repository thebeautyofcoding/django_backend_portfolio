from rest_framework  import serializers
from api.models import Skill,Project, Contact


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields=["id","title", "shortDescription", "detailedDescription"]
        
        
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields=["id","title", "shortDescription", "detailedDescription"]
        
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields=["id","title", "description", "logoLink"]
        
        
class EmailSerializer(serializers.Serializer):
    emailAddress= serializers.EmailField()
    subject= serializers.CharField(max_length=400)
    message=serializers.CharField()
    
    def validate_subject(self, value):
        if len(value)<5:
            raise serializers.ValidationError('The subject must be at least 5 letters long!')
        return value
    
    def validate_message(self, value):
        if len(value)<10:
            raise serializers.ValidationError('The message must be at least 10 letters long!')
        return value
    

    
                
        
        


        