import unittest
from test_encryptThis import TestEncryptThis

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestEncryptThis)
    unittest.TextTestRunner(verbosity=2).run(suite)
