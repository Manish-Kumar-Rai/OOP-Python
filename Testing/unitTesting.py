#---------------- Unit Testing ----------------------
import unittest

def return_true():
    return "manish"

def return_false():
    return 0


# class CheckNumbers(unittest.TestCase):
#     def test_int_float(self):
#         self.assertEqual(1,1.0)

#     def test_str_int(self):
#         self.assertNotEqual("1",1)

#     def test_fun_return_true(self):
#         self.assertTrue(return_true())

#     def test_fun_return_false(self):
#         self.assertFalse(return_false())


def average(seq):
    return sum(seq) / len(seq)

# class TestAverage(unittest.TestCase):
#     def test_zero(self):
#         self.assertRaises(ZeroDivisionError,average,[])

#     def test_with_zero(self):
#         with self.assertRaises(ZeroDivisionError):
#             average([])


# class Mytest(unittest.TestCase):
#     def test_assert(self):
#         self.assertLess(8,9)
#         self.assertTupleEqual((1,2,3),(1,2,3))
#         self.assertListEqual([1,2,3],[2,1,3],msg="The order may not be the same.")
#         self.assertIn(8,[7,8,9])


if __name__ == "__main__":
    unittest.main()