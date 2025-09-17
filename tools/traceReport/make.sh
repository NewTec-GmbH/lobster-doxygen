#!/bin/bash

# BSD 3-Clause License
#
# Copyright (c) 2025, NewTec GmbH
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#
# 3. Neither the name of the copyright holder nor the names of its
#    contributors may be used to endorse or promote products derived from
#    this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

LOBSTER_TRLC=lobster-trlc
LOBSTER_PYTHON=lobster-python
LOBSTER_REPORT=lobster-report
LOBSTER_RENDERER=lobster-html-report
OUT_DIR=out
SW_REQ_LOBSTER_CONF=./lobster-trlc-sw-req.yaml
SW_REQ_LOBSTER_OUT=$OUT_DIR/sw_req-lobster.json
SW_CONSTRAINT_LOBSTER_CONF=./lobster-trlc-sw-constraint.yaml
SW_CONSTRAINT_LOBSTER_OUT=$OUT_DIR/sw_constraint-lobster.json
SW_ARCH_LOBSTER_CONF=./lobster-trlc-sw-arch.yaml
SW_ARCH_LOBSTER_OUT=$OUT_DIR/sw_arch-lobster.json
SW_TEST_LOBSTER_CONF=./lobster-trlc-sw-test.yaml
SW_TEST_LOBSTER_OUT=$OUT_DIR/sw_test-lobster.json
SW_TESTRESULT_LOBSTER_CONF=./lobster-trlc-sw-test-result.yaml
SW_TESTRESULT_LOBSTER_OUT=$OUT_DIR/sw_test_result-lobster.json
SW_CODE_SOURCES=./../../src/lobster_doxygen
SW_CODE_LOBSTER_OUT=$OUT_DIR/sw_code-lobster.json
SW_TEST_CODE_SOURCES=./../../tests
SW_TEST_CODE_LOBSTER_OUT=$OUT_DIR/sw_test_code-lobster.json
SW_REQ_LOBSTER_REPORT_CONF=./lobster-report-sw-req.conf
SW_REQ_LOBSTER_REPORT_OUT=$OUT_DIR/lobster-report-sw-req-lobster.json
SW_REQ_LOBSTER_HTML_OUT=$OUT_DIR/sw_req_tracing_online_report.html

pushd ../testReport
chmod +x make_rst.sh
. ./make_rst.sh
popd

if [ ! -d "$OUT_DIR" ]; then
    mkdir -p "$OUT_DIR"
else
    rm -rf "$OUT_DIR"/*
fi

# ********** SW-Requirements **********
$LOBSTER_TRLC --config "$SW_REQ_LOBSTER_CONF" --out "$SW_REQ_LOBSTER_OUT"

if [ $? -ne 0 ]; then
    exit 1
fi
$LOBSTER_TRLC --config "$SW_CONSTRAINT_LOBSTER_CONF" --out "$SW_CONSTRAINT_LOBSTER_OUT"

if [ $? -ne 0 ]; then
    exit 1
fi
# ********** SW-Arch **********
$LOBSTER_TRLC --config "$SW_ARCH_LOBSTER_CONF" --out "$SW_ARCH_LOBSTER_OUT"

if [ $? -ne 0 ]; then
    exit 1
fi

# ********** SW-Test **********
$LOBSTER_TRLC --config "$SW_TEST_LOBSTER_CONF" --out "$SW_TEST_LOBSTER_OUT"

if [ $? -ne 0 ]; then
    exit 1
fi

# ********** SW-Test Result **********
$LOBSTER_TRLC --config $SW_TESTRESULT_LOBSTER_CONF --out $SW_TESTRESULT_LOBSTER_OUT

if [ $? -ne 0 ]; then
    exit 1
fi

# ********** SW-Code **********
$LOBSTER_PYTHON --out "$SW_CODE_LOBSTER_OUT" "$SW_CODE_SOURCES"

if [ $? -ne 0 ]; then
    exit 1
fi

# ********** SW-Test Code **********
$LOBSTER_PYTHON --out $SW_TEST_CODE_LOBSTER_OUT $SW_TEST_CODE_SOURCES

if [ $? -ne 0 ]; then
    exit 1
fi

# ********** Combine all lobster intermediate files **********
$LOBSTER_REPORT --lobster-config "$SW_REQ_LOBSTER_REPORT_CONF" --out "$SW_REQ_LOBSTER_REPORT_OUT"

if [ $? -ne 0 ]; then
    exit 1
fi

# ********** Create trace report **********
$LOBSTER_RENDERER --out "$SW_REQ_LOBSTER_HTML_OUT" "$SW_REQ_LOBSTER_REPORT_OUT"

if [ $? -ne 0 ]; then
    exit 1
fi
