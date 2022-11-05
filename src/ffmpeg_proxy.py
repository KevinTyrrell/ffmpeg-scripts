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

from arg_wash import ArgWash

import subprocess
from distutils.spawn import find_executable
from os import system


class FFmpegProxy:
    def __init__(self, args: ArgWash):
        """
        Constructs an ffmpeg proxy instance

        :param args: Arguments provided by argparse
        """
        self.__input = args.input
        self.__output = args.output
        self.__lib = args.lib
        self.__alib = args.alib
        self.__yes = args.yes
        self.__abr = args.abr
        self.__threads = args.threads
        duration = FFmpegProxy.get_length(self.__input)
        print("duration", duration)
        self.__bitrate = FFmpegProxy.__calc_bitrate(args.file_size, duration, args.abr)

    def encode(self) -> None:
        if not find_executable("ffmpeg"):
            raise ModuleNotFoundError("Dependency 'ffprobe' was not found in your system PATH")

        """
        {0} => threads to use for encoding, otherwise empty string
        {1} => -y if 'yes' was entered, otherwise empty string
        {2} => input file path
        {3} => video encoding library
        {4} => output video average bitrate
        {5} => audio encoding library
        {6} => output audio average bitrate
        {7} => output file path
        """
        fmt = "ffmepg{0} {1}-i \"{2}\" -c:v {3} -b:v {4}k -pass 1 -an -f null /dev/null &&" \
              " ffmpeg{0} -i \"{2}\" -c:v {3} -b:v {4}k -pass 2 -c:a {5} -b:a {6}k \"{7}\""
        cmd = fmt.format(
            " -threads " + str(self.__threads) if self.__threads > 1 else "",  # hide if threads=1
            "-y " if self.__yes else "", self.__input, self.__lib,
            self.__bitrate, self.__alib, self.__abr, self.__output)
        system(cmd)  # start ffmpeg through a system call

    @staticmethod
    def __calc_bitrate(file_size: int, file_duration: float, abr: int) -> int:
        """
        Calculates the maximum encoding bitrate for a size-constrained file

        :param file_size: Size of the file, in MiB
        :param file_duration: Duration of the video file, in seconds
        :param abr: Audio bitrate, in kBit/s
        :return: Bitrate of the file, in kBit/s
        """
        # 8388.608 -> Conversion from MiB to kBit
        print("file size", file_size)
        print("file_size * 8388.608", file_size * 8388.608)

        return int(file_size * 8388.608 / file_duration - abr)

    @staticmethod
    def get_length(file_path: str) -> float:
        """
        Returns the duration of a video file, in seconds

        This function requires 'ffprobe' to be located in your PATH.
        This is usually included in your installation of FFmpeg.

        Code Source: https://stackoverflow.com/a/3844467

        :param file_path: Path to a video file
        :return: Duration of a video file, in seconds
        """
        if not find_executable("ffprobe"):
            raise ModuleNotFoundError("Dependency 'ffprobe' was not found in your system PATH")
        result = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                                 "-of", "default=noprint_wrappers=1:nokey=1", file_path],
                                stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        return float(result.stdout)


"""
TODO: See: https://trac.ffmpeg.org/wiki/Encode/H.264#twopass
TODO: (200 MiB * 8388.608 [converts MiB to kBit; note: not 8192 as 1 kBit is always 1000 bit]) / 600 seconds = ~2796 kBit/s total bitrate
TODO: 2796 - 128 kBit/s (desired audio bitrate) = 2668 kBit/s video bitrate

TODO: Note 8388.608 appears to be a magic conversion number
"""