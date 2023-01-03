from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from django.contrib.auth.models import User
from .models import Profile

from django.core.mail import send_mail
from django.conf import settings #signals.py'dan sonra Django'ya tanıt apps.py'da yapabilirsin bunu.

# @receiver(post_save, sender=Profile)


def createProfile(sender, instance, created, **kwargs): #Anytime we add a user a profile is autamatically created. Sender the Model that sends it.Instance of a model that actually triggered this or object.Created true or false.
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            name=user.first_name,
        )

        subject = 'Welcome to my PortfolioSite!'
        message = 'I am glad you are here!'

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [profile.email],
            fail_silently=False,
        )

post_save.connect(createProfile, sender=User) #Everytime save method is called on a User(User gets created) model trigger this method.