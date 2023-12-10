#nome = input("\nDigite o seu nome:")
#print("Olá", nome)
print("1- Criptografar")
print("2- Descriptografar")

lang = input()
match lang:
    case "1":
         lista = ['a','b','c','d','e','f','g','h','i',
                  'j','k','l','m','n','o','p','q','r',
                  's','t','u','v','w','x','y','z']
         text = input("\nDigite o texto:")

         print(len(lista))
        
          
            

        

    case "2":
            lista = ['a','b','c','d','e','f','g','h','i',
                    'j','k','l','m','n','o','p','q','r',
                    's','t','u','v','w','x','y','z']
            text = input("\nDigite o texto:")

            print(len(lista))

    case _:
        print("ERRO")