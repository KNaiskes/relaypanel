from django.test import TestCase
from api.models import Relay, User

class RelayTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(
            username='test_user1', email='test_user1@example.com',
            password='secret1')
        self.desk_lamp = Relay.objects.create(
            name='desk lamp', device='lamp', status=False, owner=self.user1)

    def test_relay_name(self):
        relay_device = Relay.objects.get(name='desk lamp')
        self.assertEqual(relay_device.name, 'desk lamp')

    def test_relay_device(self):
        relay_device = Relay.objects.get(name='desk lamp')
        self.assertEqual(relay_device.device, 'lamp')

    def test_relay_owner(self):
        relay_device = Relay.objects.get(name='desk lamp')
        self.assertEqual(relay_device.owner, self.user1)

    def test_relay_status(self):
        relay_device = Relay.objects.get(name='desk lamp')
        self.assertFalse(relay_device.status, False)
