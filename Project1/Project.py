#Mariana de Matos Anjinho Charneca, LEIC-A, numero 95635
def eh_labirinto(maze):
    if isinstance(maze,tuple) and len(maze) >= 3: # Tuplo e ter mais de 3 tuplos
        for coluna in range(len(maze)): #Tuplos dentro do tuplo principal
            if isinstance(maze[coluna],tuple) and len(maze[coluna]) == len(maze[0]) and len(maze[0]) != 0: # tem que ter tuplos dentro de si
                leng = len(maze[0])
                if maze[coluna][0] == 1 and maze[coluna][leng-1] == 1 and leng >= 3:  # primeiro e ultimo elemento de todos tem que ser 1 (paredes), tuplos com comprimento iguais e tem que ser mais de 3
                    for linha in range(leng): 
                        if (maze[coluna][linha] != 1 and maze[coluna][linha] != 0) or not isinstance(maze[coluna][linha],int): #Elementos so podem que ser 0 e 1  
                            return False
                else:
                    return False
            else:
                return False  
    else:
        return False
    for el in maze[0] and maze[len(maze)-1]: #Primeiro e ultimo tem que ser parede
            if el != 1:
                return False
    return True
              
def eh_posicao(posicao):
    if isinstance(posicao,tuple) and len(posicao) == 2: #Tem que ser dado tuple e a len tem que ser de dois
        for digitos in posicao:
            if digitos < 0 or not isinstance(digitos,int): #i tem que ser maior que 0 e inteiro
                return False
        return True
    else:
        return False
    
def eh_conj_posicoes(posicoes):
    if isinstance(posicoes,tuple):
        for pos in range(len(posicoes)):
            if eh_posicao(posicoes[pos]) == True: # Validar se sao posicoes
                for e in range(pos):
                    if posicoes[e] == posicoes[pos]: #as posicoes tem que ser diferentes
                        return False
            else:
                return False
    else:
        return False
    return True

def tamanho_labirinto(maze):
    if eh_labirinto(maze) == True: #Validacao 
        return (len(maze),len(maze[0])) #diz a length do tuplo(colunas) e depois dentro dos tuplos a length (linhas) 
    else: 
        raise ValueError ('tamanho_labirinto: argumento invalido')
    
def eh_mapa_valido(maze,posicoes):
    if eh_labirinto(maze) == True and eh_conj_posicoes(posicoes) == True:
        tamanho = tamanho_labirinto(maze)
        for posicao in posicoes:
            if posicao[0] >= (tamanho[0]-1) or posicao[0] == 0 or 0 == posicao[1] or posicao[1] > (tamanho[1]-1): #tem que estar dentro dos limites 
                return False
            if maze[posicao[0]][posicao[1]] == 1: #Posicao ocupada dentro nao pode ser parede
                return False
        return True
    else:
        raise ValueError ('eh_mapa_valido: algum dos argumentos e invalido')
    
def eh_posicao_livre(maze,unidades,posi):
    if eh_labirinto(maze) == False or eh_conj_posicoes(unidades) == False: #Validacao
        raise ValueError ('eh_posicao_livre: algum dos argumentos e invalido')
    tamanho = tamanho_labirinto(maze)
    if eh_mapa_valido(maze,unidades) == True and eh_posicao(posi) == True: #Verificar valores
        if 0 < posi[0] < (tamanho[0] - 1) and 0 < posi[1] < (tamanho[1] - 1):  #Verificar se a posicao esta dentro do maze e nao das paredes
            if maze[posi[0]][posi[1]] == 1: #Nao pode ser paredes
                return False
            for el in range(len(unidades)): 
                if unidades[el] == posi:  #Se sobreporem as posicoes, Falso
                    return False
            return True
        else:
            return False
    else:
        raise ValueError ('eh_posicao_livre: algum dos argumentos e invalido')

def posicoes_adjacentes(posicao):
    if eh_posicao(posicao) == True: #Se for uma posicao valida
        zero = posicao[0]
        um = posicao[1]
        res = ((zero,um-1),(zero-1,um),(zero+1,um),(zero,um+1)) #posicoes adjacentes
        final = ()
        for pos in res:
            if eh_posicao(pos) == True: #Verificar quais delas sao validas
                final = final + (pos, )
        return final
    else:
        raise ValueError ("posicoes_adjacentes: argumento invalido")

def mapa_str(maze,unidades):
    if eh_labirinto(maze) == False or eh_conj_posicoes(unidades) == False: #Validacao
        raise ValueError ("mapa_str: algum dos argumentos e invalido")
    if eh_mapa_valido(maze,unidades) == True: #Validacao
        stri = ""
        posicao = False
        for linha in range(len(maze[0])):  #em todos os algarismos dos tuplos 
            for coluna in range(len(maze)): 
                for unidade in unidades:
                    if (coluna,linha) == unidade:   #Verificar se a posicao e ocupada por uma unidade
                        stri = stri + "O" #Unidade mete O
                        posicao = True
                        break    #Se for acabar o ciclo
                    else:
                        posicao = False
                if posicao == False:  #Se a posicao nao for ocupada
                    if maze[coluna][linha] == 0: 
                        stri = stri + "."  
                    else:                  #Por # em vez de 1 e . em vez de 0
                        stri = stri + "#"
            stri = stri + "\n"
        stri = stri[:len(stri)-1]
        return stri
    else:
        raise ValueError ('mapa_str: algum dos argumentos e invalido')
    
def obter_objetivos(maze,unidades,posicao):
    adj = ()
    if eh_labirinto(maze) == False or eh_conj_posicoes(unidades) == False or posicao not in unidades:
        raise ValueError ("obter_objetivos: algum dos argumentos e invalido") #Validar
    if eh_mapa_valido(maze,unidades) == True: #Validar dados
        for unidade in unidades:
            if unidade != posicao:
                adj = adj + (posicoes_adjacentes(unidade))  #Unidades em que precisamos de adjacentes
        tamanho = tamanho_labirinto(maze)
        res = ()
        for unidade in adj:  #Unidades em que fazemos as adjacentes
            if eh_posicao_livre(maze,unidades,unidade) == True and unidade not in res: #Validar as posicoes adjacentes e nao repetir 
                res = res + (unidade,)
        return res
    else:
        raise ValueError ("obter_objetivos: algum dos argumentos e invalido")
    
def obter_caminho(maze,unidades,posicao):
    if eh_labirinto(maze) == False or eh_conj_posicoes(unidades) == False or posicao not in unidades: #Validar
        raise ValueError ('obter_caminho: algum dos argumentos e invalido')    
    if eh_mapa_valido(maze,unidades) == False: #Validacao
        raise ValueError ('obter_caminho: algum dos argumentos e invalido')
    lista_exploracao = [((posicao),())] #Lista = [(posicaoAtual),(caminhoAtual)]
    visitados = ()
    objetivos = obter_objetivos(maze,unidades,posicao)
    if objetivos == () or len(unidades) == 1:     #Se nao houver objetivos devolve nada
        return ()
    posicao_atual = ()
    caminho_atual = ()
    while lista_exploracao != []:         #Loop infinito 
        posicao_atual = lista_exploracao[0][0] 
        caminho_atual = lista_exploracao[0][1]
        if posicao_atual not in visitados:    
            visitados = visitados + (posicao_atual,) #Adicionar a posicao atual aos visitados
            caminho_atual = caminho_atual + (posicao_atual,) #caminho + posicao onde esta (caminho completo
            if posicao_atual in objetivos: #Chegou ao objetivo
                return caminho_atual
            else:
                for pos in posicoes_adjacentes(posicao_atual): #Adicionar proxima posicao como posicoes adjacentes
                    if  eh_posicao_livre(maze,unidades,pos) == True: #Validacao
                        lista_exploracao = lista_exploracao + [((pos),(caminho_atual))] #adicionar a lista de exploracao 
        del(lista_exploracao)[0] #Delete ao primeiro para mudar posicoes e caminhos atuais
    return () #Caso seja impossivel encontrarem-se
        
def mover_unidade(maze,unidades,posicao):
    if eh_labirinto(maze) == False or eh_conj_posicoes(unidades) == False or posicao not in unidades:
        raise ValueError ('mover_unidade: algum dos argumentos e invalido')     
    if eh_mapa_valido(maze,unidades) == False: #Validacao
        raise ValueError ('mover_unidade: algum dos argumentos e invalido') 
    caminho = obter_caminho(maze,unidades,posicao)
    res = ()
    for unidade in unidades: 
        if unidade in posicoes_adjacentes(posicao) or caminho == (): #Se uma das unidades for adjacente mantem-se igual ou caminho = ()
            return unidades
        elif posicao != unidade: #Se for a unidade que nao queremos mover
            res = res + (unidade,)
        else: #Se for a que mexe, anda um pelo caminho
            res = res + (caminho[1],)
    return res
            
            
    
    
    
        
                        
                    
    
    

    

                             
                         