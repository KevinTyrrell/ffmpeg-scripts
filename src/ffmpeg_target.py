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


from argparse import ArgumentParser

from arg_wash import ArgWash


def main():
    args = ArgumentParser(prog="ffmpeg-target",
                          description="Convenient short-hand scripts for various complicated, but commonly-used "
                                      "ffmpeg commands",
                          epilog="Shorthand ffmpeg command for a two-pass encoding to target an approximate file "
                                 "size. Ideal for uploaded media which must meet tight file size constraints.")
    # Required arguments
    args.add_argument("input", type=str, help="Absolute path to input media file to be re-encoded")
    args.add_argument("file_size", type=int, help="Output file size target, in mega-bytes")
    args.add_argument("output", type=str, help="File name/absolute file path of re-encoded file, including extension")
    # Optional arguments
    args.add_argument("-l", "--lib", dest="lib", type=str, default="libx264",
                      help="ffmpeg library to use for video encoding")
    args.add_argument("-a", "--alib", dest="alib", type=str, default="aac",
                      help="ffmpeg library to use for audio encoding")
    args.add_argument("-b", "--abr", dest="abr", type=int, default=128,
                      help="Average desired audio bit-rate used for encoding, in kilobits per second")
    args.add_argument("-t", "--threads", dest="threads", type=int, choices=range(1, 64), default=0,  # '0' => automatic
                      help="Number of threads to use for encoding, by default automatic to CPU core count")
    args.add_argument("-y", "--yes", dest="yes", action="store_true",
                      help="Proxy for ffmpeg -y, confirming yes to file overwriting")
    args = args.parse_args()

    wash = ArgWash(args)


if __name__ == '__main__':
    main()
