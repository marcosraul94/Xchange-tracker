from unittest import TestCase
from src.repositories.base import Repository
from src.views.migrations import migrate


class E2ETestCase(TestCase):
    def setUp(self):
        Repository().table.delete()
        migrate()
