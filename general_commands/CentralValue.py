def central(t):
  data=[float(i) for i in t.split(",")]
  return '```js\nResult\nmax: '+str(max(data))+'\n'+'min: '+str(min(data))+'\n'+'sort: '+str(sorted(data))[1:-1]+'\n'+\
    'sum: '+str(sum(data))+'\n'+ 'mean: '+str(sum(data)/len(data))  + '```'