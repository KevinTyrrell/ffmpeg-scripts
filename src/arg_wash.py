"""
    Convenient short-hand scripts for various complicated, but commonly-used ffmpeg commands
    Copyright (C) 2022  Kevin Tyrrell

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

from __future__ import annotations

from typing import Any
from os.path import exists, isfile, getsize
from argparse import Namespace
from re import search
from os import cpu_count


class ArgWash:

    def __init__(self, args: Namespace) -> None:
        """
        Constructs an Argument Washer, ensuring provided arguments are prepared for use

        Argument List:
        * [str] input: must be a valid path to an existing file
        * [int] file_size: must be less than the current file size of the input file
        * [str] output: must be a valid path and contain a file extension
        * [str] lib: must not be an empty string
        * [str] alib: must not be an empty string
        * [int] abr: must be positive
        * [int] threads: must be positive, LTE to number of cores for the system, '0' => auto detect
        * [bool] yes: no wash

        :param args: Arguments provided by argparse
        """

        for washer in [  # Error check all user inputs
            ArgWash.__InputWasher(args, args.input),
            ArgWash.__FileSizeWasher(args, args.file_size),
            ArgWash.__OutputWasher(args, args.output),
            ArgWash.__ABRWasher(args, args.abr),
            ArgWash.__ThreadWasher(args, args.threads)
        ]:
            washer.wash()

    class __ArgWasher:  # Interface
        def __init__(self, args: Namespace, value: Any):
            """
            Constructs a primitive Argument Washer, washing one particular instance variable

            :param args: Arguments provided to the washer
            :param value: Value being checked by the washer
            """
            self._args = args
            self._value = value

        def wash(self) -> None:
            if not self._wash():
                raise ValueError("{}: {}".format(self._get_exc(), self._value))

        def _get_exc(self) -> str:
            """
            :return: Exception reason in which this washer is capable of raising
            """
            pass

        def _wash(self) -> bool:
            """
            :return: True if the value associated with the key is appropriate and ready to be used
            """
            pass

    class __InputWasher(__ArgWasher):
        def _get_exc(self) -> str:
            return "Input file must be a valid path to an existing file"

        def _wash(self) -> bool:
            return exists(self._value) and isfile(self._value)

    class __FileSizeWasher(__ArgWasher):
        def _get_exc(self) -> str:
            return "File size must be less than the input's file size"

        def _wash(self) -> bool:
            return getsize(self._args.input) / 1048576 < self._value  # Convert Bytes -> MB

    class __OutputWasher(__ArgWasher):
        def _get_exc(self) -> str:
            return "Output file must be a valid path and contain a file name with extension"

        def _wash(self) -> bool:
            match = search("(.+)[\\\\/].+\\..+", self._value)  # Split path from filename and check for ext
            return match is not None and exists(match.group(1))

    class __ABRWasher(__ArgWasher):
        def _get_exc(self) -> str:
            return "Bitrate must be a positive integer"

        def _wash(self) -> bool:
            return self._value > 0

    class __ThreadWasher(__ArgWasher):
        def _get_exc(self) -> str:
            return "Thread count must be positive and cannot exceed number of available CPU cores"

        def _wash(self) -> bool:
            cores = cpu_count()
            if self._value == 0:  # Automatic mode: set to number of cores
                self._args.threads = cores
                return True
            return 1 <= self._value <= cores
