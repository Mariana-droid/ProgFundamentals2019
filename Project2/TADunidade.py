#TAD Posicao
#Construtor
def cria_posicao(x,y):
    if isinstance(x,int) and isinstance(y,int): #Tem que ser inteiros
        if x >= 0 and y >= 0: #Maiores que zero
            return (x,y) #Devolve um tuplo
    raise ValueError ("cria_posicao: argumentos invalidos")

def cria_copia_posicao(pos): 
    if isinstance(pos,tuple) and len(pos) == 2: #Tem que ser tuplo e len = 2
        if isinstance(pos[0],int) and isinstance(pos[1],int): #Tem que ser inteiros
            if pos[0] >= 0 and pos[1] >= 0: #E maiores que zero
                return pos
    raise ValueError ("cria_copia_posicao: argumentos invalidos")

#Seletores

def obter_pos_x(pos):
    return pos[0]

def obter_pos_y(pos):
    return pos[1]

#reconhecedor

def eh_posicao(pos):
    if isinstance(pos,tuple) and len(pos) == 2: #Tem que ser tuplo e len = 2
        if isinstance(pos[0],int) and isinstance(pos[1],int): #Tem que ser inteiros
            if pos[0] >= 0 and pos[1] >= 0: #E maiores que zero
                return True
    return False

#Teste

def posicoes_iguais(pos1,pos2):
    if pos1 == pos2: #Se for igual return True
        return True
    else:
        return False

#Transformador

def posicao_para_str(pos):
    return str(pos) #poe em string

#Funcao de alto nivel

def obter_posicoes_adjacentes(pos):
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

def cria_unidade(pos,vida,forca,exercito):
    if eh_posicao(pos) == True and isinstance(vida,int) and isinstance(forca,int) and isinstance(exercito,str): #Verficiao do tipo
        if vida > 0 and forca > 0 and " " not in exercito: #forca e vida maior que zero e exercito nao tem espacos
            if exercito == "": #exercito nao pode ser vazia
                raise ValueError ("cria_unidade: argumentos invalidos")
            else:
                return { "pos" : pos, "vida" : vida, "forca" : forca, "exercito" : exercito}
    raise ValueError ("cria_unidade: argumentos invalidos")

def cria_copia_unidade(unidade):
    if isinstance(unidade,dict) and len(unidade) == 4: #Ve se e dicionario e len = 4
        if "pos" in unidade and "vida" in unidade and "forca" in unidade and "exercito" in unidade: #ve se existem as chaves com os nomes certos
            if eh_posicao(unidade["pos"]) and isinstance(unidade["vida"],int) and isinstance(unidade["forca"],int) and isinstance(unidade["exercito"],str): #Verifica os tipos
                if unidade["exercito"] == "": #verifica se nao e vazia
                    raise ValueError ("cria_copia: argumento invalido")
                elif unidade["vida"] > 0 and unidade["forca"] > 0 and " " not in unidade["exercito"]: #vida e forca maior que zero e sem espacos no unidade 
                    return cria_unidade(unidade["pos"],unidade["vida"],unidade["forca"],unidade["exercito"])  
    raise ValueError ("cria_copia: argumento invalido")

#Seletores

def obter_posicao(unidade):  #obtem a posicao do dicionario
    return unidade["pos"]

def obter_exercito(unidade): #obtem o exercito do dicionario
    return unidade["exercito"]

def obter_forca(unidade): #obtem a forca do dicionario
    return unidade["forca"]

def obter_vida(unidade): #obtem a vida do dicionario
    return unidade["vida"]

#modificadores

def muda_posicao(unidade,pos):
    unidade["pos"] = pos #Trocar as pos no dicionario
    return unidade

def remove_vida(unidade,vidaatirar):
    unidade["vida"] = unidade["vida"] - vidaatirar # subtrair e trocar a vida 
    return unidade

#reconhecedor

def eh_unidade(unidade):
    if isinstance(unidade,dict) and len(unidade) == 4: # Ve se e dicionario de tamanho 4
        if "pos" in unidade and "vida" in unidade and "forca" in unidade and "exercito" in unidade: #verificar se existem as chaves 
            if eh_posicao(obter_posicao(unidade)) and isinstance(obter_vida(unidade),int) and isinstance(obter_forca(unidade),int) and isinstance(obter_exercito(unidade),str): #verificar os tipos 
                if obter_exercito(unidade) == "": #string pode ser vazia
                    return False
                elif obter_vida(unidade) > 0 and obter_forca(unidade) > 0 and " " not in obter_exercito(unidade):  #vida e forca maior que zero e sem espacos na string 
                    return True
    return False

#Teste

def unidades_iguais(unidade1,unidade2):
    if unidade1 == unidade2:
        return True
    else:
        return False
    
#transformadores

def unidade_para_char(unidade):
    return obter_exercito(unidade)[0].upper()   

def unidade_para_str(unidade):
    return unidade_para_char(unidade) + str((obter_vida(unidade),obter_forca(unidade))) + "@" + str(obter_posicao(unidade))

#Funcoes de Alto Nivel

def unidade_ataca(u1,u2):
    remove_vida(u2,obter_forca(u1)) #Remocao da vida
    return obter_vida(u2) <= 0 #devolver True se for destruida
    
def ordenar_unidades(tuplo):
    tuplo = list(tuplo) #Transforma em lista
    tuplo = sorted(tuplo,key = lambda x: x["pos"]) #Sort por posicao
    tuplo = tuple(tuplo) #Transforma em tuplo
    return tuplo
    
    
#Tad Mapa
#Construtores

def cria_mapa(dim,wall,e1,e2):
    if isinstance(dim,tuple) and isinstance(wall,tuple) and isinstance(e1,tuple) and isinstance(e2,tuple): #Verifica o tipo dos dados
            for a in dim:
                if not isinstance(a,int) or a < 3: #Ve se a dimensao e inteiro maior ou igual a 3x3
                    raise ValueError ("cria_mapa: argumentos invalidos")
            for pos in wall: 
                if eh_posicao(pos) == False: #Ve se sao posicoes 
                    raise ValueError ("cria_mapa: argumentos invalidos")
                elif pos[0] == 0 or pos[1] == 0 or pos[0] >= dim[0] or pos[1] >= dim[1]: #Nao parede e dentro do mapa
                    raise ValueError ("cria_mapa: argumentos invalidos")
            for tuplo_com_uni in (e1,e2): #ve nos dois exercitos 
                for unidade in tuplo_com_uni:
                    if eh_unidade(unidade) == False: #Se os componentes sao todos unidades
                        raise ValueError ("cria_mapa: argumentos invalidos")
            return {"dim" : dim, "wall" : wall, "e1" : e1, "e2" : e2} #Devolve em dicionario
    raise ValueError ("cria_mapa: argumentos invalidos")

def cria_copia_mapa(mapa): #Cria copia do mapa
    if isinstance(mapa,dict):
        return cria_mapa(mapa["dim"],mapa["wall"],mapa["e1"],mapa["e2"])
    
#Seletores

def obter_tamanho(mapa):
    return mapa["dim"]

def obter_nome_exercitos(mapa):
    res = (obter_exercito(mapa["e1"][0]),obter_exercito(mapa["e2"][0])) #Obtem o nome dos dois exercitos
    res = list(res)
    res = sorted(res) #organiza
    res = tuple(res)
    return res

def obter_unidades_exercito(mapa,string): 
    if obter_exercito(mapa["e1"][0]) == string: #Ve se o e1 e o da string 
        return ordenar_unidades(mapa["e1"]) #devolve unidades organizadas
    else:
        return ordenar_unidades(mapa["e2"]) #Devolve unidades organizadas do e2

def obter_todas_unidades(mapa):
    tuplo = ()
    for e1 in mapa["e1"]: 
        tuplo = tuplo + (e1,) #Coloca as unidades todas do e1 num tuplo
    for e2 in mapa["e2"]:
        tuplo = tuplo + (e2,) #Coloca as unidades todas do e2 num tuplo
    return ordenar_unidades(tuplo) #ordena

def obter_unidade(mapa,pos):
    for exercito in (mapa["e1"],mapa["e2"]): #ve nos dois exercitos
        for posicao in exercito:
            if obter_posicao(posicao) == pos: #se a posicao e igual ao pos
                return exercito #devolve a unidade 

#Modificadores

def eliminar_unidade(mapa,unidade):
    for e in ("e1","e2"): #Dentro dos dois exercitos 
        if obter_exercito(unidade) == obter_exercito(mapa[e][0]): #Ver se o nomes sao iguais
            for unidadenum in range(len(mapa[e])): 
                if mapa[e][unidadenum] == unidade: #Se as unidades forem iguais
                    mape = list(mapa[e]) #criar um mape que e transformado em lista
                    del(mape[unidadenum]) #Delete da unidade do mape 
            mapa[e] = tuple(mape) # mapa[e] e subsitituido
            
def mover_unidade(mapa,uni,posicao):
    for e in ("e1","e2"): #ver os dois exercitos
        if obter_exercito(uni) == obter_exercito(mapa[e][0]): #naquele cujo o nome e igual
            for num_unidade in range(len(mapa[e])): 
                if mapa[e][num_unidade] == uni: #Quando as unidades forem iguais 
                    muda_posicao(mapa[e][num_unidade],posicao) #trocar a unidade 

#Reconhecedores

def eh_posicao_unidade(mapa,posicao): 
    tuplo = obter_todas_unidades(mapa) #obter as unidades num tuplo 
    for unidade in tuplo: 
        if obter_posicao(unidade) == posicao: #Se as posicoes forem iguais
            return True #da True
    return False

def eh_posicao_corredor(mapa,posicao):
    for corredor in mapa["wall"]: #ver no tuplo da wall 
        if corredor == posicao: #Se a posicao e corredor 
            return True #Da true
    return False
        
def eh_posicao_parede(mapa,posicao): 
    dim = obter_dim(mapa) 
    if posicao[0] == 0 or posicao[1] == 0 or posicao[0] == dim[0] or posicao[1] == dim[1]: #Paredes
        return True
    return False

#Teste

def mapas_iguais(mapa1,mapa2):
    if mapa1 == mapa2:
        return True
    return False

#Transformador

def mapa_para_str(mapa):
        stri = ""
        