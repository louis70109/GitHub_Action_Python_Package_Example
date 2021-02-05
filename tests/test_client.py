import unittest

from GitHub_Action_Python_Example.client import HelloWorld


class TestClient(unittest.TestCase):
    def setUp(self):
        self.message = "It is test from package."
        self.test_with_message = HelloWorld(message=self.message)
        self.test_default = HelloWorld()

    def test_get_auth_link(self):
        result = self.test_with_message.get_message()
        default_result = self.test_default.get_message()
        self.assertEqual(result, self.message)
        self.assertEqual(default_result, "Hello World!")
