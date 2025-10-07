print('=' * 50)
print('🚀 LOGISTICS OPTIMIZER - HAROLDO ENGINEERING')
print('=' * 50)

def carregar_cidades():
    '''Carrega cidades do arquivo CSV'''
    print('📖 Lendo arquivo de dados...')
    
    try:
        with open('cities.csv', 'r') as arquivo:
            linhas = arquivo.readlines()
        
        cidades = []
        for linha in linhas[1:]:  # Pular cabeçalho
            dados = linha.strip().split(',')
            if len(dados) == 3:
                nome, x, y = dados
                cidades.append({
                    'nome': nome,
                    'x': int(x),
                    'y': int(y)
                })
                print(f'📍 {nome} - ({x}, {y})')
        
        return cidades
        
    except FileNotFoundError:
        print('❌ Arquivo cities.csv não encontrado!')
        return []

# EXECUTAR
if __name__ == '__main__':
    cidades = carregar_cidades()
    print(f'\n✅ {len(cidades)} cidades carregadas com sucesso!')
    print('🎯 Próximo passo: Implementar algoritmo de otimização!')
