######################################################################
#
# File: test/test_base.py
#
# Copyright 2016 Backblaze Inc. All Rights Reserved.
#
# License https://www.backblaze.com/using_b2_code.html
#
######################################################################

from contextlib import contextmanager
import re
import unittest


class TestBase(unittest.TestCase):
    def assertIsNone(self, expr, msg=None):
        """Fail the test unless the expression is None."""
        if expr is not None:
            standardMsg = '%s is not None' % (repr(expr))
            assert False, msg or standardMsg

    @contextmanager
    def assertRaises(self, exc):
        try:
            yield
        except exc:
            pass
        else:
            assert False, 'should have thrown %s' % (exc,)

    @contextmanager
    def assertRaisesRegexp(self, expected_exception, expected_regexp):
        try:
            yield
        except expected_exception as e:
            if not re.search(expected_regexp, str(e)):
                assert False, "expected message '%s', but got '%s'" % (expected_regexp, str(e))
        else:
            assert False, 'should have thrown %s' % (expected_exception,)
