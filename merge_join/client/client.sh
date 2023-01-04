#!/usr/bin/bash

set -e

if [ -z "$1" ]; then
  echo "No argument URL found"
  exit 1
fi

URL="$1"
CERT_PATH="/tmp/cert.pem"

if [[ ${URL} == *"https"* ]]; then
  openssl s_client -showcerts -connect "${URL}":443 </dev/null 2>/dev/null | openssl x509 -outform PEM >/tmp/cert.pem
  if ! [ -x "$(command -v sgx-ra-verify)" ]; then
    echo 'Error: intel-sgx-ra is not installed (pip install intel-sgx-ra)'
    exit 1
  fi
  sgx-ra-verify certificate --path "${CERT_PATH}"
  export CURL_CA_BUNDLE="${CERT_PATH}"
fi

curl -X DELETE "${URL}"

csvs=("A.csv" "B.csv")

for csv in "${csvs[@]}"; do
  curl -F "file=@$(realpath data/"${csv}")" "${URL}"
done

curl "${URL}" -o "result.csv"
