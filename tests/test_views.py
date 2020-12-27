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

    def test_post_successful_request(self):
        url = reverse('api:new_relay')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user1_token.key)
        self.new_relay = {
            'name': 'post test',
            'device': 'lamp',
            'device': 'True',
            'owner': self.user1
        }
        response = self.client.post(url, self.new_relay, fromat='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_put_relay_without_token(self):
        url = reverse('api:relay', kwargs={'pk': self.desk_lamp.id })
        response = self.client.put(url, {}, fromat='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


    def test_put_successful_requests(self):
        url = reverse('api:relay', kwargs={'pk': self.desk_lamp.id })
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user1_token.key)
        self.updated_relay = {
            'name': 'updated name',
            'device': 'updated device',
            'status': 'True',
            'owner': self.user1
        }
        response = self.client.put(url, self.updated_relay, fromat='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_without_token(self):
        url = reverse('api:relay', kwargs={'pk': self.desk_lamp.id })
        response = self.client.delete(url, {}, fromat='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
