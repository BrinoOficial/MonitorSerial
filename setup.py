#setup.py
from cx_Freeze import setup, Executable
setup(
    name = "MonitorSerial",
    version = "0.1",
    options = {"build_exe":{
        'packages':["tkinter","serial","threading"],
        'include_msvcr':True,
    }},
    executables = [Executable("MonitorSerial.py", base = "Win32GUI")]
    )

