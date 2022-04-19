from django.contrib.auth.models import User
from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.
class Neighborhood(models.Model):
    name = models.CharField(max_length=99, null=False, blank=False)
    location = models.CharField(max_length=199, null=False, blank=False)
    admin = models.ForeignKey(User, on_delete=models.CASCADE, max_length=99, null=False, blank=False)
    police_dept = models.CharField(max_length=99, null=True, blank=True)
    hospital_contact = models.CharField(max_length=99, null=True, blank=True)
    description = models.TextField(null=False, blank=True)
    members_count = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.name}'

    def create_neighborhood(self):
        return self.save()

    @classmethod
    def update_members(cls, neigh_id, new_count):
        neighborhood = cls.objects.filter(id=neigh_id).first()
        neighborhood.members_count = new_count
        neighborhood.save()
        return neighborhood

    @classmethod
    def get_all_items(cls):
        return cls.objects.all()

    @classmethod
    def delete_neighborhood(cls, id):
        return cls.objects.filter(id=id).delete()

    @classmethod
    def find_neighborhood(cls, id):
        return cls.objects.filter(id=id).all()

    @classmethod
    def search_item_by_location(cls, location):
        search_results = cls.objects.filter(location=location).all()
        return search_results


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, unique=True)
    # profile_img = models.ImageField(upload_to='images', blank=True)
    bio = models.TextField(blank=True)
    gen_location = models.CharField(blank=False, null=False, max_length=133)
    neighborhood_name = models.CharField(blank=False, null=False, max_length=99)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.SET_NULL, null=True, max_length=99, blank=True)
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
    def search_profile_by_neigh_name(cls, name):
        search_results = cls.objects.filter(neighborhood_name=name).all()
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

    def create_member(self):
        return self.save()

    @classmethod
    def get_all_items(cls):
        return cls.objects.all()

    @classmethod
    def delete_member(cls, id):
        return cls.objects.filter(id=id).delete()

    @classmethod
    def find_member(cls, id):
        return cls.objects.filter(id=id).all()

    @classmethod
    def search_item_by_username(cls, username):
        search_results = cls.objects.filter(user__username__icontains=username).all()
        return search_results



class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE, null=True)
    image = CloudinaryField('post_img', null=True, blank=True)
    message = models.TextField(null=False, blank=False)
    updated = models.DateTimeField(auto_now=True)
    # The auto_now_add is updated once, when the model item is created/added to the db
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}'

    def save_post(self):
        return self.save()

    @classmethod
    def get_all_posts(cls):
        return cls.objects.order_by("created")

    @classmethod
    def delete_post(cls, id):
        return cls.objects.filter(id=id).delete()

    @classmethod
    def get_post_by_id(cls, id):
        return cls.objects.filter(id=id).all()

    @classmethod
    def search_posts_by_creator_id(cls, creator_id):
        search_results = cls.objects.filter(user__id=creator_id).all()
        return search_results

    @classmethod
    def filter_by_username(cls, username):
        filter_results = cls.objects.filter(user__username__icontains=username).all()
        return filter_results



class Business(models.Model):
    name = models.CharField(max_length=99, null=False, blank=False)
    location = models.CharField(max_length=122, null=False, blank=False)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE)
    email = models.EmailField(null=True, blank=True)
    open_time = models.CharField(max_length=33, null=True, blank=True)
    close_time = models.CharField(max_length=33, null=True, blank=True)
    website = models.CharField(max_length=77, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    # The auto_now_add is updated once, when the model item is created/added to the db
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'

    def create_business(self):
        return self.save()

    @classmethod
    def update_members(cls, neigh_id, new_count):
        neighborhood = cls.objects.filter(id=neigh_id).first()
        neighborhood.members_count = new_count
        neighborhood.save()
        return neighborhood

    @classmethod
    def get_all_items(cls):
        return cls.objects.all()

    @classmethod
    def delete_business(cls, id):
        return cls.objects.filter(id=id).delete()

    @classmethod
    def find_business(cls, id):
        return cls.objects.filter(id=id).all()

    @classmethod
    def search_item_by_location(cls, location):
        search_results = cls.objects.filter(location=location).all()
        return search_results



