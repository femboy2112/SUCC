import unittest,json,sys
files=json.load(open("/home/leah/succ-main-xxii-evidence/focused-files.json"))
s=unittest.TestSuite(unittest.defaultTestLoader.discover("tests",pattern=p.rsplit("/",1)[-1]) for p in files)
r=unittest.TextTestRunner(verbosity=2).run(s)
sys.exit(not r.wasSuccessful())
