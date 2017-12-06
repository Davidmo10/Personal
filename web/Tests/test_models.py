# test_models.py

import pytest
from django.test import TestCase

from mixer.backend.django import mixer

pytestmark = pytest.mark.django_db


class TestUser(TestCase):
	def test_init(self):
		obj = mixer.blend('web.Post')
		assert obj.pk == 1, "Should save an instance"


