# Mendel's first law

'''Given: Three positive integers k, m, and n, representing 
   a population containing k+m+n organisms: k individuals are 
   homozygous dominant for a factor, m are heterozygous, 
   and n are homozygous recessive.'''

'''Return: The probability that two randomly selected mating 
   organisms will produce an individual possessing a dominant 
   allele (and thus displaying the dominant phenotype). Assume 
   that any two organisms can mate.'''

# k the number of homozygous dominant individuals
AA = 20.0
# m the number of heterozygous individuals
Aa = 23.0
# n the number of homozygous recessive individuals
aa = 29.0

pop = AA + Aa + aa
npop = pop - 1.0

option1 = (Aa / pop) * ((Aa - 1) / npop) * 0.25
option2 = (Aa / pop) * (aa / npop) * 0.50
option3 = (aa / pop) * (Aa / npop) * 0.50
option4 = (aa / pop) * ((aa - 1) / npop)

a =  option1 + option2 + option3 + option4
print 1-a


