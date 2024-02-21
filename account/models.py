from django.db import models

# Create your models here.

class User(models.Model):
        username = models.CharField(max_length = 50, unique = True)
        password = models.CharField(max_length =  45)
        email = models.CharField(unique = True)
        
        def __str__(self):
             return self.username
        
class Conversation(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    created = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
             return self.user

class Message(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete = models.CASCADE)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
             return self.conversation

class SentimentAnalysisResult(models.Model):
    message = models.OneToOneField(Message, on_delete = models.CASCADE)
    sentiment_score = models.TextField()
    
    def __str__(self):
             return self.message

class WellbeingPlan(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    content = models.TextField()
    
    def __str__(self):
             return self.user

class ProgressTracker():
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    progress_percentage = models.FloatField()
    
    
    def __str__(self):
             return self.user

class Resource(models.Model):
    Wellbeing_plan = models.ForeignKey(WellbeingPlan, on_delete = models.CASCADE)
    title = models.CharField(max_length = 100)
    link = models.URLField()

    def __str__(self):
             return self.Wellbeing_plan
         
         
class CommunityPost(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    content = models.CharField
    created = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
             return self.user