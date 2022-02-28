import unittest
from models import category
                                                                                                                                                                                                                                                                                                                                                         # author , title , description , publishedAt , content , url , urlToImage 
    class CategoryTest(unittest.TestCase):
        '''
        Test Class to test the behaviour of the articles class
        '''
    
    
    def setUp(self):
        '''
        setup method to run before every test
        '''

        self.new_category = Category('Alex Kimani' ,'$125 Oil Could Push The U.S. Into A Recession - OilPrice.com' ,'High oil prices and rising inflation have plagued the U.S. Fed, and now analysts are expecting the situation to become even more dire due to the ongoing Ukraine crisis' , '2022-02-27T22:00:00Z' , 'Amid the continued rally in…\r\nOil bulls are raising price…\r\nOil prices are soaring after…\r\nBy Alex Kimani - Feb 27, 2022, 4:00 PM CSTRussian forces launched theirlong-feared attack on Ukraine, and th… [+5721 chars]' , 'https://oilprice.com/Energy/Oil-Prices/Russias-War-Could-Cripple-US-Economic-Growth.html' , 'https://d32r1sh890xpii.cloudfront.net/article/718x300/2022-02-25_k9akqlg1qx.jpg')


    def test_instance(self):
        '''
        method to check if news source is an instance of the article class
        '''
        self.assertTrue(isinstance(self.new_category,Category))