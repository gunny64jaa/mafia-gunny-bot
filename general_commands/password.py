def t1(t):
    if len(t)>=8:return True ,''
    else:return False ,'Less than 8 characters'
    
def t2(t):
    mode=[];b=0;s=0;n=0;l=0;al='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    als=al.lower();aln='0123456789';ay='\'\"\\{}[]><,./ZX*=+!@#$%^&*_-;:'
    for e in t:
        if e in al :b+=1
        elif e in als:s+=1
        elif e in aln:n+=1
        elif e in ay:l+=1
    if s==0:mode.append('No lowercase letters')    
    if b==0:mode.append('No uppercase letters')
    if n==0:mode.append('No numbers')
    if l==0:mode.append('No symbols')
    if mode != []:return False,mode
    else : return True ,''
    
def t3(t):
    for i in range(len(t)-3):
        if t[i]==t[i+1] and t[i]==t[i+2] and t[i]==t[i+3]:return False,'Character repetition'
    return True ,''

def t4(t):
    i=0
    while i!=len(t)-3:
        if t[i] in('0123456789') and t[i+1] in('0123456789') and t[i+2] in('0123456789') and t[i+3] in('0123456789'):
           a=int(t[i]);b=int(t[i+1]);c=int(t[i+2]);d=int(t[i+3])
           if (a+1)%10== b and (a+2)%10== c and (a+3)%10== d :return False,'Number sequence'
           elif (a-1)%10== b and (a-2)%10== c and (a-3)%10== d :return False,'Number sequence'
        i+=1
    return True ,''

def t5(t):
    alph='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    i=0
    while i!=len(t)-3:
        if t[i] in alph and t[i+1] in alph and t[i+2] in alph and t[i+3] in alph:
            a=t[i].lower();b=t[i+1].lower();c=t[i+2].lower();d=t[i+3].lower()
            if alph[alph.find(a)+1]==b and alph[alph.find(a)+2]==c and alph[alph.find(a)+3]==d:return False,'Letter sequence'
            elif alph[alph.find(a)-1]==b and alph[alph.find(a)-2]==c and alph[alph.find(a)-3]==d:return False,'Letter sequence'
        i+=1
    return True,''

def t6(t):        
    c1='!@#$%^&*()_+'
    c2='qwertyuiopQWERTYUIOP'
    c3='asdfghjklASDFGHJKL'
    c4='zxcvbnmZXCVBNM'
    i=0
    while i!=len(t)-3:
        if t[i] in c1 and t[i+1] in c1 and t[i+2] in c1 and t[i+3] in c1:
            a=t[i];b=t[i+1];c=t[i+2];d=t[i+3]
            if c1[c1.find(a)+1]==b and c1[c1.find(a)+2]==c and c1[c1.find(a)+3]==d:return False,'Keyboard pattern'
            elif c1[c1.find(a)-1]==b and c1[c1.find(a)-2]==c and c1[c1.find(a)-3]==d:return False,'Keyboard pattern'
        for j in range(3):
            if j==1:c2=c3
            elif j==2:c2=c4
            if t[i] in c2 and t[i+1] in c2 and t[i+2] in c2 and t[i+3] in c2:        
                a=t[i].lower();b=t[i+1].lower();c=t[i+2].lower();d=t[i+3].lower()
                if c2[c2.find(a)+1]==b and c2[c2.find(a)+2]==c and c2[c2.find(a)+3]==d:return False,'Keyboard pattern'
                elif c2[c2.find(a)-1]==b and c2[c2.find(a)-2]==c and c2[c2.find(a)-3]==d:return False,'Keyboard pattern'
        i+=1
    return True,''
def checkall(t):
    if t1(t)[0]and t2(t)[0]and t3(t)[0]and t4(t)[0]and t5(t)[0]and t6(t)[0]:
        return True
    
def passwordcheck(t):
  if checkall(t) == True:return 'OK'
  else:
      result=[]
      if not t1(t)[0]:result.append(t1(t)[1])
      if not t2(t)[0]:
          for e in t2(t)[1]:result.append(e)
      if not t3(t)[0]:result.append(t3(t)[1])
      if not t4(t)[0]:result.append(t4(t)[1])
      if not t5(t)[0]:result.append(t5(t)[1])
      if not t6(t)[0]:result.append(t6(t)[1]) 
      return ', '.join(result)