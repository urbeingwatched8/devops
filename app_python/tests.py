import datetime
from django.utils import timezone
from django.test import TestCase

now = datetime.datetime.now().strftime('%M:%S')
now1=timezone.now().strftime('%M:%S')
class timeTestCase (TestCase):
    def test_now(self):
        self.assertEqual(now,now1)