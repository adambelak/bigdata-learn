import unittest
from os import remove

from mapper.mapper import Mapper


class TestMapper(unittest.TestCase):
    _example_as_row = '2016;5;2016.02.06.;0;0 Ft;30;1 910 065 Ft;2955;20 530 Ft;86050;1 370 Ft;11;15;26;39;78'
    _example_as_dict = [(11, 1), (15, 1), (26, 1), (39, 1), (78, 1)]
    _otos_min_expected_log = 'resources/otos.min.expected.txt'
    _otos_min_result_log = 'resources/otos.min.result.txt'
    _otos_min_csv = 'resources/otos.min.txt'

    def setUp(self):
        self.test_subject = Mapper()

    def tearDown(self):
        self.test_subject = None

    def test_getNumbers_with_valid_input(self):
        expected = self._example_as_dict
        actual = self.test_subject.getNumbers(self._example_as_row)
        self.assertEqual(expected, actual)

    def test_getNumbers_with_invalid_input(self):
        expected = []
        actual = self.test_subject.getNumbers('')
        self.assertEqual(expected, actual)

    def test_processInput_with_valid_input(self):
        with open(self._otos_min_csv) as f:
            self._remove_logfile(self._otos_min_result_log)
            with open(self._otos_min_result_log, 'a') as r:
                self.test_subject.processInput(f.readlines(), r)
        with open(self._otos_min_expected_log) as f:
            expected = f.read().strip()
            with open(self._otos_min_result_log) as r:
                actual = r.read().strip()
        self.assertEqual(expected, actual)

    def _remove_logfile(self, filename):
        try:
            remove(filename)
        except Exception:
            pass
