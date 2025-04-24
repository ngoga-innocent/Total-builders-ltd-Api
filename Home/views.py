# views.py

from rest_framework import generics
from .models import Services, Project, Testimonial, OurClients,OurTeam,ContactMessage,Quote
from .serializers import (
    ServicesSerializer,
    ProjectSerializer,
    TestimonialSerializer,
    OurClientsSerializer,
    OurTeamSerializer,
    QuoteSerializer
)
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
import json
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt

class ServicesListView(generics.ListAPIView):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer

class ProjectListView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class TestimonialListView(generics.ListAPIView):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer

class OurClientsListView(generics.ListAPIView):
    queryset = OurClients.objects.all()
    serializer_class = OurClientsSerializer
class OurTeamListView(generics.ListAPIView):
    queryset = OurTeam.objects.all()
    serializer_class = OurTeamSerializer
@csrf_exempt
def contact_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            name = data.get('name')
            email = data.get('email')
            phone = data.get('phone')
            message = data.get('message')

            # Save to DB
            ContactMessage.objects.create(
                name=name,
                email=email,
                phone=phone,
                message=message
            )

            # Send email
            html_content = render_to_string("emails/contact_email.html", {
                'name': name,
                'email': email,
                'phone': phone,
                'message': message,
            })

            send_mail(
                subject=f"New Contact Message from {name}",
                message=f"Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage:\n{message}",  # Fallback plain text
                from_email='totalbuilders@gmail.com',
                recipient_list=['housemajorrwanda@gmail.com'],
                fail_silently=False,
                html_message=html_content,  # 💅 This is your pretty email
)

            return JsonResponse({'success': True, 'message': 'Message received and saved!'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)}, status=500)

    return JsonResponse({'success': False, 'message': 'Only POST method allowed'}, status=405)
@api_view(['POST'])
def submit_quote(request):
    serializer = QuoteSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            'message': 'Quote received and saved successfully!',
            'data': serializer.data
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)