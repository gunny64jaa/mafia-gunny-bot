from molmass import Formula
def chem(t):
  f = Formula(t)
  a='Formula: '+f.formula
  b='Isotope mass: '+str(f.isotope.mass)
  return "```"+a+'\n'+b+'\n'+str(f.composition())+"```"