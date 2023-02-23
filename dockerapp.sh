#!/bin/bash
# ------------------------------------------------------------------
# [diggyblock] dockerapp
#   Shell Script to start or stop our containers
# ------------------------------------------------------------------

VERSION=1.0
USAGE="Usage: ./dockerapp [up,down]"

if [ $# == 0 ] ; then
    echo $USAGE
    exit 1;
elif [ $1 == 'up' ] ; then
    docker compose up &
elif [ $1 == 'down' ] ; then
    docker compose down &
else
    echo $USAGE
    exit 1;
fi