import unittest

from agent.utils import get_s3_client

AUTH = {"ACCESS_KEY": "key", "SECRET_KEY": "secret", "REGION": "us-east-1"}


class TestGetS3Client(unittest.TestCase):
    def test_custom_endpoint_is_used(self):
        s3 = get_s3_client({"bucket": "b", "auth": AUTH, "endpoint": "https://s3.example.com"})
        self.assertEqual(s3.meta.endpoint_url, "https://s3.example.com")

    def test_falls_back_to_aws(self):
        for offsite in ({"auth": AUTH}, {"auth": AUTH, "endpoint": None}, {"auth": AUTH, "endpoint": ""}):
            s3 = get_s3_client(offsite)
            self.assertTrue(s3.meta.endpoint_url.endswith(".amazonaws.com"))

    def test_region_is_optional(self):
        auth = {"ACCESS_KEY": "key", "SECRET_KEY": "secret"}
        self.assertIsNotNone(get_s3_client({"auth": auth, "endpoint": "https://s3.example.com"}))
