# Converts unity.py to unity.exe
from cx_Freeze import setup, Executable

setup( name = "Unit Converter" , version = "0.1" , description = "Unit Converter for Python" , executables = [Executable("unity.py")]  )
