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
from ffmpeg_proxy import FFmpegProxy


def main():
    args = ArgumentParser(prog="ffmpeg-target",
                          description="Convenient short-hand scripts for various complicated, but commonly-used "
                                      "ffmpeg commands",
                          epilog="Shorthand ffmpeg command for a two-pass encoding to target an approximate file "
                                 "size. Ideal for uploaded media which must meet tight file size constraints.")
    # Required arguments
    args.add_argument("input", type=str, help="Absolute file path to your input video file")
    args.add_argument("file_size", type=float, help="Desired size of the output file, in megabytes")
    args.add_argument("output", type=str, help="Absolute file path for your output video file")
    # Optional arguments
    args.add_argument("-l", "--lib", dest="lib", type=str, default="libx264",
                      help="Library to use for video encoding")
    args.add_argument("-a", "--alib", dest="alib", type=str, default="aac",
                      help="Library to use for audio encoding")
    args.add_argument("-b", "--abr", dest="abr", type=int, default=128,
                      help="Average audio encoding bitrate, in kilobits per second")
    args.add_argument("-t", "--threads", dest="threads", choices=range(0, 64), type=int, default=0,  # '0' => automatic
                      help="Number of worker threads for the encoding process (0 for auto-detect CPU cores)")
    args.add_argument("-y", "--yes", dest="yes", action="store_true",
                      help="Overwrite output file if file already exists in the output path")
    args.add_argument("-p", "--preset", default="medium", help="Sets the speed preset for the encoding process",
                      choices=["veryslow", "slower", "slow", "medium", "fast",
                               "faster", "veryfast", "superfast", "ultrafast"])
    args = args.parse_args()

    wash = ArgWash(args)
    proxy = FFmpegProxy(wash)
    proxy.encode()


if __name__ == '__main__':
    main()
