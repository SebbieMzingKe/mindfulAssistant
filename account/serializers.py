from .models import User, Conversation, Message, SentimentAnalysisResult, WellbeingPlan, ProgressTracker, Resource, CommunityPost
from rest_framework import serializers
from rest_framework.validators import ValidationError

class UserSerializer(serializers.ModelSerializer):
    email = serializers.CharField(max_length = 50)
    username = serializers.CharField(max_length = 45)
    password = serializers.CharField(min_length = 8, write_only = True)
    
    class Meta:
        model = User
        fields = "__all__"
        
        
        def validate(self, attrs):
            email_exists = User.objects.filter(email = attrs["email"]).exists()
            if email_exists:
                raise ValidationError("Email has already been used")
            return super().validate(attrs)

        def create(self, validated_data):
            password = validated_data.pop(password)
            user = super().create(validated_data)
            user.set_password(password)
            user.save()
            return user



class ConversationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conversation
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializers):
    class Meta:
        model = Message
        fields = '__all__'

class SentimentAnalysisResultSerializer(serializers.ModelSerializer):
    class meta:
        model = SentimentAnalysisResult
        fields = '__all__'

class WellbeingPlanSerializer(serializers.ModelSerializer):
     class Meta:
        model = WellbeingPlan
        fields = '__all__'

class ProgressTrackerSerializer(serializers.ModelSerializer):
     class Meta:
        model = ProgressTracker
        fields = '__all__'

class ResourceSerializer(serializers.ModelSerializer):
     class Meta:
        model = Resource
        fields = '__all__'

class CommunityPostSerializer(serializers.ModelSerializer):
     class Meta:
        model = CommunityPost
        fields = '__all__'