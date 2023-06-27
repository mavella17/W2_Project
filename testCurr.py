import unittest
import requests
from capi_main import updateDB, printDB
from capi_main import getList, base_exchange
from capi_main import checkValidCurrency


class TestFileName(unittest.TestCase):
	# These first 3 test cases only verify they run without errors
	# Not much other testing can be done here
    def testUpdate(self):
	    self.assertEqual(updateDB(), True)

    def testPrint(self):
        self.assertEqual(printDB(), True)

    def testList(self):
	    self.assertEqual(getList(), True)

    def testValidCurr(self):
        self.assertEqual(checkValidCurrency('usd'), True)
        self.assertEqual(checkValidCurrency('usd213132'), False)
        self.assertEqual(checkValidCurrency('USD'), True)
        self.assertEqual(checkValidCurrency('uSd'), True)

    def testBaseExchange(self):
	    url = 'https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/eur/jpy.json'
	    r = requests.get(url).json()['jpy']
	    self.assertEqual(base_exchange('eur','jpy'),r)


if __name__ == '__main__':
    unittest.main()
