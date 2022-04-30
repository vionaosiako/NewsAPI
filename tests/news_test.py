import unittest
from app.models import Sources
class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News class
    '''
    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Sources(1234,"Citizen TV","https://www.citizen.digital/", "General", "Meet Archbishop Anthony Muheria, The Engineer Turned Priest")
    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Sources))