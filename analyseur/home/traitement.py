import csv
import numpy as np
import matplotlib.pyplot as plt


class GetValue():

    def __init__(self):
        print("Initialisation de la récupération des valeurs")
        self.Tirage = []
        self.Tirage2 = []
        self.dicoTirage = {}
        self.apparition = [0]*50

        self.Nbchiffre = []
        self.Nbdixaine = []
        self.Nbvingt = []
        self.Nbtrente = []
        self.Nbquarante = []

        self.apparition_num_selec = []

        self.start()

    def start(self):    
        with open(r'../data/euromillions_202002.csv', newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
            for row in spamreader:
                if row[1] == 'VENDREDI':
                    self.Tirage.append(row[12]+row[13][1:])
                elif row[1] == 'MARDI   ':
                    self.Tirage.append(row[12]+row[13][1:])

        #on enlève les "-" pour avoir un tableau de nombres
        for elem in self.Tirage:
            self.Tirage2.append([int(a) for a in elem.split("-")[1:-1]])
        del self.Tirage

        #print("Tirage :")
        #print(Tirage2)
        #print("nombre de tirages : {}".format(len(Tirage2)))

        self.NbTirage = len(self.Tirage2)
        self.Nbchiffre = [0]*self.NbTirage
        self.Nbdixaine = [0]*self.NbTirage
        self.Nbvingt = [0]*self.NbTirage
        self.Nbtrente = [0]*self.NbTirage
        self.Nbquarante = [0]*self.NbTirage

        self.apparition_num_selec = [0]*self.NbTirage

        self.dicoInitialisation()
        self.trouverUnités()
    
    def dicoInitialisation(self):
        #On initialise le dico avec des 0
        for index in range(50):
            self.dicoTirage[index+1] = 0

        #On remplit le dico pour avoir le nombre de tirage de chaque nombre. 
        for tirage in self.Tirage2:
            for numero in tirage[:-2]:
                self.dicoTirage[numero] += 1 
                self.apparition[numero-1] += 1

    def trouverUnités(self):
        for index,elem in enumerate(self.Tirage2):
            for elem2 in elem[:-2]:
                if elem2 < 10:
                    self.Nbchiffre[index] += 1
                elif 10 <= elem2 <20:
                    self.Nbdixaine[index] += 1
                elif 20 <= elem2 <30:
                    self.Nbvingt[index] += 1
                elif 30 <= elem2 < 40:
                    self.Nbtrente[index] += 1
                elif 40<= elem2 <50:
                    self.Nbquarante[index] += 1

    def trouverOccurenceNum(self, num):
        ### APPARITION DU NUMERO SELECTIONNE ###
        #num = int(input("Voir l'historique du numéro : "))
        self.apparition_num_selec = [0]*self.NbTirage
        if num:
            for index,k in enumerate(self.Tirage2):
                #-2 car on enlève les num étoiles
                for val in k[:-2]:
                    if num == val:
                        self.apparition_num_selec[index] = 1
    
    def probaParNumero(self,num):
        ### CALCULE DES PROBA D'APPARITION DE CHAQUE NUM PAR RAPPORT A UN NUM ###
        Tirage_num = []
        if num:
            for index,k in enumerate(self.Tirage2):
                #-2 car on enlève les num étoiles
                for val in k[:-2]:
                    if num == val:
                        Tirage_num.append(k)
            nombre_apparition_desnum = [0]*50
            for k in Tirage_num:
                for val in k[:-2]:
                    nombre_apparition_desnum[val-1] += 1
            for l in range(len(nombre_apparition_desnum)):
                nombre_apparition_desnum[l] = (nombre_apparition_desnum[l]/len(Tirage_num))*100

        return {'x_num':[k for k in range(1,51)], 'y_num':nombre_apparition_desnum}



    def returnOccurencesNumero(self):
        return {'x': [k for k in range(1,51)], 'y':self.apparition}

    def returnOccurencesChiffres(self):
        return {'chiffres_x': [k for k in range(1,self.NbTirage+1)], 'chiffres_y':self.Nbchiffre}

    def returnOccurencesDixaines(self):
        return {'dixaines_x': [k for k in range(1,self.NbTirage+1)], 'dixaines_y':self.Nbdixaine}
    
    def returnOccurencesVingtaines(self):
        return {'vingtaines_x': [k for k in range(1,self.NbTirage+1)], 'vingtaines_y':self.Nbvingt}
    
    def returnOccurencesTrentaines(self):
        return {'trentaines_x': [k for k in range(1,self.NbTirage+1)], 'trentaines_y':self.Nbtrente}
    
    def returnOccurencesQuarantaines(self):
        return {'quarantaines_x': [k for k in range(1,self.NbTirage+1)], 'quarantaines_y':self.Nbquarante}

    def apparitionNumero(self,num):
        self.trouverOccurenceNum(num)
        return {'tirage': [k for k in range(1,self.NbTirage+1)], 'apparition':self.apparition_num_selec, 'num':num}

    def afficher(self):
        #### AFFICHAGE ####

        print("Nb chiffre : ")
        print(self.Nbchiffre)

        print("apparition des numéros :")
        print(self.dicoTirage)
        #a = input("récupérer le nombre d'occurence d'une valeur : ")
        #print(NbTirage_save[int(a)-1])

        x = np.array(range(1,self.NbTirage+1))
        x2 = np.array(range(1,51))
        y_chiffre = np.array(self.Nbchiffre)
        y_dixaine = np.array(self.Nbdixaine)
        y_vingt = np.array(self.Nbvingt)
        y_trente = np.array(self.Nbtrente)
        y_quarante = np.array(self.Nbquarante)
        #plt.plot(x,y_chiffre,"b:o", label="chiffres")
        #plt.plot(x,y_dixaine, label="dixaine")
        #plt.plot(x,y_vingt, label="vingtaine")
        #plt.plot(x,y_trente, label="trente")
        plt.figure()
        plt.plot(x,y_chiffre)
        plt.title("occurence chiffres")
        plt.figure()
        plt.plot(x,y_dixaine)
        plt.title("occurence dixaine")
        plt.figure()
        plt.plot(x,y_vingt)
        plt.title("occurence vingtaine")
        plt.figure()
        plt.plot(x,y_trente)
        plt.title("occurence trentaine")
        plt.figure()
        plt.plot(x,y_quarante)
        plt.title("occurence quarantaine")
        plt.figure()
        plt.plot(x2,np.array(self.apparition))
        plt.title("apparition des nombres")
        plt.figure()
        plt.plot(x, np.array(self.apparition_num_selec))
        plt.title("historique du numéro sélectionné")
        plt.show()