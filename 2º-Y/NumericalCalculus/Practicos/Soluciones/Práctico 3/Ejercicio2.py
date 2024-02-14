def inewton(abscisa, imagen1, xlist):
    
    def dif_divididas(abscisa, c_dif_divididas):
        n = len(abscisa)
        coefs = []
        #Genero las filas de los coeficientes
        for i in range(n):
            coefs.append(c_dif_divididas[:n-i].copy()) #.copy() lo puse porq era un error "ingenieril" segun el profe
        #Se calculan los coeficientes
        for i in range(1, n):
            for j in range(n-i):
                coefs[i][j] = (coefs[i-1][j+1] - coefs[i-1][j]) / (abscisa[j+i] - abscisa[j])

        c = [x[0] for x in coefs]
        return c 
    
    imagen = dif_divididas(abscisa, imagen1)
    
    px = []
    
    for x in xlist:
        sumatoria = 0

        for i in range(len(abscisa)):
            productoria = 1

            for j in range(i):
                productoria = productoria * (x - abscisa[j])
            
            sumatoria = sumatoria + imagen[i] * productoria
        
        px.append(sumatoria)
    return px




abscisa = [2, 3, 5]
imagen1 = [4, 9, 25]
#En este caso sería la función cuadrática
x_list = [4, 12]

#print(inewton(abscisa, imagen1, x_list))