from app import getURLData, parseData
import unittest, urllib2, ssl

class TestMyApp(unittest.TestCase) :
    def test_getURLData_ValueError(self) :
        with self.assertRaises(ValueError) :
            getURLData('www.google.com')

    def test_getURLData_HTTPError(self) :
        with self.assertRaises(urllib2.HTTPError) :
            getURLData('https://www.google.com/asasasdd/asdasajjf')

    def test_getURLData_URLError(self) :
        with self.assertRaises(urllib2.URLError) :
            getURLData('https://www.google123124dd3.com')
            getURLData('https://asddd.google.com')

    def test_getURLData_CertificateError(self) :
        with self.assertRaises(ssl.CertificateError) :
            getURLData('https://flask.pocoo.org/')

if __name__ ==  '__main__' :
    unittest.main()
