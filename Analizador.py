import json
import pandas as pd
import random
import xlsxwriter
import csv
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
import os

plt.rcParams['figure.figsize'] = (16, 9)
plt.style.use('ggplot')

def leer():

    with open("log") as f:
        content = f.readlines()
    total = {}
    carreras = ['Ingenieria', 'Ciencias Sociales', 'Artes', 'Ciencias Exactas']
    for line in content:
        line = line.split(" ")
        if line[0] in total:
            pass
        else:
            #print(line[0])
            aleat=random.randint(0,len(carreras)-1)
            total[line[0]] = {'ip':line[0],'consultas':0, 'login.do':0, '':0, 'login-submit.do':0, 'salir.do':0, 'certificados':0, 'asistencia':0, 'enlaces.do':0, 'comentarios.do':0, 'solicitudes':0, 'incentivos':0, 'contactenos.do':0, 'sa':0, 'ayudaFaq.do':0, 'noSesion.do':0, 'comentarios-submit.do':0, 'contactenos-submit.do':0, 'administracion':0, 'matriculas':0, 'ayudafaq.do':0, 'matricula':0, 'gm':0, 'Seleccione':0, '%7D':0,'Carrera':'{0}'.format(carreras[aleat])}
        
        categoria = line[6].split('/')
        total[line[0]][categoria[2]] += 1
    df = []
    for x in total:
        df.append(total[x])
    df = pd.DataFrame(df)
    return df

def preProceso(df):
    df = df.drop(["login.do","login-submit.do","salir.do","matriculas","ayudafaq.do","matricula","gm",
                  "Seleccione", "%7D", "asistencia", "enlaces.do", "comentarios.do", "ayudaFaq.do", "noSesion.do", "comentarios-submit.do",
                   "contactenos-submit.do", "administracion", "contactenos.do", "sa"],axis=1)
    
    features = ["consultas","certificados","solicitudes","incentivos"]
    nondisc = ["ip","Carrera"]

    x = df.loc[:, features].values
    y = df.loc[:, nondisc].values
    x = StandardScaler().fit_transform(x)

    pca = PCA(n_components=2)

    components = pca.fit_transform(x)

    pdf = pd.DataFrame(data= components, columns= ['p1','p2'])
    km4=KMeans(n_clusters=5,init='k-means++', max_iter=300, n_init=10, random_state=0)


    y_means = km4.fit_predict(pdf)

    clusters = pd.DataFrame({'Cluster': y_means})

    df = pd.concat([df,clusters],axis=1)
    dicson = {}
    
    pdf = np.array(pdf)
    #Visualizing the clusters for k=4
    plt.scatter(pdf[y_means==0,0],pdf[y_means==0,1],s=50, c='red',label='Cluster 0')
    plt.scatter(pdf[y_means==1,0],pdf[y_means==1,1],s=50, c='yellow',label='Cluster 1')
    plt.scatter(pdf[y_means==2,0],pdf[y_means==2,1],s=50, c='green',label='Cluster 2')
    plt.scatter(pdf[y_means==3,0],pdf[y_means==3,1],s=50, c='blue',label='Cluster 3')
    plt.scatter(pdf[y_means==4,0],pdf[y_means==4,1],s=50, c='purple',label='Cluster 4')
    #plt.scatter(pdf[y_means==5,0],pdf[y_means==5,1],s=50, c='yellow',label='Cluster6')
    plt.scatter(km4.cluster_centers_[:,0], km4.cluster_centers_[:,1],s=200,marker='s', c='red', alpha=0.7, label='Centroids')
    plt.title('Clusterizacion de Usuarios')
    plt.legend()
    plt.savefig('statics/img/Clusters.png')
    plt.clf()
    print(df)
    for i in range(5):
        c1 =df[df['Cluster'] == i]
        dicson['Cluster {0}'.format(i)] = {'ips': c1['ip'].tolist(),'consultas': int(c1['consultas'].sum()),
                                           'certificados': int(c1['certificados'].sum()),'solicitudes': int(c1['solicitudes'].sum()),
                                           'incentivos': int(c1['incentivos'].sum())}

    try:
        os.remove("result.json")
    except:
        pass 
    with open('result.json', 'w') as fp:
        json.dump(dicson, fp,indent=4)

    return json.dumps(dicson,indent=4)



def main():
    df = leer()
    js = preProceso(df)
    return js


if __name__ == "__main__":
    main()