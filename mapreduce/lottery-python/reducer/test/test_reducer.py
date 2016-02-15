import unittest
from os import remove

from reducer.reducer import Reducer


class TestReducer(unittest.TestCase):
    _otos_min_expected_log = 'resources/otos.min.expected.txt'
    _otos_min_result_log = 'resources/otos.min.result.txt'
    _otos_min_result2_log = 'resources/otos.min.result2.txt'
    _otos_min_invalid_txt = 'resources/otos.min.invalid.txt'
    _otos_min_txt = 'resources/otos.min.txt'

    def setUp(self):
        self.test_subject = Reducer()

    def tearDown(self):
        self.test_subject = None

    def test_getNumber_with_valid_input(self):
        expected = 11
        actual = self.test_subject.getNumber('11\t1')
        self.assertEqual(expected, actual)

    def test_getNumber_with_invalid_input(self):
        expected = 0
        actual = self.test_subject.getNumber('')
        self.assertEqual(expected, actual)

    def test_processInput_with_valid_input(self):
        with open(self._otos_min_txt) as f:
            self._remove_logfile(self._otos_min_result_log)
            with open(self._otos_min_result_log, 'a') as r:
                self.test_subject.processInput(f.readlines(), r)
        with open(self._otos_min_expected_log) as f:
            expected = f.read().strip()
            with open(self._otos_min_result_log) as r:
                actual = r.read().strip()
        self.assertEqual(expected, actual)

    def test_processInput_with_invalid_input(self):
        with open(self._otos_min_invalid_txt) as f:
            self._remove_logfile(self._otos_min_result2_log)
            with open(self._otos_min_result2_log, 'a') as r:
                self.test_subject.processInput(f.readlines(), r)
        with open(self._otos_min_expected_log) as f:
            expected = f.read().strip()
            with open(self._otos_min_result2_log) as r:
                actual = r.read().strip()
        self.assertEqual(expected, actual)

    def _remove_logfile(self, filename):
        try:
            remove(filename)
        except Exception:
            pass
