# ffmpeg-scripts
> Convenient short-hand scripts for various complicated, but commonly-used ffmpeg commands

<!---
[![NPM Version][npm-image]][npm-url]
[![Build Status][travis-image]][travis-url]
[![Downloads Stats][npm-downloads]][npm-url]
--->

This is a repository for any scripts I write in order to make my life easier when working with the program [ffmpeg](https://ffmpeg.org/). ffmpeg commands are often simple for quick & dirty jobs but complex and specific use-case commands can become unwieldy or tedious to re-type or re-research. Each script is listed below with its respective description and usage.

![](res/HeaderImage.png)
## ffmpeg-target

>###### Shorthand ffmpeg command for a two-pass encoding to target an approximate file size. Ideal for uploaded media which must meet tight file size constraints.

* Example: You have a 45 MB video file `my_mov.mp4` and wish to upload it to a file sharing website with an `8.0` MB limit
** **Command:** `. bin/ffmpeg-target.sh my_mov.mp4 7.95 my_smaller_mov.mp4`
** This will take `my_mov.mp4` and re-encode it attempting to get it as close to `7.95` MB as possible. `7.95` instead of `8.0` as to not accidentally meet or exceed the constraint
** See [Usage](#Usage) for more details on parameters

### Usage

OS X & Linux:

```sh
. bin/ffmpeg-target.sh
```

| **Parameter** | **Flag** | **Flag(Formal)** | **Sub-Parameter(s)** | **Default Value** | **Description**                                                                 |
|---------------|----------|------------------|----------------------|-------------------|---------------------------------------------------------------------------------|
| _input_       |          |                  | path [str]           |                   | Absolute file path to your input video file                                     |
| _file_size_   |          |                  | size [float]         |                   | Desired size of the output file, in megabytes                                   |
| _output_      |          |                  | output [str]         |                   | Absolute file path for your output video file                                   |
| _lib_         | -l       | --lib            | library [str]        | libx264           | Library to use for video encoding                                               |
| _alib_        | -a       | --alib           | library [str]        | aac               | Library to use for audio encoding                                               |
| _abr_         | -b       | --abr            | bitrate [int]        | 128               | Average audio encoding bitrate, in kilobits per second                          |
| _threads_     | -t       | --threads        | threads [int]        | 0*                | Number of worker threads for the encoding process (0 for auto-detect CPU cores) |
| _yes_         | -y       | --yes            |                      | false             | Overwrite output file if file already exists in the output path                 |
| _preset_      | -p       | --preset         | preset [str]         | medium            | Amount of time taken by ffmpeg to optimize quality per frame (see help)         |
| _help_        | -h       |                  |                      |                   | Displays the help menu, provided by Python's Argparse Library                   |

<!--
## Development setup

Describe how to install all development dependencies and how to run an automated test-suite of some kind. Potentially do this for multiple platforms.

```sh
make install
npm test
```
-->

## Meta

Kevin Tyrrell – [KevinTearUl@gmail.com](mailto:KevinTearUl@gmail.com)

Distributed under the GPL3 license. See ``LICENSE`` for more information.

[https://github.com/KevinTyrrell](https://github.com/KevinTyrrell/)

## Contributing

1. Fork it (<https://github.com/KevinTyrrell/ffmpeg-scripts>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

<!-- Markdown link & img dfn's
[npm-image]: https://img.shields.io/npm/v/datadog-metrics.svg?style=flat-square
[npm-url]: https://npmjs.org/package/datadog-metrics
[npm-downloads]: https://img.shields.io/npm/dm/datadog-metrics.svg?style=flat-square
[travis-image]: https://img.shields.io/travis/dbader/node-datadog-metrics/master.svg?style=flat-square
[travis-url]: https://travis-ci.org/dbader/node-datadog-metrics
[wiki]: https://github.com/yourname/yourproject/wiki
-->
