@echo off
title  calculator

:presenter
echo ===========
echo Wellcome to calculator
echo ===========
echo.

set /p x="Enter x:"
set /p y="Enter y:"

echo select option
echo press 1 for (+)
echo press 2 for (-)
echo press 3 for (*)
echo press 4 for (/)
echo press 5 for (22)
echo press 6 for exit
echo.

set /p operator=" select operation "


if %operator%==6 exit
if %operator%==1 goto add
if %operator%==2 goto sub
if %operator%==4 goto div
if %operator%==3 goto mul
if %operator%==5 goto hoch


:add
set /a result=%x% + %y%
echo.
echo result = %result%
goto presenter

:sub
set /a result=%x% - %y%
echo.
echo result = %result%
goto presenter

:mul
set /a result=%x% * %y%
echo.
echo result = %result%
goto presenter

:div
if %y% == 0 (
    echo You can't div by zero
    goto end
)
set /a result=%x% / %y%
echo.
echo result = %result%
goto presenter

:hoch
set /a result= %x% * %x%
set /a tesult= %y% * %y%
echo.
echo result x = %result%
echo result y = %tesult%
goto presenter



