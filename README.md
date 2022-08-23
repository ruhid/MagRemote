# MagPy_UI

This simple UI is created for our projects in Transcranial magnetic stimulation (TMS) laborotory,  and used to control over the serial Magstim TMS device based on original work of [MagPy by nicolasmcnair](https://github.com/nicolasmcnair/magpy) which helped a lot for saving time required for study time.

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

- ARM: arms coils <br/>
- FIRE: fires TMS stimulus. It is for control purposes only, but may be for simultaneous EMG recording trigger out of Magstim devices can be used. Needs to be tested.   <br/>
- SYNCRONISE: syncronises settings between device and program <br/>
- SET: this button is redundant, al the parameters is setted on the go <br/>

LCD numbers show feedback from device Coil status. 

## Issues
 
 
- Sometimes serial connection can drop and it freezes UI, may be it is related to my serial devices <br/>
- Disconnection doesn't  work properly <br/>
- Not tested on Linux <br/>


