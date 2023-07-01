from django.contrib.auth.models import User, AnonymousUser
from .models import Profile
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_out, user_logged_in
from django.shortcuts import get_object_or_404

# Create Profile for User
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created and not hasattr(instance, 'profile'):
        Profile.objects.create(user=instance)
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    if hasattr(instance, 'profile'):
        instance.profile.save()

# Login
@receiver(user_logged_in)
def on_user_logged_in(sender, request, **kwargs):
    if isinstance(request.user, AnonymousUser):
        return
    user = request.user
    profile = get_object_or_404(Profile, user=user)
    profile.online = True
    profile.save()

# Logout
@receiver(user_logged_out)
def on_user_logged_out(sender, request, **kwargs):
    if isinstance(request.user, AnonymousUser):
        return
    user = request.user
    profile = get_object_or_404(Profile, user=user)
    profile.online = False
    profile.save()