#!/bin/bash

LOBSTER_ONLINE_REPORT=lobster-online-report
LOBSTER_RENDERER=lobster-html-report
OUT_DIR=out

SW_REQ_LOBSTER_ONLINE_REPORT_CONF=$OUT_DIR/online_report_config.yaml
SW_REQ_LOBSTER_REPORT_OUT=$OUT_DIR/lobster-report-sw-req-lobster.json
SW_REQ_LOBSTER_ONLINE_REPORT_OUT=$OUT_DIR/lobster-online-report-sw-req-lobster.json

SW_REQ_LOBSTER_HTML_OUT=$OUT_DIR/sw_req_tracing_online_report.html


if [ ! -f "$OUT_DIR/$SW_REQ_LOBSTER_REPORT_OUT" ]; then
    echo "Error: Missing input report file $OUT_DIR/$SW_REQ_LOBSTER_REPORT_OUT"
    echo "call make.sh first to generate a local report for conversion to online report"
    exit 1
fi

# ********** Create online report configuration  **********
COMMIT_ID=$(git rev-parse HEAD)
BASE_URL=$(git remote get-url origin)
echo "report: '$SW_REQ_LOBSTER_REPORT_OUT'" > "$SW_REQ_LOBSTER_ONLINE_REPORT_CONF"
echo "commit_id: '$COMMIT_ID'" >> "$SW_REQ_LOBSTER_ONLINE_REPORT_CONF"
echo "repo_root: './../..'" >> "$SW_REQ_LOBSTER_ONLINE_REPORT_CONF"
echo "base_url: '$BASE_URL'" >> "$SW_REQ_LOBSTER_ONLINE_REPORT_CONF"

# ********** LOBSTER Report conversion to GIT URLS **********
$LOBSTER_ONLINE_REPORT --out $SW_REQ_LOBSTER_ONLINE_REPORT_OUT --config $SW_REQ_LOBSTER_ONLINE_REPORT_CONF
if [ $? -ne 0 ]; then
    exit 1
fi

# ********** Create trace report **********
$LOBSTER_RENDERER --out "$SW_REQ_LOBSTER_HTML_OUT" "$SW_REQ_LOBSTER_REPORT_OUT"

if [ $? -ne 0 ]; then
    exit 1
fi
