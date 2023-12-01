sum([ (cs[0]-48)*10 + (cs[-1]-48)  for cs in [list(filter(  lambda x: x<64 , map(ord,l[:-1]))) for  l in open("input.txt").readlines()]])   

