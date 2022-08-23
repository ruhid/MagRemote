# MagPy_GUI

This simple UI is created for our projects in Transcranial magnetic stimulation (TMS) laborotory,  and used to control over the serial Magstim TMS device based on original work of [MagPy by nicolasmcnair](https://github.com/nicolasmcnair/magpy) which helped a lot to save time required for one study.

## Installation
Installation requires PyQt and MagPy with it dependecies

```python
git clone https://github.com/ruhid/MagPy_UI
python -m pip install './MagPy_UI'
```
If some error happens, installation of pyserial and PyQt5 for your system will be enough 

Tested on Windows and MacOS Monterey(Installing PyQt5 on apple silicon can be a bit tricky, but possible. Follow online instructions)


## Using
Run run_magremote.py file, choose serial port for magstim devices, wait cuple of seconds for connection. 

![Screenshot](MagRemote.png)

ARM: arms coils <br/>
FIRE: fires <br/>
SYNCRONISE: syncronises settings between device and program <br/>

LCD numbers show feedback from device
Coil temperature gages are available to monitor device temperature status

