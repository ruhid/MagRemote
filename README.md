# MagRemote
Remote Magstim device control UI over the serial based on [MagPy by nicolasmcnair](https://github.com/nicolasmcnair/magpy)

## Installation
Installation requires PyQt and MagPy with it dependecies

```python
git clone https://github.com/ruhid/MagRemote
python -m pip install './MagRemote'
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


