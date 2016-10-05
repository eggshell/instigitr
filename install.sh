#!/usr/bin/env bash

if [[ ! -d ${HOME}/bin ]]; then
    mkdir ${HOME}/bin
fi

ln -s ${PWD}/instigitr/instigitr.py ${HOME}/bin/instigitr
