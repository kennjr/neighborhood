from django.contrib import admin


# Register your models here.
from hood.models import Profile, Neighborhood, Member, Post, Business


class ProfileAdmin(admin.ModelAdmin):
    # The line below will allow us to display the meetup obj items in a list with the specified columns
    # the columnnames in the models are what we've used in the strs
    list_display = ('neighborhood_name', 'gen_location', 'phone')
    # The line below will allow us to have filter opts for our list of entries that appear in the admin dash
    list_filter = ('gen_location', )
    # The line below will pre-populate the slug field based on the title we enter,
    #  the key is the param that we'd like to pre-populate and the tuple has the entries that'll be concat'ed to create the key
    # prepopulated_fields = {'slug': ('title',)}


class NeighborhoodAdmin(admin.ModelAdmin):
    # The line below will allow us to display the meetup obj items in a list with the specified columns
    # the columnnames in the models are what we've used in the strs
    list_display = ('name', 'location', 'members_count')
    # The line below will allow us to have filter opts for our list of entries that appear in the admin dash
    list_filter = ('members_count', )
    # The line below will pre-populate the slug field based on the title we enter,
    #  the key is the param that we'd like to pre-populate and the tuple has the entries that'll be concat'ed to create the key
    # prepopulated_fields = {'slug': ('title',)}


class MemberAdmin(admin.ModelAdmin):
    # The line below will allow us to display the meetup obj items in a list with the specified columns
    # the columnnames in the models are what we've used in the strs
    # list_display = ('name', 'location', 'members_count')
    # The line below will allow us to have filter opts for our list of entries that appear in the admin dash
    list_filter = ('status', )
    # The line below will pre-populate the slug field based on the title we enter,
    #  the key is the param that we'd like to pre-populate and the tuple has the entries that'll be concat'ed to create the key
    # prepopulated_fields = {'slug': ('title',)}


class PostAdmin(admin.ModelAdmin):
    # The line below will allow us to display the meetup obj items in a list with the specified columns
    # the columnnames in the models are what we've used in the strs
    list_display = ('message', 'image')
    # The line below will allow us to have filter opts for our list of entries that appear in the admin dash
    list_filter = ('user', )
    # The line below will pre-populate the slug field based on the title we enter,
    #  the key is the param that we'd like to pre-populate and the tuple has the entries that'll be concat'ed to create the key
    # prepopulated_fields = {'slug': ('title',)}


class BusinessAdmin(admin.ModelAdmin):
    # The line below will allow us to display the meetup obj items in a list with the specified columns
    # the columnnames in the models are what we've used in the strs
    list_display = ('name', 'phone')
    # The line below will allow us to have filter opts for our list of entries that appear in the admin dash
    list_filter = ('location', )
    # The line below will pre-populate the slug field based on the title we enter,
    #  the key is the param that we'd like to pre-populate and the tuple has the entries that'll be concat'ed to create the key
    # prepopulated_fields = {'slug': ('title',)}


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Neighborhood, NeighborhoodAdmin)
admin.site.register(Member, MemberAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Business, BusinessAdmin)
