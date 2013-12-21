cd screenshots
mencoder mf://*.png -mf fps=25:type=png -ovc copy -oac copy -o ../output.avi
