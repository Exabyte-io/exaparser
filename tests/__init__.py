import unittest
import numpy as np


class TestBase(unittest.TestCase):
    """
    Base class for ExaParser tests.
    """

    def setUp(self):
        super(TestBase, self).setUp()

    def tearDown(self):
        super(TestBase, self).tearDown()

    def assertDeepAlmostEqual(self, expected, actual, *args, **kwargs):
        """
        Asserts that two complex structures have almost equal contents. Compares lists, dicts and tuples recursively.
        Checks numeric values using assertAlmostEqual() and checks all other values with assertEqual(). Accepts
        additional positional and keyword arguments and passes those intact to assertAlmostEqual().

        Notes:
            Based on: http://stackoverflow.com/a/23550280

        Args:
            expected (dict|list|tuple): expected complex object.
            actual (dict|list|tuple): actual complex object.
        """
        is_root = '__trace' not in kwargs
        trace = kwargs.pop('__trace', 'ROOT')
        try:
            if isinstance(expected, (int, float, long, complex)):
                self.assertAlmostEqual(expected, actual, *args, **kwargs)
            elif isinstance(expected, (str)):
                self.assertEqual(expected, actual)
            elif isinstance(expected, (list, tuple, np.ndarray)):
                self.assertEqual(len(expected), len(actual))
                for index in xrange(len(expected)):
                    v1, v2 = expected[index], actual[index]
                    self.assertDeepAlmostEqual(v1, v2, __trace=repr(index), *args, **kwargs)
            elif isinstance(expected, dict):
                self.assertEqual(set(expected), set(actual))
                for key in expected:
                    self.assertDeepAlmostEqual(expected[key], actual[key], __trace=repr(key), *args, **kwargs)
        except AssertionError as exc:
            exc.__dict__.setdefault('traces', []).append(trace)
            if is_root:
                trace = ' -> '.join(reversed(exc.traces))
                exc = AssertionError("%s\nTRACE: %s" % (exc.message, trace))
            raise exc
