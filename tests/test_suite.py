import unittest
from..........required packages
from ......

tc1 =unittest.TestLoader().loadTestsFromTestCase(test1)
tc2 =unittest.TestLoader().loadTestsFromTestCase(test2)

smokeTest = unittest.TestSuite([tc1,tc2])
unittest.TextTestRunner(verbosity=2),run(smokeTest)



#    running ...........................
