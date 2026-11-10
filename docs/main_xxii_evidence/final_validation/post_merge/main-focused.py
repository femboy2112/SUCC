import unittest,sys
names=['test_haar_successor_junction.py','test_haar_pascal_successor.py','test_bbp_parity_pressure.py','test_bbp_parity_holdout_512.py','test_aphex_haar_feedback.py','test_aphex_two_fiber_haar.py','test_branch_inventory.py']
s=unittest.TestSuite(unittest.defaultTestLoader.discover('tests',pattern=n) for n in names)
r=unittest.TextTestRunner(verbosity=2).run(s);sys.exit(not r.wasSuccessful())
