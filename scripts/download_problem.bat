@echo off
set problemNo=%1
set category=%problemNo:~0,3%

if "%category%"=="abc" (
    mkdir abc\%problemNo%
    cd abc\%problemNo%
    oj-prepare https://atcoder.jp/contests/%problemNo%
) else if "%category%"=="arc" (
    mkdir arc\%problemNo%
    cd arc\%problemNo%
    oj-prepare https://atcoder.jp/contests/%problemNo%
) else if "%category%"=="agc" (
    mkdir agc\%problemNo%
    cd agc\%problemNo%
    oj-prepare https://atcoder.jp/contests/%problemNo%
) else if "%category%"=="ahc" (
    mkdir ahc\%problemNo%
    cd ahc\%problemNo%
    oj-prepare https://atcoder.jp/contests/%problemNo%
) else (
    echo Invalid category: %category%
    exit /b 1
)
