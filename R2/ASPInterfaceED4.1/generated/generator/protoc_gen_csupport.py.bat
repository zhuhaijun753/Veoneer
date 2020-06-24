@echo off
set mydir=%~dp0
python3 "%mydir%\protoc_gen_csupport.py"
