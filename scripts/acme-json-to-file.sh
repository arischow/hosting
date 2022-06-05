#!/usr/bin/env bash

set -e

FILE=$1
DEST_DIR=/home/arischow/data/traefik/secrets/generated

mkdir -p $DEST_DIR && cd $DEST_DIR

while read -r a b c; do
  echo "$b" | base64 -d > "$a".cert;
  echo "$c" | base64 -d > "$a".key;
done < <(jq -r '.cloudflareresolver.Certificates[] |
                select(.domain.main | IN("arisc.how", "arischow.org")) |
                { domain: .domain.main, cert: .certificate, key: .key} |
                join(" ")' "$FILE")
