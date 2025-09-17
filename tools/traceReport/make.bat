@echo off
REM BSD 3-Clause License
REM
REM Copyright (c) 2025, NewTec GmbH
REM
REM Redistribution and use in source and binary forms, with or without
REM modification, are permitted provided that the following conditions are met:
REM
REM 1. Redistributions of source code must retain the above copyright notice, this
REM    list of conditions and the following disclaimer.
REM
REM 2. Redistributions in binary form must reproduce the above copyright notice,
REM    this list of conditions and the following disclaimer in the documentation
REM    and/or other materials provided with the distribution.
REM
REM 3. Neither the name of the copyright holder nor the names of its
REM    contributors may be used to endorse or promote products derived from
REM    this software without specific prior written permission.
REM
REM THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
REM AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
REM IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
REM DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
REM FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
REM DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
REM SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
REM CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
REM OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
REM OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

rem Keep all environment variables local to this script.
setlocal

pushd %~dp0

set LOBSTER_TRLC=lobster-trlc
set LOBSTER_PYTHON=lobster-python
set LOBSTER_REPORT=lobster-report
set LOBSTER_RENDERER=lobster-html-report
set OUT_DIR=out

set SW_REQ_LOBSTER_CONF=.\lobster-trlc-sw-req.yaml
set SW_REQ_LOBSTER_OUT=%OUT_DIR%\sw_req-lobster.json

set SW_CONSTRAINT_LOBSTER_CONF=.\lobster-trlc-sw-constraint.yaml
set SW_CONSTRAINT_LOBSTER_OUT=%OUT_DIR%\sw_constraint-lobster.json

set SW_ARCH_LOBSTER_CONF=.\lobster-trlc-sw-arch.yaml
set SW_ARCH_LOBSTER_OUT=%OUT_DIR%\sw_arch-lobster.json

set SW_TEST_LOBSTER_CONF=.\lobster-trlc-sw-test.yaml
set SW_TEST_LOBSTER_OUT=%OUT_DIR%\sw_test-lobster.json

set SW_TESTRESULT_LOBSTER_CONF=.\lobster-trlc-sw-test-result.yaml
set SW_TESTRESULT_LOBSTER_OUT=%OUT_DIR%\sw_test_result-lobster.json

set SW_CODE_SOURCES=.\..\..\src\lobster_doxygen
set SW_CODE_LOBSTER_OUT=%OUT_DIR%\sw_code-lobster.json

set SW_TEST_CODE_SOURCES=.\..\..\tests
set SW_TEST_CODE_LOBSTER_OUT=%OUT_DIR%\sw_test_code-lobster.json

set SW_REQ_LOBSTER_REPORT_CONF=.\lobster-report-sw-req.conf
set SW_REQ_LOBSTER_REPORT_OUT=%OUT_DIR%\lobster-report-sw-req-lobster.json

set SW_REQ_LOBSTER_HTML_OUT=%OUT_DIR%\sw_req_tracing_online_report.html

if not exist "%OUT_DIR%" (
    md %OUT_DIR%
) else (
    del /q /s "%OUT_DIR%\*" >nul
)

pushd ..\testReport
call make_rst.bat
popd

rem ********** SW-Requirements **********
%LOBSTER_TRLC% --config %SW_REQ_LOBSTER_CONF% --out %SW_REQ_LOBSTER_OUT%

if errorlevel 1 (
    goto error
)

%LOBSTER_TRLC% --config %SW_CONSTRAINT_LOBSTER_CONF% --out %SW_CONSTRAINT_LOBSTER_OUT%

if errorlevel 1 (
    goto error
)

rem ********** SW-Arch **********
%LOBSTER_TRLC% --config %SW_ARCH_LOBSTER_CONF% --out %SW_ARCH_LOBSTER_OUT%

if errorlevel 1 (
    goto error
)

rem ********** SW-Test **********
%LOBSTER_TRLC% --config %SW_TEST_LOBSTER_CONF% --out %SW_TEST_LOBSTER_OUT%

if errorlevel 1 (
    goto error
)

rem ********** SW-Test Result **********
%LOBSTER_TRLC% --config %SW_TESTRESULT_LOBSTER_CONF% --out %SW_TESTRESULT_LOBSTER_OUT%

if errorlevel 1 (
    goto error
)

rem ********** SW-Code **********
%LOBSTER_PYTHON% --out %SW_CODE_LOBSTER_OUT% %SW_CODE_SOURCES%

if errorlevel 1 (
    goto error
)

rem ********** SW-Test Code **********
%LOBSTER_PYTHON% --out %SW_TEST_CODE_LOBSTER_OUT% %SW_TEST_CODE_SOURCES%

if errorlevel 1 (
    goto error
)

rem ********** Combine all lobster intermediate files **********
%LOBSTER_REPORT% --lobster-config %SW_REQ_LOBSTER_REPORT_CONF% --out %SW_REQ_LOBSTER_REPORT_OUT%

if errorlevel 1 (
    goto error
)

rem ********** Create trace report **********
%LOBSTER_RENDERER% --out %SW_REQ_LOBSTER_HTML_OUT% %SW_REQ_LOBSTER_REPORT_OUT%

if errorlevel 1 (
    goto error
)

goto finished

:error

:finished

endlocal
popd