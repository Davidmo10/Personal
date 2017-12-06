import unittest

import web.Tests.OldTests.TestGameMaker

# Classes to Test
game_maker_test = web.Tests.OldTests.TestGameMaker


def suite():
    my_suite = unittest.TestSuite()
    my_suite.addTest(unittest.makeSuite(game_maker_test.TestGameMaker))

    runner = unittest.TextTestRunner(verbosity=2)
    res = runner.run(my_suite)
    print(res)
    print('*'*25+'/n')


# run the suite
suite()

# Optional Code
# if __name__ == '__main__':
#     unittest.main()
