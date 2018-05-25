import unittest
import os

from cfgtool import config

class BasicTest(unittest.TestCase):
    def test_init(self):
        self.assertEqual(1+1,2)

class TestConfLoad(unittest.TestCase):
    def setUp(self):
        os.environ['ENV'] = 'test'

    def test_load_yaml_file(self):
        pass

    def test_load_yaml_string(self):
        test_yaml = "title: testPostTitle\n" \
                    "categories: \n" \
                    "  - TestCate1\n" \
                    "  - TestCate2\n" \
                    "tags: \n" \
                    "  - Tag1\n" \
                    "  - Tag2\n"
        expected_data = {
            "title": "testPostTitle",
            "categories": ["TestCate1", "TestCate2"],
            "tags": ['Tag1', 'Tag2']
        }
        result = config.parse_yaml_string(test_yaml)
        self.assertDictEqual(result, expected_data)


if __name__ == '__main__':
    unittest.main()