from tests.utils import W3CTestCase


class TestVerticalAlign(W3CTestCase):
    vars().update(W3CTestCase.find_tests(__file__, "vertical-align-"))
