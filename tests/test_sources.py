import unittest
from app.models import Source

class SourceTest(unittest.TestCase):
    '''
    Test class to test the Sources class
    '''

    def setUp(self):
        '''
        setup method that will run before every test
        '''
        self.news_source = ('bbc-news' , 'BBC News' , 'Estonia, Latvia and Slovenia join Bulgaria, Poland, the Czech Republic and the UK in announcing curbs.' , 'http://www.bbc.co.uk/news/world-europe-60539303')
    

    def test_instance(self):
        '''
        method to check if news source is an instance of the article class
        '''
        self.assertTrue(isinstance(self.news_source, Source))


# if __name__ == '__main__':
#     unittest.main()