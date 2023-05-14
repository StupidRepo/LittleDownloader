# Little Downloader
Yeah... I don't know what to put here.
## Description
Little Downloader is a simple downloader for downloading files from the internet.
It is written in [Python](https://python.org) and uses the [`requests`](https://requests.readthedocs.io/en/master/) library.
## Installing
### macOS + Windows + Linux
> **Note**: For pre-compiled macOS builds (a.k.a the builds linked below for macOS), you will need to open `Terminal.app` and run `chmod +x /path/to/LittleDownloader` to make the file executable. (e.g. if the file is in your Downloads folder, you will need to run `chmod +x ~/Downloads/LittleDownloader/LittleDownloader`)

Latest stable build:
- [macOS][macs]
- [Windows][wins]
- [GNU/Linux][lins]
- [All][alls]

Latest unstable build:
- [macOS][macu]
- [Windows][winu]
- [GNU/Linux][linu]
- [All][allu]

> **Warning**: The unstable builds may be unstable, and may not work properly.

The executable is `LittleDownloader` (the file without the file extenstion) for macOS, `LittleDownloader` (the file without the file extentsion) for GNU/Linux or `LittleDownloader.exe` for Windows.
## Building
### macOS + Windows + Linux
1. Run `git clone https://github.com/StupidRepo/LittleDownloader` in a Terminal or Command Prompt window.
2. Run `python3 -m pip install -r requirements.txt`
3. Run `python3 build.py`
4. The executable will be in the `dist` folder.
## Contributing
I need to make this less ugly, and faster so please contribute if you can :3
You can contribute by making forking this repo, making your changes and then making a pull request.
## Credits/Contributors
- Bradlee Barnes ([StupidRepo][bb-sr])
## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE.md) file for more information.

[macu]: https://nightly.link/StupidRepo/LittleDownloader/workflows/main/main/macOS.zip
[macs]: https://github.com/StupidRepo/LittleDownloader/releases/latest/download/macOS.zip

[winu]: https://nightly.link/StupidRepo/LittleDownloader/workflows/main/main/Windows.zip
[wins]: https://github.com/StupidRepo/LittleDownloader/releases/latest/download/Windows.zip

[linu]: https://nightly.link/StupidRepo/LittleDownloader/workflows/main/main/Linux.zip
[lins]: https://github.com/StupidRepo/LittleDownloader/releases/latest/download/Linux.zip

[allu]: https://nightly.link/StupidRepo/LittleDownloader/workflows/main/main
[alls]: https://github.com/StupidRepo/LittleDownloader/releases/latest

[bb-sr]: https://github.com/StupidRepo/