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

from abc import ABC, abstractmethod
from typing import Any


class Buildable(ABC):
    @abstractmethod
    def build(self) -> Any:
        """
        Builds the buildable object

        This function should be non-terminating.
        Each call results in a newly built object.

        :return: Built object instance
        """
        pass
