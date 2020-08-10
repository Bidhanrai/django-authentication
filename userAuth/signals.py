from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import UserProfileInfo


def user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfileInfo.objects.create(
            user=instance
        )
        print('profile created')
    else:
        instance.profile.save()
        print('profile updated')


post_save.connect(user_profile, sender=User)
