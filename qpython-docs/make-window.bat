@echo off
set SPHINXBUILD=sphinx-build
set BUILDDIR=build
set ALLSPHINXOPTS=-d %BUILDDIR%/doctrees %SPHINXOPTS% source

if "%1" == "" goto help

if "%1" == "help" (
    goto help
)

if "%1" == "clean" (
    rmdir /s /q %BUILDDIR%
    goto end
)

%SPHINXBUILD% -b %1 %ALLSPHINXOPTS% %BUILDDIR%/%1
goto end

:help
echo Please use `make ^<target^>` where ^<target^> is one of
echo   html       to make standalone HTML files
echo   dirhtml    to make HTML files named index.html in directories
echo   singlehtml to make a single large HTML file
echo   latex      to make LaTeX files
echo   latexpdf   to make LaTeX files and run them through pdflatex
echo   linkcheck  to check all external links for integrity
echo   doctest    to run all doctests embedded in the documentation
echo   coverage   to run coverage check of the documentation
echo   dummy      to check syntax errors of document sources
goto end

:end