#!/bin/bash

MYDIR=$(dirname $0)

socat TCP-LISTEN:11020,fork,reuseaddr,bind=192.168.13.37 EXEC:$MYDIR/run.sh
