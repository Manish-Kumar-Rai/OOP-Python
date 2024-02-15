import unittest
import sys

class SkipTests(unittest.TestCase):

    @unittest.expectedFailure
    def test_fails(self):
        self.assertEqual(True,False)

    @unittest.skip("This test is useless.")
    def test_skip(self):
        self.assertEqual(True,False)

    @unittest.skipIf(sys.version_info.minor==11,"broken on 3.4")
    def test_skipIf(self):
        self.assertEqual(True,False)

    @unittest.skipUnless(sys.platform.startswith("linux"),"broken unless on linux")
    def test_skipUnless(self):
        self.assertEqual(True,False)


if __name__ == "__main__":
    unittest.main()