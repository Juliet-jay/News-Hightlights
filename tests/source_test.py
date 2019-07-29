import unittest
from app.models import Sources



class SourcesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Sources Class
    '''

    def setUp(self):
        '''
        Set up method that will run before every test
        '''

        self.new_source=Sources('1234','NBA games','all stars playing','https://world cup finals','tenis','8.5','1122546')


    def test_instance(self):

        self.assertTrue(isinstance(self.new_source,Sources))

     
