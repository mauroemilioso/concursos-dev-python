import re

class Palindromo():
    
    def ehpalindromo(palavra):         
        
        palavra = palavra.lower()
        palavra = re.sub("[^a-zA-Z]", "", palavra)
        
        # inverte
        palindromo = palavra[::-1]
        
        return palavra == palindromo

        """try:
            palavra_informada = input("Ditite a palavra: ")
            print('É palindromo?')
            if ehpalindromo(palavra_informada):
                print('Sim')
            else:
                print ('Não')
        #else:
        #    print('Não deu erro')
        except NameError:
            print('Deu Problema' + NameError)
        finally:
            print('Sucesso!')"""

    







    
   