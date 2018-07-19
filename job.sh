#!/usr/env/bin bash

git clone https://github.com/greyspectrum/inception.git
cd inception
python mission.py
cd ..
rm -rf inception
