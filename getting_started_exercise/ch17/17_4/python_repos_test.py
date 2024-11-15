import unittest
import requests

class TestApi(unittest.TestCase):

    def test_api(self):

        url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
        r = requests.get(url)
        c = r.status_code

        response_dict = r.json()
        repo_dicts = response_dict['items']
        

        self.assertEqual(c, 200)
        self.assertTrue(response_dict['total_count'] > 14000000)
        self.assertTrue(len(repo_dicts) > 20)



if __name__ == '__main__':
    unittest.main()