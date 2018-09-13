import unittest
from app.models import Comment

class CommentTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Pitch class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_comment = Comment(1234, 'I love this pitch')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_comment,Comment))