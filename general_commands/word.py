def word(t):
  a='\n'
  for i in range (len(t)):
      a+=t[:i+1:] +'\n'
  return '```'+a+'```'