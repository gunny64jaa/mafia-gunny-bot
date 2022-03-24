def triangle(h):
  a='';h=int(h)
  a+=' '*(h-1)+'*\n' 
  for i in range(2,h):
    a+=' '*(h-i) +'*'+ ' '*(2*i-3)+'*\n' 
  a+='*'*(2*h-1)+'\n'
  return "```"+a+"```"