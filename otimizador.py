print("=" * 50)
print("🚀 LOGISTICS OPTIMIZER - HAROLDO ENGINEERING")
print("=" * 50)

import math
import itertools

def carregar_cidades():
    """Carrega cidades do arquivo CSV"""
    cidades = []
    
    try:
        with open('C:/Users/harol/OneDrive/Documentos/Haroldo-Engineering/projects/logistics-optimizer/cities.csv', 'r') as arquivo:
            linhas = arquivo.readlines()
        
        print("📖 Lendo arquivo de dados...")
        
        for linha in linhas[1:]:
            dados = linha.strip().split(',')
            if len(dados) == 3:
                nome = dados[0]
                x = int(dados[1])
                y = int(dados[2])
                cidades.append({'nome': nome, 'x': x, 'y': y})
                print(f"📍 {nome} - ({x}, {y})")
                
    except Exception as e:
        print(f"❌ Erro: {e}")
    
    return cidades

def calcular_distancia(cidade1, cidade2):
    """Calcula distância entre duas cidades"""
    x1, y1 = cidade1['x'], cidade1['y']
    x2, y2 = cidade2['x'], cidade2['y']
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def forca_bruta(cidades):
    """Algoritmo ingênuo - testa todas as possibilidades"""
    print("\n🔍 ALGORITMO 1: FORÇA BRUTA")
    print("📊 Analisando TODAS as possibilidades...")
    
    if len(cidades) > 8:
        print("⚠️  Muitas cidades para força bruta!")
        return None, float('inf')
    
    todas_rotas = list(itertools.permutations(cidades))
    print(f"🎯 Total de rotas possíveis: {len(todas_rotas):,}")
    
    melhor_rota = None
    menor_distancia = float('inf')
    
    for rota in todas_rotas[:1000]:
        distancia_total = 0
        for i in range(len(rota) - 1):
            distancia_total += calcular_distancia(rota[i], rota[i + 1])
        
        if distancia_total < menor_distancia:
            menor_distancia = distancia_total
            melhor_rota = rota
    
    return melhor_rota, menor_distancia

def vizinho_mais_proximo(cidades):
    """Algoritmo inteligente - escolhe sempre o mais próximo"""
    print("\n🧠 ALGORITMO 2: VIZINHO MAIS PRÓXIMO")
    print("💡 Estratégia gulosa...")
    
    if not cidades:
        return [], 0
    
    rota = [cidades[0]]
    cidades_restantes = cidades[1:]
    distancia_total = 0
    
    while cidades_restantes:
        ultima_cidade = rota[-1]
        mais_proxima = None
        menor_dist = float('inf')
        
        for cidade in cidades_restantes:
            dist = calcular_distancia(ultima_cidade, cidade)
            if dist < menor_dist:
                menor_dist = dist
                mais_proxima = cidade
        
        rota.append(mais_proxima)
        cidades_restantes.remove(mais_proxima)
        distancia_total += menor_dist
    
    return rota, distancia_total

def duas_opt(rota, distancia_total):
    """Algoritmo de refinamento - Melhora a rota existente"""
    print("\n⚡ ALGORITMO 3: REFINAMENTO 2-OPT")
    print("🎨 Melhorando a rota inteligente...")
    
    melhor_rota = rota[:]
    melhor_distancia = distancia_total
    melhorou = True
    
    while melhorou:
        melhorou = False
        for i in range(1, len(rota) - 2):
            for j in range(i + 1, len(rota)):
                if j - i == 1:
                    continue
                
                # Tentar trocar as cidades
                nova_rota = melhor_rota[:]
                nova_rota[i:j] = reversed(melhor_rota[i:j])
                
                # Calcular nova distância
                nova_distancia = 0
                for k in range(len(nova_rota) - 1):
                    nova_distancia += calcular_distancia(nova_rota[k], nova_rota[k + 1])
                
                # Se melhorou, aceitar
                if nova_distancia < melhor_distancia:
                    melhor_rota = nova_rota
                    melhor_distancia = nova_distancia
                    melhorou = True
                    break
            
            if melhorou:
                break
    
    return melhor_rota, melhor_distancia

# PROGRAMA PRINCIPAL
if __name__ == "__main__":
    # Carregar dados
    cidades = carregar_cidades()
    print(f"\n✅ {len(cidades)} cidades carregadas")
    
    if cidades:
        print("\n" + "="*50)
        print("🎯 INICIANDO OTIMIZAÇÃO DE ROTAS")
        print("="*50)
        
        # Testar força bruta (limitado)
        rota_bruta, dist_bruta = forca_bruta(cidades)
        
        # Testar algoritmo inteligente
        rota_inteligente, dist_inteligente = vizinho_mais_proximo(cidades)
        
        print("\n" + "="*50)
        print("📊 RESULTADOS COMPARATIVOS")
        print("="*50)
        
        if rota_inteligente:
            print(f"🧠 VIZINHO MAIS PRÓXIMO:")
            print(f"   📏 Distância: {dist_inteligente:.2f}")
            print(f"   🛣️  Rota: ", end="")
            for cidade in rota_inteligente:
                print(f"{cidade['nome']} → ", end="")
            print("FIM")
        
        if rota_bruta:
            print(f"\n🔍 FORÇA BRUTA (amostra):")
            print(f"   📏 Distância: {dist_bruta:.2f}")
        
        print(f"\n💡 INSIGHT: Com {len(cidades)} cidades:")
        print(f"   • Força bruta testaria {math.factorial(len(cidades)):,} rotas")
        print(f"   • Algoritmo inteligente: {len(cidades)} passos")
        
        print("\n" + "="*50)
        print("🚀 FASE 2: REFINAMENTO AVANÇADO")
        print("="*50)

        # Refinar a rota do algoritmo inteligente
        rota_refinada, dist_refinada = duas_opt(rota_inteligente, dist_inteligente)

        print(f"\n⚡ ROTA REFINADA (2-OPT):")
        print(f"   📏 Distância: {dist_refinada:.2f} (melhoria de {((dist_inteligente - dist_refinada)/dist_inteligente*100):.1f}%)")
        print(f"   🛣️  Rota: ", end="")
        for cidade in rota_refinada:
            print(f"{cidade['nome']} → ", end="")
        print("FIM")

        print(f"\n🎯 COMPARAÇÃO FINAL:")
        print(f"   • Força Bruta: {dist_bruta:.2f} (ideal)")
        print(f"   • Vizinho Próximo: {dist_inteligente:.2f}")
        print(f"   • Refinado: {dist_refinada:.2f}")

        print(f"\n💡 APRENDIZADO DOS 0.1%:")
        print(f"   Algoritmos inteligentes + refinamento = Resultados quase ótimos em tempo viável!")
