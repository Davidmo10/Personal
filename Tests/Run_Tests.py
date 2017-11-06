import unittest
import Test_DBMock
import Test_Team
import Test_Game
import Test_Command
import Test_Landmark

suite = unittest.defaultTestLoader.loadTestsFromModule(Test_DBMock)
suite = unittest.defaultTestLoader.loadTestsFromModule(Test_Landmark)
suite = unittest.defaultTestLoader.loadTestsFromModule(Test_Team)
suite = unittest.defaultTestLoader.loadTestsFromModule(Test_Game)
suite = unittest.defaultTestLoader.loadTestsFromModule(Test_Command)
res = unittest.TextTestRunner(verbosity=0).run(suite)
print('\n', '*'*25, '\n')
print(res)
print('\n', '*'*25, '\n')
