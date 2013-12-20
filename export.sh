cd screenshots
mencoder mf://*.png -mf w=1366:h=768:fps=25:type=png -ovc lavc -lavcopts vcodec=mpeg4:mbd=2:trell -oac copy -o ../output.avi 
