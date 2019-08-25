# TriggEye

When looking at the webcam, [TriggEye](https://github.com/takjg/TriggEye) executes the given command.
![Overview](https://user-images.githubusercontent.com/34579033/63515725-755d7900-c526-11e9-9a2e-9c0453d8899d.png)
![Example](https://user-images.githubusercontent.com/34579033/63647905-ed17e780-c762-11e9-91fb-65433bc5499d.png)    

- Usage: `triggeye COMMAND_TO_BE_EXECUTED_WHEN_LOOKING_AT_THE_WEBCAM`
- Example: `triggeye say OK Google`
- Supported OS: Windows10, Mac, Linux

## Features

- High Performance: Detects gaze wherever you are in the room. ([Performance of TriggEye](https://scrapbox.io/smart-home/TriggEye%E3%81%AE%E6%80%A7%E8%83%BD%E8%A9%95%E4%BE%A1))
- Light Weight: Runs on a low-end computer with a regular webcam. ([System Requirements](https://scrapbox.io/smart-home/TriggEye%E3%81%AE%E6%9D%90%E6%96%99%E8%B2%BB))
- Secure: No internet connection required, so you don't have to worry about video leaking from your webcam.

## Installation 

### Prerequisites (Only for Windows10)

TriggEye requires [WSL](https://docs.microsoft.com/ja-jp/windows/wsl/about) (Windows subsystem for Linux). This allows it to be handled in the same way as Linux or Mac.

### Building

1. Clone the GitHub repository of TriggEye.
   ```
   % git clone https://github.com/takjg/TriggEye.git
   ```
1. Install [OpenFace](https://github.com/TadasBaltrusaitis/OpenFace) in the TriggEye directory. (See also [OpenFace License](https://github.com/TadasBaltrusaitis/OpenFace/blob/master/OpenFace-license.txt))
    - [Windows](https://github.com/TadasBaltrusaitis/OpenFace/wiki/Windows-Installation)
    - [Linux](https://github.com/TadasBaltrusaitis/OpenFace/wiki/Unix-Installation)
    - [Mac](https://github.com/TadasBaltrusaitis/OpenFace/wiki/Mac-installation)

### Operation Check

Connect a webcam to your computer and execute:
```
% cd PATH/TO/TriggEye
% ./triggeye echo OK
```
It is a success if `OK` is displayed every time you look at the webcam.

When failed:
- Use the option `-d` to specify the webcam device ID:
  ```
  ./triggeye -d 3 echo OK
  ```
- Use the options `-w` and `-h` to specify the width and height of the webcam resolution:
  ```
  .triggeye -w 640 -h 480 echo OK
  ```
- Make sure the path of OpenFace is directly under TriggEye

## Options

|    | Option                   | Unit        | Default |
|:---|:-------------------------|:------------|--------:|
| -d | camera ID                | id          |       0 |
| -w | camera width             | pixels      |    1920 |
| -h | camera height            | pixels      |    1080 |
| -i | minimum trigger interval | seconds     |     1.0 |
| -m | margin for error         | millimeters |     150 |

## Example

[Wake up a smart speaker without a wake word](https://qiita.com/takjg/items/afc6348ceed67868d41f)

- Mac
  ```
  % ./triggeye say OK Google
  ```
- Windows
  ```
  % ./triggeye ./say_win ok_google.wav
  ```
- Linux
  - See [How to play audio files on the command line](https://scrapbox.io/smart-home/%E9%9F%B3%E5%A3%B0%E3%81%AE%E5%86%8D%E7%94%9F%E3%82%B3%E3%83%9E%E3%83%B3%E3%83%89)

The sample audio files [ok_google.wav](https://github.com/takjg/TriggEye/blob/master/ok_google.wav) and [alexa.wav](https://github.com/takjg/TriggEye/blob/master/alexa.wav) were created by [Open JTalk](http://open-jtalk.sp.nitech.ac.jp/index.php).

## Mechanism and implementation

See [Mechanism and implementation of TriggEye](https://scrapbox.io/smart-home/TriggEye%E3%81%AE%E4%BB%95%E7%B5%84%E3%81%BF)

## License

Released under the [Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0)

Copyright (c) 2019 Tak Jaga
