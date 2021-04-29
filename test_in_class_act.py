import unittest
import in_class_act

class TestCase(unittest.TestCase):
    
    def test_add_1(self):
        self.assertEqual(in_class_act.add(4,2), 6)
    
    def test_add_2(self):
        self.assertEqual(in_class_act.add(4,2), 5)

    def test_sub(self):
        self.assertEqual(in_class_act.sub(7, 4), 3)

    def test_mul(self):
        self.assertEqual(in_class_act.mul(3, 2), 6)
    
    def test_div_1(self):
        self.assertEqual(in_class_act.div(18, 9), 2)

    def test_div_2(self):
        self.assertEqual(in_class_act.div(9,0), None)

if __name__ == '__main__':
    unittest.main(verbosity=2)