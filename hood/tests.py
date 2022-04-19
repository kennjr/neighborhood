import os
from django.test import TestCase

# Create your tests here.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'neighborhood.settings')
import django
django.setup()

from django.contrib.auth.models import User
# Create your tests here.
from hood.models import Profile, Neighborhood, Business, Post, Member


class ProfileTestsClass(TestCase):
    # set up method
    def setUp(self):

        # creating a new category
        self.test_user = User.objects.create(username='theuser', password="12345")
        self.neighborhood = Neighborhood.objects.create(name="The hood", location="A test loc", admin=self.test_user,
                                                        police_dept="1234566", hospital_contact="003290939",
                                                        description="", members_count=0)
        # self.test_category.save_category()

        # self.test_local_user = Like(user=self.test_user, user=self.test_user)

        self.test_profile = Profile(user=self.test_user, neighborhood_name='nayborhud', phone="12345666",
                                    bio="test_loc", neighborhood=self.neighborhood, gen_location="A gen location")

    # testing instance
    def test_instance(self):
        profile = self.test_profile
        self.assertEqual(self.test_profile, profile)

    # testing save method
    def test_save_profile_method(self):
        original_len = Profile.get_all_profiles()
        print(f'original len {len(original_len)}')
        self.test_profile.save_profile()

        new_len = Profile.get_all_profiles()
        print(f'new len {len(new_len)}')
        self.assertTrue(len(new_len) > len(original_len))

    def test_delete_profile_method(self):
        self.test_profile.save_profile()
        original_len = Profile.objects.all()
        print(f'the categorys are{len(original_len)}')
        Profile.delete_profile(self.test_profile.id)
        new_len = Profile.objects.all()
        print(f'the categorys are{len(new_len)}')
        self.assertTrue((len(new_len)) == (len(original_len) - 1))

    def test_get_profile_by_id_method(self):
        self.test_profile.save_profile()
        req_result = Profile.get_profile_by_id(self.test_profile.id)
        self.assertTrue(req_result is not None)

    def test_search_profile_by_neigh_name_method(self):
        self.test_profile.save_profile()

        req_result = Profile.search_profile_by_neigh_name(self.test_profile.neighborhood_name)
        self.assertTrue(req_result is not None)


class NeighborhoodTestsClass(TestCase):
    # set up method
    def setUp(self):

        # creating a new category
        self.test_user = User.objects.create(username='theuser', password="12345")
        self.test_neighborhood = Neighborhood(name="The hood", location="A test loc", admin=self.test_user,
                                              police_dept="1234566", hospital_contact="003290939",
                                              description="", members_count=0)

    # testing instance
    def test_instance(self):
        neighborhood = self.test_neighborhood
        self.assertEqual(self.test_neighborhood, neighborhood)

    # testing save method
    def test_save_neighborhood_method(self):
        original_len = Neighborhood.get_all_items()
        print(f'original len {len(original_len)}')
        self.test_neighborhood.create_neighborhood()

        new_len = Neighborhood.get_all_items()
        print(f'new len {len(new_len)}')
        self.assertTrue(len(new_len) > len(original_len))

    def test_delete_neighborhood_method(self):
        self.test_neighborhood.create_neighborhood()
        original_len = Neighborhood.objects.all()
        print(f'the categorys are{len(original_len)}')
        Neighborhood.delete_neighborhood(self.test_neighborhood.id)
        new_len = Neighborhood.objects.all()
        print(f'the categorys are{len(new_len)}')
        self.assertTrue((len(new_len)) == (len(original_len) - 1))

    def test_get_neighborhood_by_id_method(self):
        self.test_neighborhood.create_neighborhood()
        req_result = Neighborhood.find_neighborhood(self.test_neighborhood.id)
        self.assertTrue(req_result is not None)

    def test_search_neighborhood_by_neigh_name_method(self):
        self.test_neighborhood.create_neighborhood()

        req_result = Neighborhood.search_item_by_location(self.test_neighborhood.location)
        self.assertTrue(req_result is not None)

    def test_update_members_count(self):
        self.test_neighborhood.create_neighborhood()
        old_mem_count = self.test_neighborhood.members_count
        print(f'the old count{old_mem_count}')
        self.test_neighborhood.update_members(self.test_neighborhood.id, (old_mem_count + 1))
        new_mem_count = self.test_neighborhood.members_count
        print(f'the new count{new_mem_count}')
        self.assertTrue(new_mem_count > old_mem_count)


class BusinessTestsClass(TestCase):
    # set up method
    def setUp(self):

        # creating a new category
        self.test_user = User.objects.create(username='theuser', password="12345")
        self.test_neighborhood = Neighborhood.objects.create(name="The hood", location="A test loc", admin=self.test_user,
                                              police_dept="1234566", hospital_contact="003290939",
                                              description="", members_count=0)
        self.test_business = Business(name='test_business', location="6th Coley Ave.", neighborhood=self.test_neighborhood,
                                      phone="12355")

    # testing instance
    def test_instance(self):
        business = self.test_business
        self.assertEqual(self.test_business, business)

    # testing save method
    def test_save_business_method(self):
        original_len = Business.get_all_items()
        print(f'original len {len(original_len)}')
        self.test_business.create_business()

        new_len = Business.get_all_items()
        print(f'new len {len(new_len)}')
        self.assertTrue(len(new_len) > len(original_len))

    def test_delete_business_method(self):
        self.test_business.create_business()
        original_len = Business.objects.all()
        print(f'the categorys are{len(original_len)}')
        Business.delete_business(self.test_business.id)
        new_len = Business.objects.all()
        print(f'the categorys are{len(new_len)}')
        self.assertTrue((len(new_len)) == (len(original_len) - 1))

    def test_get_business_by_id_method(self):
        self.test_business.create_business()
        req_result = Business.find_business(self.test_neighborhood.id)
        self.assertTrue(req_result is not None)

    def test_search_business_by_location_method(self):
        self.test_business.create_business()

        req_result = Business.search_item_by_location(self.test_neighborhood.location)
        self.assertTrue(req_result is not None)

    def test_update_members_count(self):
        self.test_neighborhood.create_neighborhood()
        old_mem_count = self.test_neighborhood.members_count
        print(f'the old count{old_mem_count}')
        self.test_neighborhood.update_members(self.test_neighborhood.id, (old_mem_count + 1))
        new_mem_count = self.test_neighborhood.members_count
        print(f'the new count{new_mem_count}')
        self.assertTrue(new_mem_count > old_mem_count)


class PostTestsClass(TestCase):
    # set up method
    def setUp(self):

        # creating a new category
        self.test_user = User.objects.create(username='theuser', password="12345")
        self.test_neighborhood = Neighborhood.objects.create(name="The hood", location="A test loc", admin=self.test_user,
                                              police_dept="1234566", hospital_contact="003290939",
                                              description="", members_count=0)
        # self.test_category.save_category()

        self.test_post = Post(user=self.test_user, image='galleria_imgs/hobbies_7.jpg',
                              neighborhood=self.test_neighborhood, message="The caption")

    # testing instance
    def test_instance(self):
        img = self.test_post
        self.assertEqual(self.test_post, img)

    # testing save method
    def test_save_post_method(self):
        original_len = Post.get_all_posts()
        print(f'original len {len(original_len)}')
        self.test_post.save_post()
        new_len = Post.get_all_posts()
        print(f'new len {len(new_len)}')
        self.assertTrue(len(new_len) > len(original_len))

    def test_delete_post_method(self):
        self.test_post.save_post()
        original_len = Post.objects.all()
        print(f'the categorys are{len(original_len)}')
        Post.delete_post(self.test_post.id)
        new_len = Post.objects.all()
        print(f'the categorys are{len(new_len)}')
        self.assertTrue((len(new_len)) == (len(original_len) - 1))

    def test_get_post_by_id_method(self):
        self.test_post.save_post()
        req_result = Post.get_post_by_id(self.test_post.id)
        self.assertTrue(req_result is not None)

    def test_search_posts_method(self):
        self.test_post.save_post()
        search_results = Post.search_posts_by_creator_id(self.test_user.id)
        print(f'The list length {len(search_results)}')
        self.assertTrue(search_results != [])

    def test_filter_posts_list_method(self):
        self.test_post.save_post()
        filter_results = Post.filter_by_username(self.test_user.username)
        print(f'The list length {len(filter_results)}')
        self.assertTrue(filter_results != [])


class MemberTestsClass(TestCase):
    # set up method
    def setUp(self):

        # creating a new category
        self.test_user = User.objects.create(username='theuser', password="12345")
        self.test_neighborhood = Neighborhood.objects.create(name="The hood", location="A test loc", admin=self.test_user,
                                              police_dept="1234566", hospital_contact="003290939",
                                              description="", members_count=0)

        self.test_member = Member(user=self.test_user, status=0, neighborhood=self.test_neighborhood)

    # testing instance
    def test_instance(self):
        member = self.test_member
        self.assertEqual(self.test_member, member)

    # testing save method
    def test_save_member_method(self):
        original_len = Member.get_all_items()
        print(f'original len {len(original_len)}')
        self.test_member.create_member()

        new_len = Member.get_all_items()
        print(f'new len {len(new_len)}')
        self.assertTrue(len(new_len) > len(original_len))

    def test_delete_neighborhood_method(self):
        self.test_neighborhood.create_neighborhood()
        original_len = Neighborhood.objects.all()
        print(f'the categorys are{len(original_len)}')
        Neighborhood.delete_neighborhood(self.test_neighborhood.id)
        new_len = Neighborhood.objects.all()
        print(f'the categorys are{len(new_len)}')
        self.assertTrue((len(new_len)) == (len(original_len) - 1))

    def test_get_neighborhood_by_id_method(self):
        self.test_neighborhood.create_neighborhood()
        req_result = Neighborhood.find_neighborhood(self.test_neighborhood.id)
        self.assertTrue(req_result is not None)

    def test_search_neighborhood_by_neigh_name_method(self):
        self.test_neighborhood.create_neighborhood()

        req_result = Neighborhood.search_item_by_location(self.test_neighborhood.location)
        self.assertTrue(req_result is not None)

