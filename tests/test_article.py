import unittest
from app.models import Article


class ArticleTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the articles class
    '''
    def setUp(self):
        '''
        setup method that will run before every test
        '''
        self.new_article = Article('Adam Satariano' ,'Russia Intensifies Censorship Campaign, Pressuring Tech Giants - The New York Times' , 'Google, Apple and others were warned that they must comply with a new law, which would make them more vulnerable to the Kremlin’s censorship demands.' , '2022-02-26T11:48:59Z' ,'On Feb. 16, a Roskomnadzor official said companies that did not comply by the end of the month would face penalties. In addition to fines and possible shutdowns or slowdowns, the penalties could disr… [+1720 chars]' , 'https://www.nytimes.com/2022/02/26/technology/russia-censorship-tech.html' ,  'https://static01.nyt.com/images/2022/02/25/business/25RUSSIA-INTERNET-COMBO/25RUSSIA-INTERNET-COMBO-facebookJumbo.jpg')

    def test_instances(self):
        '''
        method to check if new article is an instance of the article class
        '''
        self.assertTrue(isinstance(self.new_article,Article))

