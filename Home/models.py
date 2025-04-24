from django.db import models

# Create your models here.
class Services(models.Model):
    title=models.TextField()
    description=models.TextField()
    image=models.ImageField(null=True,blank=True,upload_to='Services/')
    
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural='Services'
class Project(models.Model):
    image=models.ImageField(upload_to='Project/')
    title=models.TextField(null=True,blank=True)
    location=models.TextField(null=True,blank=True)
    duration=models.TextField(null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
class Testimonial(models.Model):
    name=models.CharField(max_length=200)
    location=models.CharField(max_length=200)
    message=models.TextField()
    rating=models.IntegerField()
    user_image=models.ImageField(upload_to='Testmonies/Users/',null=True,blank=True)
    company_icon=models.ImageField(upload_to='Testmonies/',null=True,blank=True)
    
    def __str__(self):
        return self.name
class OurClients(models.Model):
    company_name=models.CharField(max_length=200)
    company_logo=models.ImageField(upload_to='OurClients/')
    
    def __str__(self):
        return self.company_name
    class Meta:
        verbose_name_plural='Our Clients'
class OurTeam(models.Model):
    image=models.ImageField(upload_to='Team/')
    name=models.CharField(max_length=200)
    position=models.CharField(max_length=200)
    linkedlin=models.TextField()
    
    def __str__(self):
        return self.name
class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"
class Quote(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"