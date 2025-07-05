"""
    Convenient short-hand scripts for various complicated, but commonly-used ffmpeg commands
    Copyright (C) 2025  Kevin Tyrrell

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import unittest

from src.wrapper.input_builder import InputBuilder as Builder


class TestFfmpegInputWrapper(unittest.TestCase):
    __TEST_PATH = "C:/users/admin/desktop/input.mp4"

    def setUp(self):
        self.builder = Builder(self.__TEST_PATH)

    def test_input_1(self):
        b: Builder = self.builder
        b.seek(5)
        self.assertEqual(b.build(), f"-ss 5 -i {self.__TEST_PATH}")

    def test_input_2(self):
        b: Builder = self.builder
        b.loop().offset(10.2)
        self.assertEqual(b.build(), f"-stream_loop  -itsoffset 10.2 -i {self.__TEST_PATH}")


if __name__ == '__main__':
    unittest.main()
