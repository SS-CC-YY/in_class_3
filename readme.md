in-class activity Unit testing

The outcome of these code should be:

$ py test_in_class_act.py
test_add_1 (__main__.TestCase) ... ok
test_add_2 (__main__.TestCase) ... FAIL
test_div_1 (__main__.TestCase) ... ok
test_div_2 (__main__.TestCase) ... ok
test_mul (__main__.TestCase) ... ok
test_sub (__main__.TestCase) ... ok

======================================================================
FAIL: test_add_2 (__main__.TestCase)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "D:\spring2021\cs362\inclassacitvity\in_class_3\test_in_class_act.py", line 10, in test_add_2
    self.assertEqual(in_class_act.add(4,2), 5)
AssertionError: 6 != 5

----------------------------------------------------------------------
Ran 6 tests in 0.002s

FAILED (failures=1)