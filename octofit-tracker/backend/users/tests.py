from django.test import TestCase


class UsersSmokeTest(TestCase):
    def test_profile_str(self):
        # basic smoke: create user and profile
        from django.contrib.auth import get_user_model
        User = get_user_model()
        user = User.objects.create_user(username='tester')
        from .models import Profile
        p = Profile.objects.create(user=user)
        self.assertIn('tester', str(p))
