def arithmetic_arranger(problemas,resultado=False):
    

    if len(problemas)>5:
        return "Error: Too many problems."
    lista=[] 
    
    for p in problemas:
        
        [x,operacion,y]=p.split()
            
        if operacion !='+' and operacion!="-":
            return "Error: Operator must be '+' or '-'."
            
        if len(x)>4 or len(y)>4:
            return "Error: Numbers cannot be more than four digits."
        
        try:
            x=int(x)
            y=int(y)
        except ValueError:
            return "Error: Numbers must only contain digits."
                
        x=str(x)
        y=str(y)       
        lista.append(helper(x,operacion,y,resultado))
           
    esto=lista[0]
    espacios=" "*4
    
    for p in lista[1:]:
       for i in range(0,len(esto)):
           esto[i]+=espacios+p[i]
         
    if not resultado:
        esto=esto[0:3]
    return'\n'.join(esto)


def helper(x,operacion,y,resultado):
    a=int(x)
    b=int(y)
    res=a+b if operacion=="+" else a-b

    res=str(res)
    
    n=max([len(x),len(y)])
    n+=2 
    algo=[x.rjust(n),operacion+" "+y.rjust(n-2),'-'*(n)]
    if resultado:
        algo.append(res.rjust(n))
    return algo
