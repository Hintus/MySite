from xmlrpc.client import DateTime

from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User, AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver



# Create your models here.

class MyGroups(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    countOfMembers = models.IntegerField(default=0)
    is_open = models.BooleanField(default=True)
    password = models.TextField(blank=True, null=True)
    meeting_Date = models.DateTimeField(blank=True)
    meeting_place = models.CharField(max_length=255)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d", blank=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Все группы'
        verbose_name_plural = 'Все группы'
        ordering = ['name', 'time_create']

    def get_absolute_url(self):
        return reverse('group_profile_url', kwargs={'group_slug': self.slug})


class Goods(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    name = models.CharField(max_length=50)
    prise = models.IntegerField(null=False)
    Count_of_subspecies = models.IntegerField


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE, related_name='profile')
    age = models.IntegerField(null=True, blank=True)
    telefone_num = models.TextField(null=True, blank=True)
    interests = models.TextField(null=True, blank=True)
    profile_pic = models.ImageField(null=True, blank=True, upload_to="groupsapp/static/img")

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def get_absolute_url(self):
        return reverse('show_profile_url', kwargs={'Profile_id': self.id})
