@echo off

REM List of dependencies
SET "DEPENDENCIES=fltk wiringpi i2c-tools"

REM Check and install dependencies using Chocolatey
FOR %%G IN (%DEPENDENCIES%) DO (
    choco list --local-only | findstr /i "%%G" > nul
    IF %ERRORLEVEL% NEQ 0 (
        echo Installing %%G...
        choco install -y %%G
    ) ELSE (
        echo %%G is already installed.
    )
)

echo Dependencies installation complete.
