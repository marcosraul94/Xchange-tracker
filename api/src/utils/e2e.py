import logging
from unittest import TestCase
from src.repositories.base import Repository
from src.views.migrations import migrate


class E2ETestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        loggers = logging.Logger.manager.loggerDict.keys()

        for logger in loggers:
            logging.getLogger(logger).setLevel(logging.CRITICAL)

    def setUp(self):
        Repository().table.delete()
        migrate()
