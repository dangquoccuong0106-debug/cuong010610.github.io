# Battle Cats 
### Windows / MacOS

1. Install Python 3.9 or later if you don't already have it: <https://www.python.org/downloads/>

2. Open a terminal such as PowerShell or Command Prompt

3. Run the following command:

```powershell
py -m pip install bcsfe
```

4. If you get an error saying that `py` is not a recongnised command, then try:

```powershell
python -m pip install bcsfe
```

or

```powershell
python3 -m pip install bcsfe
```

5. If you get an error saying `No module named pip`, then run:

```powershell
py -m ensurepip --upgrade
```

Again change `py` for `python` or `python3` if needed. I won't mention this again, so just remember
the one which works at keep using that.

5. To run the editor, as long as Python is in your PATH, you should be able to run:

```powershell
bcsfe
```

6. If Python is not in your path you'll need to run:

```powershell
py -m bcsfe
```

If you are using Windows and you are still struggling, try watching this video [here](https://codeberg.org/fieryhenry/videos/media/branch/main/bcsfe_windows_help.webm).

7. To update the editor run:

```powershell
py -m pip install -U bcsfe
```

8. To uninstall the editor run:

```powershell
py -m pip uninstall bcsfe
```

### Linux

1. Install Python 3.9 or later using your system's package manager if you don't already have it

2. You might have to install pip seperately with a package called `python-pip` or something similar
or you can run the following command:

```sh
python3 -m ensurepip --upgrade
```

3. Depending on your distro you might not be able to install the editor directly using the system
pip and you might need to use pipx (python-pipx) or create a virtual environment manually.

4. Using pipx:

```sh
pipx install bcsfe
```

5. If `~/.local/bin/` is in your path you should be able to run the editor with the command:

```sh
bcsfe
```

6. You may also need to install `tk` with your system package manager to open the
file selection dialog. This package may be called `tk` or `python-tk` or `python3-tk`.

7. To update the editor if you are using pipx run:

```sh
pipx upgrade bcsfe
```

8. To uninstall the editor if you are using pipx run:

```sh
pipx uninstall bcsfe
```

If anyone wants to put the editor on the AUR or another package repo, feel free, I'll be happy to
help if needed.

### Android

You need to install a terminal emulator to be able to install and run Python packages.

[Termux](https://termux.dev/en/) is a good option and is what this tutorial will use.

1. Download Termux, you can either get it from [F-Droid](https://f-droid.org/), or the APK directly
from [GitHub](https://github.com/termux/termux-app?tab=readme-ov-file#github). DO NOT use the
Google Play Store version, as it does not fully work.

I recommend using F-Droid since it can update Termux for you (and it's just a better alternative
than using the Google Play Store).

On F-Droid Termux is called `Termux Terminal emulator with packages`

2. Once Termux is installed, open it and run the following commands:

```sh
termux-setup-storage
termux-change-repo
pkg update
pkg upgrade
pkg install python python-pip
```

When it asks for a mirror, it doesn't really matter which one you pick, the default single mirror
works fine.

3. Install the editor with the following command:

```sh
pip install bcsfe
```

Or if that doesn't work try:

```sh
python -m pip install bcsfe
```

4. Run the editor with the following command:

```sh
bcsfe
```

Or if that doesn't work try:

```sh
python -m bcsfe
```

Note that the editor might give you warnings about tkinter not being installed, you can just
ignore those as tkinter will not work on mobile. This just means that instead of a graphical file
selection dialog, you just have to type the file path manually.

For example to save your save file to your downloads directory, the path might look something like
`/storage/emulated/0/Download/SAVE_DATA` or `/sdcard/Download/SAVE_DATA`

5. To update the editor run:

```sh
pip install -U bcsfe
```

Or

```sh
python -m pip install -U bcsfe
```


5. To uninstall the editor run:

```sh
pip uninstall bcsfe
```

Or

```sh
python -m pip uninstall bcsfe
```

### iOS

I do not have an iOS device, so there is no tutorial. The video that was recommended is now outdated.
But for a general overview of what you need to do:

1. Download a-Shell from the App Store
2. Install the editor with:

```sh
pip install bcsfe
```

3. Run the editor with:

```sh
bcsfe
```

Or if that doesn't work try:

```sh
python -m bcsfe
```

Or 

```sh
python3 -m bcsfe
```

4. To update the editor run:

```sh
pip install -U bcsfe
```

5. To uninstall the editor run:

```sh
pip uninstall bcsfe
```
