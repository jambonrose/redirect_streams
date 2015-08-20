from unittest import TestCase
import redirect_streams


class SetupTest(TestCase):

    def test_version(self):
        self.assertTrue(hasattr(redirect_streams, '__version__'))
