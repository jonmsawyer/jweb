#!/bin/bash

find . -name '*.pyc' -print0 | xargs -n1 -0 rm -f
