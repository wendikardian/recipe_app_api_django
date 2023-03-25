"""Tests for the Django admin modifications"""


from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import Client


class AdminSiteTests(TestCase):
    """test case for django admin modifications"""
    # Setup create a client and superuser and a test regularly user
    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@example.com',
            password='testpass123'
        )
        # force authentication using user that we created before
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='user@example.com',
            password='testpass123',
            name='Test User'
        )

    # Test to get user
    def test_user_list(self):
        """test that if users are listed on page or not !"""
        # Reverse to get the url for the change list inside the Django App.
        url = reverse('admin:core_user_changelist')
        # Using http get request
        res = self.client.get(url)
        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_edit_user_page(self):
        """Test the edit user page works."""
        url = reverse('admin:core_user_change', args=[self.user.id])
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)