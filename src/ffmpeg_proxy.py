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

"""
TODO: See: https://trac.ffmpeg.org/wiki/Encode/H.264#twopass
TODO: (200 MiB * 8388.608 [converts MiB to kBit; note: not 8192 as 1 kBit is always 1000 bit]) / 600 seconds = ~2796 kBit/s total bitrate
TODO: 2796 - 128 kBit/s (desired audio bitrate) = 2668 kBit/s video bitrate

TODO: Note 8388.608 appears to be a magic conversion number
"""