import json

def main():
    with open('result.json', 'r') as myfile:
        data=myfile.read()

    obj = json.loads(data)

    totalConsultas = 0
    totalCertificados = 0
    totalSolicitudes = 0
    totalIncentivos = 0
    totalPersonas = 0
    mayor = 0
    menor = 0
    totalarr = []
    for i in range(5):

        totalConsultas += obj['Cluster {0}'.format(i)]['consultas']
        totalCertificados += obj['Cluster {0}'.format(i)]['certificados']
        totalSolicitudes += obj['Cluster {0}'.format(i)]['solicitudes']
        totalIncentivos += obj['Cluster {0}'.format(i)]['incentivos']
        totalPersonas += len(obj['Cluster {0}'.format(i)]['ips'])
        print("Personas Cluster {0}".format(i),len(obj['Cluster {0}'.format(i)]['ips']) )
        
    print("Datos Totales")
    print("Consultas = ", totalConsultas,"\nCertificados =",totalCertificados,"\nIncentivos =",totalIncentivos, 
        "\nSolicitudes  =",totalSolicitudes, "\nPersonas  =", totalPersonas, "\nMedia Personas", totalPersonas/5 )
    print("++++++++++++++++++++++++++++++++++++++++++++")

    clustNav = []
    for i in range(5):
        consultas = obj['Cluster {0}'.format(i)]['consultas']
        certificados  = obj['Cluster {0}'.format(i)]['certificados']
        solicitudes = obj['Cluster {0}'.format(i)]['solicitudes']
        incentivos = obj['Cluster {0}'.format(i)]['incentivos']
        total = consultas+certificados+solicitudes+incentivos
        clustNav.append({'consultas':"%.1f"%((consultas/total)*100),'certificados':"%.1f" %((certificados/total)*100), 'solicitudes':"%.1f" %((solicitudes/total)*100),
                         'incentivos':"%.1f"%((incentivos/total)*100)})
    
    print("clustnav", clustNav)
    for i in range(5):
        print("Cluster {0}".format(i))
        consul = (obj['Cluster {0}'.format(i)]['consultas']/ len(obj['Cluster {0}'.format(i)]['ips'])) - (totalConsultas/len(obj['Cluster {0}'.format(i)]['ips']))
        certi =  (obj['Cluster {0}'.format(i)]['certificados']/ len(obj['Cluster {0}'.format(i)]['ips'])) - (totalCertificados/len(obj['Cluster {0}'.format(i)]['ips']))
        soli =  (obj['Cluster {0}'.format(i)]['solicitudes']/ len(obj['Cluster {0}'.format(i)]['ips'])) - (totalSolicitudes/len(obj['Cluster {0}'.format(i)]['ips']))
        incentivos = (obj['Cluster {0}'.format(i)]['incentivos']/ len(obj['Cluster {0}'.format(i)]['ips'])) - (totalIncentivos/len(obj['Cluster {0}'.format(i)]['ips']))
        total = abs(consul)+ abs(certi)+ abs(soli)+abs(incentivos)
        #Se debe asociar el totalarr con el cluster
        totalarr.append(total/4)


        print("Dif Consultas = ", consul,"\nDif Certificados = ", certi, "\nDif Solicitudes = ", soli, "\nDif incentivos = ", incentivos,"\nDif Total = ", total/4)
        print("++++++++++++++++++++++++++++++++++++++++++++")
    print(" Total personas: ", totalPersonas/5 )
    por = []

    for i in range(5):
        por.append("%.1f" %((len(obj['Cluster {0}'.format(i)]['ips'])/totalPersonas)*100))
    #totalarr.sort(reverse=True)
    print("Por", por)
    print(totalarr)
    #Menor Motivacion: reconocimiento Tarea: Clasificacion
    #Mayor Motivacion: participacion Tarea: Puntos si supera la media -> totalPersonas/5 si no supera la media totalpersonas/20
    #luego Motivacion: conocimiento de objetivos Tarea: Desafios
    #luego Motivacion: crecimiento Tarea: Sistema de niveles
    #luego Motivacion: resultados Tarea: Desafios
    #luego Motivacion: recompensas Tarea Regalos

    part = False
    cono =False
    creci = False
    resul = False
    reco = False
    recom =False
    totalPersonas /= 5
    colors = ['red', 'yellow', 'green', 'blue' , 'prurple']
    result = []
    for i, x in enumerate(totalarr):

        
        if(x>totalPersonas   and not part):
            result.append({'Cluster':'Cluster {0}'.format(i), 'porsentaje':por[i], 'motivacion':'participacion', 'color':colors[i], 'nav':clustNav[i]})
            part =True
            print("Inserte aca cluster: {0}".format(i))
            print("Tipo de motivación: ", "Participación")
            print("Se recomienda usar este sistema de gamificación")
            print("Tareas a emplear: ", "Sistema de desafios donde se obtengan puntos." )
        elif(x>totalPersonas/4  and not cono):
            result.append({'Cluster':'Cluster {0}'.format(i), 'porsentaje':por[i], 'motivacion':'conocimiento', 'color':colors[i], 'nav':clustNav[i]})
            cono =True
            print("Inserte aca cluster: {0}".format(i))
            print("Tipo de motivación: ", "Conocimiento de objetivos")
            print("Se recomienda usar este sistema de gamificación")
            print("Tareas a emplear: ", "Sistema de Logros." )
        elif(x>totalPersonas/(4**2) and not creci):
            result.append({'Cluster':'Cluster {0}'.format(i), 'porsentaje':por[i], 'motivacion':'crecimiento', 'color':colors[i], 'nav':clustNav[i]})
            creci =True
            print("Inserte aca cluster: {0}".format(i))
            print("Tipo de motivación: ", "Crecimiento")
            print("Se recomienda usar este sistema de gamificación")
            print("Tareas a emplear: ", "Sistema de niveles al realizar tareas, desafios o logros." )
        elif(x>totalPersonas/(4**3)  and not resul):
            result.append({'Cluster':'Cluster {0}'.format(i), 'porsentaje':por[i], 'motivacion':'resultados', 'color':colors[i], 'nav':clustNav[i]})
            resul =True
            print("Inserte aca cluster: {0}".format(i))
            print("Tipo de motivación: ", "Resultados")
            print("Se recomienda usar este sistema de gamificación")
            print("Tareas a emplear: ", "Sistema de recoleccion de puntos." )
        
        
        elif(x>totalPersonas/(4**4)and not recom):
            result.append({'Cluster':'Cluster {0}'.format(i), 'porsentaje':por[i], 'motivacion':'recompenza', 'color':colors[i], 'nav':clustNav[i]})
            recom =True
            print("Inserte aca cluster: {0}".format(i))
            print("Tipo de motivación: ", "Recompenza")
            print("Se recomienda usar este sistema de gamificación")
            print("Tareas a emplear: ", "Sistema de Premios tras realizar acciones." )
        
        elif(x>totalPersonas/(4**5)and not reco):
            result.append({'Cluster':'Cluster {0}'.format(i), 'porsentaje':por[i], 'motivacion':'reconocimiento', 'color':colors[i], 'nav':clustNav[i]})
            reco =True
            print("Inserte aca cluster: {0}".format(i))
            print("Tipo de motivación: ", "Reconocimiento")
            print("Se recomienda usar este sistema de gamificación")
            print("Tareas a emplear: ", "Sistema de Ranking según crecimiento o desafios realizados." )


    return result




if __name__ == "__main__":
    main()