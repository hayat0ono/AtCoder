@echo off
cd %1
oj test -c "python %2" -t 2 | find "[FAILURE]" > nul
if %errorlevel% equ 0 (
    echo "Test failed, submission aborted."
    exit /b 1
)
oj submit %2 -l 5078
