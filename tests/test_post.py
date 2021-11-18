import unittest
from app.models import Post, User, Comment

class TestPost(unittest.TestCase):
    
    def setUp(self):
        self.user_dev = User(first_name = "Levy",
                                last_name = "cotech",
                                username = "cotechlevy",
                                password = "1234",
                                email = "cotechlevy@mail.com")
        self.new_post = Post(post_title = "Title",
                            post_content = "I can see you",
                            user_id = self.user_dev.id)
        self.new_comment = Comment(comment = "Nice job",
                                    post_id = self.new_post.id,
                                    user_id = self.user_dev.id)

    def test_instance(self):
        self.assertTrue(isinstance(self.user_dev, User))
        self.assertTrue(isinstance(self.new_post, Post))
        self.assertTrue(isinstance(self.new_comment, Comment))