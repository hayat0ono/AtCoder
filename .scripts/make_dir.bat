@echo off
set problemNo=%1
set category=%problemNo:~0,3%

if "%category%"=="abc" (
    mkdir src\abc\%problemNo%
    copy .template\abc\*.py src\abc\%problemNo%
) else if "%category%"=="arc" (
    mkdir src\arc\%problemNo%
    copy .template\arc\*.py src\arc\%problemNo%
) else if "%category%"=="agc" (
    mkdir src\agc\%problemNo%
    copy .template\agc\*.py src\agc\%problemNo%
) else if "%category%"=="ahc" (
    mkdir src\ahc\%problemNo%
    copy .template\ahc\*.py src\ahc\%problemNo%
) else (
    echo Invalid category: %category%
    exit /b 1
)