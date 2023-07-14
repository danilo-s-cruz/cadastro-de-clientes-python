'''
FUNÇÕES PROGRAMA CLIENTES
'''
def gerar_codigo(db:list):
    if len(db) > 0:
        codigo = db[-1]['codigo']
        novo_codigo = int(codigo) + 1
        return str(novo_codigo)
    return '1'

# Verifica se o código da lista de dados, existe.
def codigo_existe(bd:list, codigo:str):
  for i in range(len(bd)):
    if bd[i]["codigo"] == codigo:
      return str(i)
  return str(-1)

def incluir(db:list, cod:str, nome:str, end:str, tipo:str, pfpj:str):
    db.append({
                'codigo':cod,
                'nome':nome,
                'endereco':end,
                'tipo':tipo,
                'cpf_cnpj':pfpj,
                })
    return 'Cliente cadastrado com sucesso!'

def alterar(db:list, cod:str):
    for cliente in db:
            if cliente['codigo'] == cod:
                novo_end = input('Digite o Novo endereço: ')
                cliente["endereco"] = novo_end
                return 'Endereço atualizado com sucesso!'

def excluir(db:list, cod:str):
    for cliente in range(len(db)):
        if db[cliente]['codigo'] == cod:
            conf = input('Deseja realmente excluir? [S/N]').strip().upper()
            if conf != 'S':
                return 'Exclusão Cancelada!'   
            else: 
                del db[cliente]
                return 'Cliente excluído com sucesso!'

def listar_filtro(db:list):
    tipo = input('Pessoa [F]ísica ou [J]urídica: ').strip().upper()
    filtrado = tuple(filter(lambda cliente: cliente['tipo'] == tipo, db))
    return filtrado