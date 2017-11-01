import unittest
import TEST_db_mock

suite = unittest.defaultTestLoader.loadTestsFromModule(TEST_db_mock)
res = unittest.TextTestRunner(verbosity=0).run(suite)
print(res)
print('*'*25+'/n')
