import unittest
from models import headlines


class HeadlinesTest(unittest.TestCase):
    '''
    test class to test the behaviour of the headlines class
    '''

    def setUp(self):
        '''
        setup method that will run before every test
        '''
        self.new_headlines = Headlines('Axios' , 'Putin orders nuclear deterrent forces on alert - Axios' , 'He cited the sanctions and \"aggressive actions\" from Western countries.' , '2022-02-27T13:57:44Z' , 'Russian President Vladimir Putin said in a televised statement on Sunday that he was ordering Russia\'s nuclear deterrent forces on alert, as he continues his unprovoked invasion of Ukraine.\r\nDriving … [+1866 chars]' , 'https://www.axios.com/putin-nuclear-forces-9d1a2823-9512-4ab3-89f2-118ee37e0970.html' , 'https://images.axios.com/-uIsSzn2HdCxfaszTbgMXRzTkec=/0x0:2503x1408/1366x768/2022/02/27/1645967879761.jpg')

    def test_instance(self):
        '''
        method to check if news source is an instance of the article class
        '''
        self.assertTrue(isinstance(self.new_headlines,Headlines))