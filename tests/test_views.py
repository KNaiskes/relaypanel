from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from api.models import Relay, User

class ViewsTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()

        self.user1 = User.objects.create_user(
            username='test_user1', email='test_user1@example.com',
            password='secret1')

        self.user1_token = Token.objects.get(user__username=self.user1)

        self.desk_lamp = Relay.objects.create(
            name='desk lamp', device='lamp', status=False, owner=self.user1)

    def test_get_relays_list_without_token(self):
        url = reverse('api:relays')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_relays_list_with_token(self):
        url = reverse('api:relays')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user1_token.key)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_relays_without_token(self):
        url = reverse('api:new_relay')
        response = self.client.post(url, {}, fromat='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
