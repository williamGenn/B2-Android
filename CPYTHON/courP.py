import getpass
def lire():
    print("entrez le nom du fichier")
    A=input()
    with open(A, "r") as fichier5:
        print(fichier5.read())


def ecrire():
    print("entrez le nom du fichier")
    A=input()
    with open(A, "a") as fichier5:
        print("Que voulez vous entrer?")
        
        fichier5.write(input())
      
        
if __name__=="__main__":       
    with open("doc.txt", "r") as fichier:
    	print(fichier.read())
        
        
    with open("doc.txt", "a") as fichier:    
        fichier.write("test")
        
        
    with open("doc1.py","r") as fichier1:
    	print(fichier1.read())
        
    ecrire()
    lire()    