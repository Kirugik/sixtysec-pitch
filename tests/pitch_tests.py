import unittest
from app.models import Pitch

class PitchTest(unittest.TestCase):
    '''
    '''
    def setUp(self):
        '''
        '''
        new_pitch=Pitch('work experience', 'interview', 'I have 5 years of experience as a front-end engineer at XYZ company')

    def test_init(self): 
        '''
        '''
        self.assertEqual(self.new_pitch.title,'work experience')
        self.assertEqual(self.new_pitch.category,'interview')
        self.assertEqual(self.new_pitch.text,'I have 5 years of experience as a front-end engineer at XYZ company')

    def test_instance(self):
        self.assertIsInstance(self.new_pitch, Pitch)