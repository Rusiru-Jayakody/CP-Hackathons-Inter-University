emirps = []

def primes():
    sieve = [True] * 1001 
    sieve[0] = sieve[1] = False
    for i in range(2,int(1000**0.5)+1):
        if sieve[i]:
            for j in range(i*i,1001,i):
                sieve[j] = False
    return sieve 

def is_emirp(prims):
    for i in range(2,1001):
        if prims[i]:
            rev = int(str(i)[::-1]) 
            if prims[rev] and rev != i:
                emirps.append(i)  
    
prims = primes()
is_emirp(prims)
# print("\n".join(map(str,emirps)))
print(emirps)



#This problem asks the shortest code for this.so upto now I got the following lin eof code as the shortest code using RUBY.
# require'prime';Prime.each(999){|n|r=n.to_s.reverse.to_i;puts n if n!=r&&r.prime?}