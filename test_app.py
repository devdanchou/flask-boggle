from unittest import TestCase

from app import app, games


# Make Flask errors be real errors, not HTML pages with error info
app.config['TESTING'] = True

# This is a bit of hack, but don't use Flask DebugToolbar
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']


class BoggleAppTestCase(TestCase):
    """Test flask app of Boggle."""

    def setUp(self):
        """Stuff to do before every test."""

        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_homepage(self):
        """Make sure information is in the session and HTML is displayed"""

        with self.client as client:
            response = client.get('/')
            html = response.get_data(as_text=True)
            self.assertEqual(response.status_code, 200)
            self.assertIn('<button class="word-input-btn">Go</button>', html)
            # test that you're getting a template

    def test_api_new_game(self):
        """Test starting a new game."""

        with self.client as client:
            response = client.post("/api/new-game")
            json_data = response.get_json()
            # dict_from_json = json.loads(json_data)
            self.assertEqual(response.status_code, 200)
            self.assertTrue(response.is_json, True)
            self.assertIn("gameId", json_data)
            self.assertIn("board", json_data)
            breakpoint()
            self.assertIn(json_data["gameId"], games)
