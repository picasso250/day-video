#!/bin/bash

cd screenshots
mencoder mf://*.png -mf fps=12:type=png -ovc copy -oac copy -o ../output.avi
