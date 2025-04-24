# serializers.py

from rest_framework import serializers
from .models import Services, Project, Testimonial, OurClients,OurTeam,Quote

class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

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
        fields = ['id', 'name', 'email', 'message', 'created_at']
