from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Neighborhood(models.Model):
    name = models.CharField(max_length=99, null=False, blank=False)
    location = models.CharField(max_length=199, null=False, blank=False)
    admin = models.ForeignKey(User, on_delete=models.CASCADE, max_length=99, null=False, blank=False)
    police_dept = models.CharField(max_length=99, null=True, blank=True)
    hospital_contact = models.CharField(max_length=99, null=True, blank=True)
    description = models.TextField(null=False, blank=True)
    members_count = models.IntegerField(default=0)


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, unique=True)
    # profile_img = models.ImageField(upload_to='images', blank=True)
    bio = models.TextField(blank=True)
    gen_location = models.CharField(blank=False, null=False, max_length=133)
    neighborhood_name = models.CharField(blank=False, null=False, max_length=99)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE, null=True, max_length=99)
    phone = models.CharField(max_length=22)
    # The auto_now is updated every time a model item is updated/saved with new changes
    updated = models.DateTimeField(auto_now=True)
    # The auto_now_add is updated once, when the model item is created/added to the db
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}'

    def save_profile(self):
        return self.save()

    @classmethod
    def get_all_profiles(cls):
        return cls.objects.all()

    @classmethod
    def delete_profile(cls, id):
        return cls.objects.filter(id=id).delete()

    @classmethod
    def get_profile_by_id(cls, id):
        return cls.objects.filter(id=id).all()

    @classmethod
    def search_profile_by_website(cls, website):
        search_results = cls.objects.filter(website=website).all()
        return search_results


class Member(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, unique=True)
    status = models.SmallIntegerField(default=0, null=False, blank=True)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.SET_NULL, null=True)
    updated = models.DateTimeField(auto_now=True)
    # The auto_now_add is updated once, when the model item is created/added to the db
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username}'

