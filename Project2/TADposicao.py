#TAD Posicao
#Construtor
def cria_posicao(x,y):
    if isinstance(x,int) and isinstance(y,int): #Tem que ser inteiros
        if x >= 0 and y >= 0: #Maiores que zero
            return (x,y) #Devolve um tuplo
        else:
            raise ValueError ("cria_posicao: argumentos invalidos")
    else:
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
        


    