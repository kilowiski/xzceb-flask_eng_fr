'''
unit test for translator
'''
import unittest
from translator import french_to_english, english_to_french
class TestFrenchToEnglish(unittest.TestCase):
    '''
    class for FR > EN
    '''
    def test_french_to_english(self):
        '''
        translate bonjour(fr>en)
        '''
        self.assertEqual(french_to_english('bonjour'.upper()), 'hello'.upper())
    def test_french_to_english_neqnull(self):
        '''
        check no null returned
        '''
        self.assertNotEqual(french_to_english('bonjour'.upper()), "")
    def test_null(self):
        '''
        null test
        '''
        self.assertEqual(french_to_english(""), "empty")
class TestEnglishToFrench(unittest.TestCase):
    '''
    class for EN > FR
    '''
    def test_english_to_french(self):
        '''
        translate hello (en>fr)
        '''
        self.assertEqual(english_to_french('hello'.upper()), 'bonjour'.upper())
    def test_english_to_french_neqnull(self):
        '''
        check no null returned
        '''
        self.assertNotEqual(english_to_french('hello'.upper()), "")
    def test_null(self):
        '''
        null test
        '''
        self.assertEqual(english_to_french(""), "empty")
unittest.main()
