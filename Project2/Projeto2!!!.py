#Mariana Charneca, LEIC - A, n 195635
#TAD Posicao
#Construtor
#Tuplo 
def cria_posicao(x,y):
    """
cria_posicao: N x N -> posicao

cria posicao(x,y) recebe os valores correspondentes as coordenadas de uma
posicao e devolve a posicao correspondente. O construtor verica a validade
dos seus argumentos, gerando um ValueError com a mensagem cria_posicao:
argumentos invalidos caso os seus argumentos nao sejam validos. 
    """
    if isinstance(x,int) and isinstance(y,int): #Tem que ser inteiros
        if x >= 0 and y >= 0: #Maiores que zero
            return (x,y) #Devolve um tuplo
    raise ValueError ("cria_posicao: argumentos invalidos")

def cria_copia_posicao(pos): 
    """
cria_copia_posicao: posicao -> posicao

cria_copia_posicao(pos) recebe uma posicao e devolve uma copia nova da posicao
    """    
    return cria_posicao(pos[0],pos[1])

#Seletores

def obter_pos_x(pos):
    """
obter_pos_x: posicao -> N

obter_pos_x(pos) devolve o componente x da posicao pos 
    """        
    return pos[0]

def obter_pos_y(pos):
    """
obter_pos_y: posicao -> N

obter_pos_y(pos) devolve o componente y da posicao pos 
    """     
    return pos[1]

#reconhecedor

def eh_posicao(pos):
    """
eh_posicao: universal -> booleano

eh_posicao(arg) devolve True caso o seu argumento seja um TAD posicao e Falso caso contrario 
    """     
    if isinstance(pos,tuple) and len(pos) == 2: #Tem que ser tuplo e len = 2
        if isinstance(pos[0],int) and isinstance(pos[1],int): #Tem que ser inteiros
            if pos[0] >= 0 and pos[1] >= 0: #E maiores que zero
                return True
    return False

#Teste

def posicoes_iguais(pos1,pos2):
    """
posicoes_iguais: posicao x posicao -> booleano

posicoes_iguais(pos1,pos2) devolve TRUE apenas de pos1 e pos2 sao posicoes iguais 
    """     
    if pos1 == pos2: #Se for igual return True
        return True
    else:
        return False

#Transformador

def posicao_para_str(pos):
    """
posicao_para_str: posicao -> str

posicao_para_str(pos) devolve a cadeia de caracteres "(x,y)" que representa o seu argumento, sendo os valores x e y as coordenadas de p
    """         
    return str(pos) #poe em string

#Funcao de alto nivel

def obter_posicoes_adjacentes(pos):
    """
obter_posicoes_adjacentes: posicao -> tuplo de posicoes 

obter_posicoes_adjacentes(pos) devolve um tuplo com as posicoes adjacentes a posicao
pos de acordo com a ordem de leitura de um labirinto.
    """      
    x = obter_pos_x(pos) 
    y = obter_pos_y(pos)
    res = ((x,y-1),(x-1,y),(x+1,y),(x,y+1)) #Obter tuplo com adjacentes
    final = ()
    for adj in range(4):   
        if eh_posicao(res[adj]) == True: #verificar a validade de cada um
            final = final + (res[adj],)
    return final

#TADunidades
#Construtores
#Dicionario
def cria_unidade(pos,vida,forca,exercito):
    """
cria_unidade: posicao x N x N x str -> unidade
    
cria unidade(p, v, f, str) recebe uma posicao p, dois valores inteiros maiores
que 0 correspondentes a vida e forca da unidade, e uma cadeia de caracteres
nao vazia correspondente ao exercito da unidade; e devolve a unidade correspondente.
O construtor verifica a validade dos seus argumentos, gerando um
ValueError com a mensagem cria unidade: argumentos invalidos
caso os seus argumentos nao sejam validos.
    """
    if eh_posicao(pos) == True and isinstance(vida,int) and isinstance(forca,int) and isinstance(exercito,str): #Verficiao do tipo
        if vida > 0 and forca > 0 and " " not in exercito: #forca e vida maior que zero e exercito nao tem espacos
            if exercito == "": #exercito nao pode ser vazia
                raise ValueError ("cria_unidade: argumentos invalidos")
            else:
                return { "pos" : cria_copia_posicao(pos), "vida" : vida, "forca" : forca, "exercito" : exercito}
    raise ValueError ("cria_unidade: argumentos invalidos")

def cria_copia_unidade(unidade):
    """
cria_copia_unidade: unidade -> unidade 

cria_copia_unidade(unidade) recebe uma unidade u e devolve uma nova copia da unidade.
    """      
    return cria_unidade(cria_copia_posicao(unidade["pos"]),unidade["vida"],unidade["forca"],unidade["exercito"]) #Cria copia
  

#Seletores

def obter_posicao(unidade):  #obtem a posicao do dicionario
    """
obter_posicao: unidade -> posicao 

obter_posicao(uni) devolve a posicao da unidade uni.
    """     
    return unidade["pos"]

def obter_exercito(unidade): #obtem o exercito do dicionario
    """
obter_exercito: unidade -> str 

obter_exercito(uni) devolve a cadeia de caracteres correspondentes ao exercito da unidade uni.
    """         
    return unidade["exercito"]

def obter_forca(unidade): #obtem a forca do dicionario
    """
obter_forca: unidade -> N 

obter_forca(uni) devolve o valor correspondente a forca de ataque da unidade.
    """     
    return unidade["forca"]

def obter_vida(unidade): #obtem a vida do dicionario
    """
obter_vida: unidade -> N 

obter_vida(uni) devolve o valor correspondente aos pontos de vida da unidade.
    """     
    return unidade["vida"]

#modificadores

def muda_posicao(unidade,pos):
    """
muda_posicao: unidade x pos -> unidade 

muda_posicao(uni,pos) modifica destrutivamente a unidade uni alterando a sua posicao com o novo valor pos e devolve a propria unidade
    """    
    unidade["pos"] = pos #Trocar as pos no dicionario
    return unidade

def remove_vida(unidade,vidaatirar):
    """
remove_vida: unidade x N -> unidade 

remove_vida(unidade,n) modifica destrutivamente a unidade uni alterando os seus pontos de vida subtraindo o valor v, e devolve a propria unidade 
    """          
    unidade["vida"] = unidade["vida"] - vidaatirar # subtrair e trocar a vida 
    return unidade

#reconhecedor

def eh_unidade(unidade):
    """
eh_unidade: Universal -> booleano 

eh_unidade(arg) devolve True caso o seu argumento seja um TAD unidade e False caso contrario 
    """      
    if isinstance(unidade,dict) and len(unidade) == 4: # Ve se e dicionario de tamanho 4
        if "pos" in unidade and "vida" in unidade and "forca" in unidade and "exercito" in unidade: #verificar se existem as chaves 
            if eh_posicao(obter_posicao(unidade)) and isinstance(obter_vida(unidade),int) and isinstance(obter_forca(unidade),int) and isinstance(obter_exercito(unidade),str): #verificar os tipos 
                if obter_exercito(unidade) == "": #string nao pode ser vazia
                    return False
                elif obter_vida(unidade) > 0 and obter_forca(unidade) > 0:  #vida e forca maior que zero e sem espacos na string 
                    return True
    return False

#Teste

def unidades_iguais(unidade1,unidade2):
    """
unidades_iguais: unidade x unidade -> booleano 

unidades_iguais(unidade1,unidade2) devolve True apenas se unidade1 e unidade2 sao unidades iguais 
    """          
    if unidade1 == unidade2: #Se e igual da True
        return True
    else:
        return False
    
#transformadores

def unidade_para_char(unidade):
    """
unidade_para_char: unidade -> str 

unidade_para_char(unidade) devolve a cadeia de caracteres dum unico elemento,
correspondente ao primeiro caracter em maiuscula do exercito da unidade
passada por argumento. 
    """          
    return obter_exercito(unidade)[0].upper()   

def unidade_para_str(unidade):
    """
unidade_para_str: unidade -> str 

unidade_para_str(unidade) devolve a cadeia de caracteres que representa a unidade
    """      
    return unidade_para_char(unidade) + str([obter_vida(unidade),obter_forca(unidade)]) + "@" + posicao_para_str(obter_posicao(unidade)) 

#Funcoes de Alto Nivel

def unidade_ataca(u1,u2):
    """
unidade_ataca: unidade x unidade -> booleano 

unidade_ataca(unidade) modica destrutivamente a unidade u2 retirando o valor de
pontos de vida correspondente a forca de ataque da unidade u1. A funcao devolve
True se a unidade u2 for destruida ou False caso contrario
    """          
    remove_vida(u2,obter_forca(u1)) #Remocao da vida
    return obter_vida(u2) <= 0 #devolver True se for destruida
    
def ordenar_unidades(tuplo):
    """
ordenar_unidades: tuplo unidades -> tuplo unidades  

ordenar_unidades(tuplo) devolve um tuplo contendo as mesmas unidades do tuplo
fornecido como argumento, ordenadas de acordo com a ordem de leitura do labirinto.
    """       
    tuplo = list(tuplo) #Transforma em lista
    tuplo = sorted(tuplo,key = lambda x: (obter_pos_y(x["pos"]),obter_pos_x(x["pos"]))) #Sort por posicao
    tuplo = tuple(tuplo) #Transforma em tuplo
    return tuplo

      
#Tad Mapa
#Construtores
#Dicionario
def cria_mapa(dim,wall,e1,e2):
    """
cria_mapa: tuplo x tuplo x tuplo x tuplo -> mapa   

cria_mapa(d, w, e1, e2) recebe um tuplo d de 2 valores inteiros correspondentes
as dimensoes Nx e Ny do labirinto seguindo as restricoes do 1 projecto,
um tuplo w de 0 ou mais posicoes correspondentes as paredes que nao sao
dos limites exteriores do labirinto, um tuplo e1 de 1 ou mais unidades do
mesmo exercito, e um tuplo e2 de um ou mais unidades de um outro exercito;
e devolve o mapa que representa internamente o labirinto e as unidades presentes.
O construtor verifica a validade dos seus argumentos, gerando um
ValueError com a mensagem cria_mapa: argumentos invalidos caso
os seus argumentos nao sejam validos.
    """        
    if isinstance(dim,tuple) and isinstance(wall,tuple) and isinstance(e1,tuple) and isinstance(e2,tuple): #Verifica o tipo dos dados
            if dim == () or e1 == () or e2 == (): #Ve se os tuplos sao vazios
                raise ValueError ("cria_mapa: argumentos invalidos")                
            for a in dim:
                if not isinstance(a,int) or a < 3 or len(dim) != 2: #Ve se a dimensao e inteiro maior ou igual a 3x3
                    raise ValueError ("cria_mapa: argumentos invalidos")
            for pos in wall: 
                if eh_posicao(pos) == False: #Ve se sao posicoes 
                    raise ValueError ("cria_mapa: argumentos invalidos")
                x = obter_pos_x(pos)
                y = obter_pos_y(pos)
                if x == 0 or y == 0 or x >= dim[0]-1 or y >= dim[1]-1: #Nao parede e dentro do mapa
                    raise ValueError ("cria_mapa: argumentos invalidos")
            for tuplo_com_uni in (e1,e2): #ve nos dois exercitos 
                for unidade in tuplo_com_uni:
                    if eh_unidade(unidade) == False: #Se os componentes sao todos unidades
                        raise ValueError ("cria_mapa: argumentos invalidos")
            return {"dim" : dim, "wall" : wall, "e1" : e1, "e2" : e2} #Devolve em dicionario
    raise ValueError ("cria_mapa: argumentos invalidos")


def cria_copia_mapa(mapa): #Cria copia do mapa
    """
cria_copia_mapa: mapa -> mapa  

cria_copia_mapa(mapa) recebe um mapa e devolve uma nova copia do mapa 
    """           
    e1_new = () 
    e2_new = ()
    Wall_new = () 
    for wall in mapa["wall"]:
        Wall_new = Wall_new + (cria_copia_posicao(wall),) #Cria copias das posicoes
    for e in (mapa["e1"]): 
        e1_new = e1_new + (cria_copia_unidade(e),) #Cria copias das unidades do e1 
    for e in mapa["e2"]:
        e2_new = e2_new + (cria_copia_unidade(e),) #Cria copia das unidades do e2
    return cria_mapa(mapa["dim"],Wall_new,e1_new,e2_new) #cria copia
    
#Seletores

def obter_tamanho(mapa):
    """
obter_tamanho: mapa -> tuplo  

obter_tamanho(mapa) devolve um tuplo de dois valores inteiros correspondendo
o primeiro deles a dimensao Nx e o segundo a dimensao Ny do mapa.
    """
    return mapa["dim"]

def obter_nome_exercitos(mapa):
    """
obter_nome_exercitos: mapa -> tuplo  

obter_nome_exercitos(mapa) devolve um tuplo ordenado com duas cadeias de
caracteres correspondendo aos nomes dos exercitos do mapa.
    """     
    res = (obter_exercito(mapa["e1"][0]),obter_exercito(mapa["e2"][0])) #Obtem o nome dos dois exercitos
    res = list(res)
    res = sorted(res) #organiza
    res = tuple(res)
    return res

def obter_unidades_exercito(mapa,string):
    """
obter_unidades_exercito: mapa x str -> tuplo unidades

obter_unidades_exercito(mapa,str) devolve um tuplo contendo as unidades do
mapa pertencentes ao exercito indicado pela cadeia de caracteres e, ordenadas
em ordem de leitura do labirinto.
Devolve () se as unidades nao forem validas
    """         
    for uni in mapa["e1"]:
        if eh_unidade(uni) == True and obter_exercito(uni) == string: #Ve se o e1 e o da string
            return ordenar_unidades(mapa["e1"]) #devolve unidades organizadas
    for uni in mapa["e2"]:
        if eh_unidade(uni) == True and obter_exercito(uni) == string:
            return ordenar_unidades(mapa["e2"]) #Devolve unidades organizadas do e2
    return () #se o exercito em questao nao for valido 

def obter_todas_unidades(mapa):
    """
obter_todas_unidades: mapa -> tuplo  

obter_todas_unidades(mapa) devolve um tuplo contendo todas as unidades do
mapa, ordenadas em ordem de leitura do labirinto.
    """         
    tuplo = ()
    for e1 in mapa["e1"]:
        tuplo = tuplo + (e1,) #Coloca as unidades todas do e1 num tuplo
    for e2 in mapa["e2"]:
        tuplo = tuplo + (e2,) #Coloca as unidades todas do e2 num tuplo
    return ordenar_unidades(tuplo) #ordena

def obter_unidade(mapa,pos):
    """
obter_unidade: mapa x posicao -> unidade  

obter_unidade(mapa,pos) devolve a unidade do mapa que se encontra na posicao
pos.
    """          
    for exercito in (mapa["e1"],mapa["e2"]): #ve nos dois exercitos
        for unidade in exercito:
            if obter_posicao(unidade) == pos: #se a posicao e igual ao pos
                return unidade #devolve a unidade 

#Modificadores

def eliminar_unidade(mapa,unidade):
    """
eliminar_unidade: mapa x unidade -> mapa  

eliminar_unidade(mapa,unidade) modifica destrutivamente o mapa m eliminando a
unidade u do mapa e deixando livre a posicao onde se encontrava a unidade.
Devolve o proprio mapa.
    """       
    for e in ("e1","e2"): #Dentro dos dois exercitos 
        if obter_exercito(unidade) == obter_exercito(mapa[e][0]):
            for num_unidade in range(len(mapa[e])): 
                if unidades_iguais(mapa[e][num_unidade],unidade): #Se as unidades forem iguais
                    aux = list(mapa[e]) #criar um aux que e transforma em lista
                    del(aux[num_unidade])
            mapa[e] = tuple(aux) # mapa[e] e subsitituido
    return mapa 
            
def mover_unidade(mapa,uni,posicao):
    """
mover_unidade: mapa x unidade x posicao -> mapa  

mover_unidade(mapa,uni,posicao) modifica destrutivamente o mapa e a unidade
alterando a posicao da unidade no mapa para a nova posicao (posicao) e deixando
livre a posicao onde se encontrava. Devolve o proprio mapa.
    """           
    for e in (mapa["e1"],mapa["e2"]): #ver os dois exercitos
        if obter_exercito(uni) == obter_exercito(e[0]): #naquele cujo o nome e igual
            for num_unidade in range(len(e)): 
                if unidades_iguais(e[num_unidade],uni):#Quando as unidades forem iguais
                    muda_posicao(e[num_unidade],posicao) #trocar a unidade
    return mapa

#Reconhecedores

def eh_posicao_unidade(mapa,posicao):
    """
eh_posicao_unidade: mapa x posicao -> booleano  

eh_posicao_unidade(mapa,pos) devolve True apenas no caso da posicao p do mapa
estar ocupada por uma unidade.
    """          
    tuplo = obter_todas_unidades(mapa) #obter as unidades num tuplo 
    for unidade in tuplo: 
        if obter_posicao(unidade) == posicao: #Se as posicoes forem iguais
            return True #da True
    return False

def eh_posicao_corredor(mapa,posicao):
    """
eh_posicao_corredor: mapa x posicao -> booleano  

eh_posicao_corredor(mapa,pos) devolve True apenas no caso da posicao p do mapa
corresponder a um corredor no labirinto (independentemente de estar ou nao
ocupado por uma unidade).
    """              
    dim = obter_tamanho(mapa) 
    if posicao[0] == 0 or posicao[1] == 0 or posicao[0] == dim[0]-1 or posicao[1] == dim[1]-1: #Paredes exteriores 
        return False
    for parede_dentro in mapa["wall"]: #parede interiores 
        if parede_dentro == posicao: 
            return False 
    return True

def eh_posicao_parede(mapa,posicao):
    """
eh_posicao_parede: mapa x posicao -> booleano  

eh_posicao_parede(mapa,pos) devolve True apenas no caso da posicao p do mapa
corresponder a uma parede do labirinto.
    """         
    dim = obter_tamanho(mapa) 
    if posicao[0] == 0 or posicao[1] == 0 or posicao[0] == dim[0]-1 or posicao[1] == dim[1]-1: #Paredes exteriores 
        return True
    for parede_dentro in mapa["wall"]: #parede interiores 
        if parede_dentro == posicao: 
            return True
    return False

#Teste

def mapas_iguais(mapa1,mapa2):
    """
mapas_iguais: mapa1 x mapa2 -> booleano  

mapas_iguais(mapa1,mapa2) devolve True apenas se m1 e m2 forem mapas iguais.
    """    
    if mapa1 == mapa2: #Se os mapas forem iguais 
        return True #Da true
    return False

#Transformador

def mapa_para_str(mapa):
    """
mapa_para_str: mapa-> str  

mapa_para_str(mapa) devolve uma cadeia de caracteres que representa o mapa
como descrito no primeiro projeto, neste caso, com as unidades representadas
pela sua representacao externa.
    """        
    stri = ""
    dim = obter_tamanho(mapa) #Dimensoes 
    for y in range(obter_pos_y(dim)): #Em cada linha 
        for x in range(obter_pos_x(dim)): #Em cada coluna 
            if eh_posicao_parede(mapa,cria_posicao(x,y)): #Ver se e parede 
                stri = stri + "#"
            elif eh_posicao_unidade(mapa,cria_posicao(x,y)): #ver se e unidade 
                letra = unidade_para_char(obter_unidade(mapa,cria_posicao(x,y)))
                stri = stri + letra
            else: #Se nao e nada 
                stri = stri + "."
        stri = stri + "\n"
    stri = stri[:len(stri)-1] #Para tirar o ultimo paragrafo
    return stri 

#Funcoes de Alto nivel

def obter_inimigos_adjacentes(mapa,unidade):
    """
obter_inimigos_adjacentes: mapa x unidade -> tuplo unidades  

obter_inimigos_adjacentes(mapa,u) devolve um tuplo contendo as unidades inimigas
adjacentes a unidade u de acordo com a ordem de leitura do labirinto.
    """            
    res = ()
    for nome in obter_nome_exercitos(mapa): #descobrir o nome do inimigo
        if obter_exercito(unidade) != nome:
            inimigo = nome
    adjacentes = obter_posicoes_adjacentes(obter_posicao(unidade)) #obter o tuplo com adjacentes
    for adj in adjacentes:
        uni = obter_unidade(mapa,adj) #unidade da posicao 
        if uni != None and obter_exercito(uni) == inimigo: #se existir unidade e for dos inimigos
            res = res + (uni,) #adiciona a solucao
    return res


def obter_movimento(mapa, unit):
    '''
    A funcao obter_movimento devolve a posicao seguinte da unidade argumento
    de acordo com as regras de movimento das unidades no labirinto.

    obter_movimento: mapa x unidade -> posicao
    '''

    ######################
    # Funcoes auxiliares #
    ######################
    def pos_to_tuple(pos):
        return obter_pos_x(pos), obter_pos_y(pos)

    def tuple_to_pos(tup):
        return cria_posicao(tup[0], tup[1])

    def tira_repetidos(tup_posicoes):
        conj_tuplos = set(tuple(map(pos_to_tuple, tup_posicoes)))
        return tuple(map(tuple_to_pos, conj_tuplos))

    def obter_objetivos(source):
        enemy_side = tuple(filter(lambda u: u != obter_exercito(source), obter_nome_exercitos(mapa)))[0]
        target_units = obter_unidades_exercito(mapa, enemy_side)
        tup_com_repetidos = \
            tuple(adj
                  for other_unit in target_units
                  for adj in obter_posicoes_adjacentes(obter_posicao(other_unit))
                  if eh_posicao_corredor(mapa, adj) and not eh_posicao_unidade(mapa, adj))
        return tira_repetidos(tup_com_repetidos)

    def backtrack(target):
        result = ()
        while target is not None:
            result = (target,) + result
            target, _ = visited[target]
        return result

    ####################
    # Funcao principal #
    ####################
    # Nao mexer se ja esta' adjacente a inimigo
    if obter_inimigos_adjacentes(mapa, unit):
        return obter_posicao(unit)

    visited = {}
    # posicao a explorar, posicao anterior e distancia
    to_explore = [(pos_to_tuple(obter_posicao(unit)), None, 0)]
    # registro do numero de passos minimo ate primeira posicao objetivo
    min_dist = None
    # estrutura que guarda todas as posicoes objetivo a igual minima distancia
    min_dist_targets = []

    targets = tuple(pos_to_tuple(obj) for obj in obter_objetivos(unit))

    while to_explore:  # enquanto nao esteja vazio
        pos, previous, dist = to_explore.pop(0)

        if pos not in visited:  # posicao foi ja explorada?
            visited[pos] = (previous, dist)  # registro no conjunto de exploracao
            if pos in targets:  # se a posicao atual eh uma dos objetivos
                # se eh primeiro objetivo  ou se esta a  distancia minima
                if min_dist is None or dist == min_dist:
                    # acrescentor 'a lista de posicoes minimas
                    min_dist = dist
                    min_dist_targets.append(pos)
            else:  # nao 'e objetivo, acrescento adjacentes
                for adj in obter_posicoes_adjacentes(tuple_to_pos(pos)):
                    if eh_posicao_corredor(mapa, adj) and not eh_posicao_unidade(mapa, adj):
                        to_explore.append((pos_to_tuple(adj), pos, dist + 1))

        # Parar se estou a visitar posicoes mais distantes que o minimo,
        # ou se ja encontrei todos os objetivos
        if (min_dist is not None and dist > min_dist) or len(min_dist_targets) == len(targets):
            break

    # se encontrei pelo menos uma posicao objetivo, 
    # escolhe a de ordem de leitura menor e devolve o primeiro movimento
    if len(min_dist_targets) > 0:
        # primeiro dos objetivos em ordem de leitura
        tar = sorted(min_dist_targets, key=lambda x: (x[1], x[0]))[0]
        path = backtrack(tar)
        return tuple_to_pos(path[1])

    # Caso nenhuma posicao seja alcancavel
    return obter_posicao(unit)


    
def calcula_pontos(mapa,string):
    """
    calcula_pontos: mapa x string -> int
    
    Funcao auxiliar que recebe um mapa e uma cadeia de caracteres correspondente ao nome
de um dos exercitos do mapa e devolve a sua pontuacao. A pontuacao dum exercito e
o total dos pontos de vida de todas as unidades do exercito.
    """
    pontos = 0
    unidades = obter_unidades_exercito(mapa,string) #obter as unidades
    if unidades == (): #se nao houverem unidades
        return pontos # 0 pontos 
    for uni in unidades: 
        pontos = pontos + obter_vida(uni) #soma da vida e os pontos
    return pontos

def simula_turno(mapa):
    """
    simula_turno: mapa -> mapa
    
    Funcao auxiliar que modifica o mapa fornecido como argumento de acordo com a simulacao de um turno de batalha completo,
    e devolve o proprio mapa. Isto e, seguindo a ordem de leitura do labirinto, cada unidade (viva) realiza um unico movimento e
(eventualmente) um ataque de acordo com as regras descritas.
    """    
    unidades = obter_todas_unidades(mapa)
    for uni in unidades: # Ver as unidades todas por ordem do mapa    
        if uni in obter_todas_unidades(mapa): #se nao foi eliminada no turno
            pos = obter_movimento(mapa,uni) #obter o movimento 
            if pos != obter_posicao(uni): #Se a posicao for diferente 
                mover_unidade(mapa,uni,pos) #Troca a posicao 
            pos = obter_movimento(mapa,uni) #obtem movimento
            if pos == obter_posicao(uni): #Se 
                adj = obter_inimigos_adjacentes(mapa,uni)#o primeiro adj
                if adj != ():
                    adj = adj[0]
                    if unidade_ataca(uni,adj) == True : #Se o outro morre
                        eliminar_unidade(mapa,adj) #Elimina-o
                        if obter_unidades_exercito(mapa,obter_exercito(adj)) == (): #Se o exercito morrer, acabar a batalha
                            break
    return mapa 
            
def simula_batalha(string,T_F):
    """
    simula_batalha: string x booleano -> str
    
    Funcao principal que permite simular uma batalha completa. A batalha termina quando
um dos exercitos vence ou, se apos completar um turno de batalha, nao ocorreu nenhuma
alteracao ao mapa e as unidades. A funcao simula batalha recebe uma cadeia de
caracteres e um valor booleano e devolve o nome do exercito ganhador. Em caso de
empate, a funcao deve devolver a cadeia de caracteres 'EMPATE'. A cadeia de caracteres
passada por argumento corresponde ao ficheiro de conguracao do simulador. O argumento
booleano ativa o modo verboso (True) ou o modo quiet (False). No modo quiet
mostra-se pela saida standard o mapa e a pontuacao no incio da simulacao e apos do
ultimo turno de batalha. No modo verboso, mostra-se tambem o mapa e a pontuacao
apos de cada turno de batalha.
    """        
    f1 = open(string,"r") #abri doc e ler cada linha 
    dim = eval(f1.readline())
    e1_misc = eval(f1.readline())
    e2_misc = eval(f1.readline())
    wall = eval(f1.readline())
    pose1 = eval(f1.readline())
    pose2 = eval(f1.readline())
    e1 = ()
    e2 = ()
    f1.close() #fechar doc
    for pos in pose1: #criar os exercitos com o cria unidades
        e1 = (cria_unidade(cria_posicao(pos[0],pos[1]),e1_misc[1],e1_misc[2],e1_misc[0]),) + e1
    for pos in pose2:
        e2 = (cria_unidade(cria_posicao(pos[0],pos[1]),e2_misc[1],e2_misc[2],e2_misc[0]),) + e2
        
    mapa = cria_mapa(dim,wall,e1,e2) #criar o mapa
    
    Empate = False
    Maior = False #ver o nome dos exercitos que aparece antes
    nom_e1 = e1_misc[0]
    nom_e2 = e2_misc[0]
    if nom_e1 < nom_e2:
        Maior = True
    print(mapa_para_str(mapa)) # print inicial dos mapas 
    if Maior == True: 
        print("[ " + str(nom_e1) + ":" + str(calcula_pontos(mapa,nom_e1)) + " " + str(nom_e2) + ":" + str(calcula_pontos(mapa,nom_e2)) +" ]")
    else:
        print("[ " + str(nom_e2) + ":" + str(calcula_pontos(mapa,nom_e2)) + " " + str(nom_e1) + ":" + str(calcula_pontos(mapa,nom_e1)) +" ]")
        
#####################################################################################################################################################
        
    while calcula_pontos(mapa,nom_e1) != 0 and calcula_pontos(mapa,nom_e2) != 0: #enquanto os pontos nao sao 0 
        mapa_antes = cria_copia_mapa(mapa)
        simula_turno(mapa)
        if mapas_iguais(mapa_antes,mapa): #Se os mapas sao iguais quer dizer que e empate
            Empate = True 
            break
        if T_F == True: #Dar print a cada turno se for true
            print(mapa_para_str(mapa))
            if Maior == True:
                print("[ " + str(nom_e1) + ":" + str(calcula_pontos(mapa,nom_e1)) + " " + str(nom_e2) + ":" + str(calcula_pontos(mapa,nom_e2)) +" ]")
            else:
                print("[ " + str(nom_e2) + ":" + str(calcula_pontos(mapa,nom_e2)) + " " + str(nom_e1) + ":" + str(calcula_pontos(mapa,nom_e1)) +" ]")

#####################################################################################################################################################
            
    if T_F == False: #Se for True nao e preciso dar o print final
        print(mapa_para_str(mapa))
        if Maior == True:
            print("[ " + str(nom_e1) + ":" + str(calcula_pontos(mapa,nom_e1)) + " " + str(nom_e2) + ":" + str(calcula_pontos(mapa,nom_e2)) +" ]")
        else:
            print("[ " + str(nom_e2) + ":" + str(calcula_pontos(mapa,nom_e2)) + " " + str(nom_e1) + ":" + str(calcula_pontos(mapa,nom_e1)) +" ]")
             
    if Empate == True: #Se for empate da print de EMPATE
        return ("EMPATE")
    else:
        if calcula_pontos(mapa,nom_e1) == 0: #Ver qual e o vencedor e da print do nome 
            return (nom_e2) 
        else:
            return (nom_e1)
        
