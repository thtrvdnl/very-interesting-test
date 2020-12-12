from django.contrib.auth.models import AnonymousUser, User
from django.urls import reverse

from .models import Place
from .form import PlaceForm
from django.test import TestCase, Client


class PlaceModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(username='test', email='test@…', password='top_secret')
        Place.objects.create(user_id=1, location='Russia', comment='Very intresting')

    def test_first_location_label(self):
        place = Place.objects.get(id=1)
        field_label = place._meta.get_field('location').verbose_name
        self.assertEquals(field_label, 'location')

    def test_date_of_created_label(self):
        place = Place.objects.get(id=1)
        field_label = place._meta.get_field('created').verbose_name
        self.assertEquals(field_label, 'created')

    def test_location_max_length(self):
        place = Place.objects.get(id=1)
        max_length = place._meta.get_field('location').max_length
        self.assertEquals(max_length, 200)

    def test_comment_max_length(self):
        place = Place.objects.get(id=1)
        max_length = place._meta.get_field('comment').max_length
        self.assertEquals(max_length, 500)


class UserTest(TestCase):

    def setUp(self):
        test_user1 = User.objects.create_user(username='testuser1', password='12345')
        test_user1.save()
        test_user2 = User.objects.create_user(username='testuser2', password='12345')
        test_user2.save()

        Place.objects.create(user_id=1, location='Russia', comment='Very intresting')

    def test_base(self):
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_redirect_if_not_logged_in(self):
        resp = self.client.get(reverse('home'))
        self.assertRedirects(resp, '/')

    def test_logged_in_uses_correct_template(self):
        login = self.client.login(username='testuser1', password='12345')
        resp = self.client.get(reverse('home'))

        self.assertEqual(str(resp.context['user']), 'testuser1')

        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'core/home.html')


class PlacesListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(username='test', email='test@…', password='top_secret')
        Place.objects.create(user_id=1, location='Moscow', comment='Very intresting')
        Place.objects.create(user_id=1, location='London', comment='No intresting')

    def test_lists_all_places(self):
        login = self.client.login(username='test', password='top_secret')
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(len(resp.context['places']) == 2)
