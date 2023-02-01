def funFibo(n):
   if n <= 1:
       return n
   else:
       return(funFibo(n-1) + funFibo(n-2))