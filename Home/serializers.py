# serializers.py

from rest_framework import serializers
from .models import Services, Project, Testimonial, OurClients,OurTeam,Quote,ProjectImage

class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = '__all__'
class ProjectImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectImage
        fields = ['id', 'image']

class ProjectSerializer(serializers.ModelSerializer):
    images = ProjectImageSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ['id','thumbnail','title', 'location', 'duration', 'description', 'created_at', 'images']


class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = '__all__'

class OurClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurClients
        fields = '__all__'
class OurTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurTeam
        fields = '__all__'
class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = ['id', 'name', 'email', 'message','attachment', 'created_at']
