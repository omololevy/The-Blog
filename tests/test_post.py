import unittest
from app.models import Post, User, Comment

class TestPost(unittest.TestCase):
    
    def setUp(self):
        self.dev_user = User(first_name = "Cotech", last_name = "Levy", username = "cotech_m", password = "easy", email = "cotech@mail.com")
        self.new_post = Post(post_title = "Sample Title", post_content = "Hallo Welt! Ich bin hier", user_id = self.dev_user.id)
        self.new_comment = Comment(comment = "Nice job", post_id = self.new_post.id, user_id = self.dev_user.id)

    def test_instance(self):
        self.assertTrue(isinstance(self.dev_user, User))
        self.assertTrue(isinstance(self.new_post, Post))
        self.assertTrue(isinstance(self.new_comment, Comment))