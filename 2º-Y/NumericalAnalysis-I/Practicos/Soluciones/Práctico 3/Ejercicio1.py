
def ilagrange(abscisa, imagen, x_list):
    px = []
    for x in x_list:
        sumatoria = 0
        j = 0
        for xi in abscisa:
            productoria = 1
            
            for xj in abscisa:
                if xj != xi:
                    productoria = productoria * ((x - xj)/(xi-xj))
            
            sumatoria = productoria*imagen[j] + sumatoria
            j+=1

        px.append(sumatoria)

    return px

abscisa = [2, 3, 5]
imagen = [4, 9, 25] #En este caso sería la función cuadrática
x_list =[4]

print(ilagrange(abscisa, imagen, x_list))