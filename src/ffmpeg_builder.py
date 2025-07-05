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

from __future__ import annotations
from typing import Any, Optional
from abc import ABC, abstractmethod

class Buildable(ABC):
    @abstractmethod
    def build(self) -> Any:
        pass


class FfmpegBuilder(Buildable):
    pass

class InputBuilder(Buildable):
    __INPUT: str = "-i"
    __OFFSET: str = "-itsoffset"
    __DURATION: str = "-t"
    __SEEK: str = "-ss"
    __LOOP: str = "-stream_loop"

    def __init__(self, file_path: str) -> None:
        """
        :param file_path: Path or filename to the media file
        """
        self.__path: str = file_path
        self.__params: dict[str, Any] = dict()

    def build(self) -> str:
        return "{} {} {}".format(
            " ".join(f'{k} {v}' for k, v in self.__params.items()),
            self.__INPUT,
            self.__path)

    def offset(self, t: Optional[float]) -> InputBuilder:
        """
        :param t: Duration (+/-) to offset the stream by, or None to disable
        :return: Builder instance
        """
        if t is not None:
            self.__params[self.__OFFSET] = t
        else: del self.__params[self.__OFFSET]
        return self

    def duration(self, t: Optional[float | str]) -> InputBuilder:
        """
        :param t: Duration of the input to be read, or None to disable
        :return: Builder instance
        """
        if t is not None:
            self.__params[self.__DURATION] = t
        else: del self.__params[self.__DURATION]
        return self

    def seek(self, t: Optional[float | str]) -> InputBuilder:
        """
        :param t: Duration or timestamp to seek to, or None to disable
        :return: Builder instance
        """
        if t is not None:
            self.__params[self.__SEEK] = t
        else: del self.__params[self.__SEEK]
        return self

    def loop(self, toggle: bool) -> InputBuilder:
        """
        :param toggle: Loops the input if True, otherwise disabled
        :return: Builder instance
        """
        if toggle:
            self.__params[self.__LOOP] = ""
        else: del self.__params[self.__LOOP]
        return self
