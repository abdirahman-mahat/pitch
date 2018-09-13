import unittest
from app.models import Pitch

class PitchTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Pitch class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_pitch = Pitch(56,'My pitch','I can pitch all day long','But wont',15,72)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_pitch,Pitch))

if __name__ ==  '__main__':
    unittest.main()