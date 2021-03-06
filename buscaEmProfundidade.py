from itertools import permutations
import functions as ft

caracteristicas = {}
caracteristicas["cor"] = ["amarela", "azul", "vermelha", "verde", "branca"]
caracteristicas["nacionalidade"] = ["norueguês", "dinamarquês", "inglês", "alemão", "sueco"]
caracteristicas["bebida"] = ["água", "café", "leite" ,"chá", "cerveja"]
caracteristicas["cigarro"] = ["dunhill", "bluemaster", "blends", "pall mall", "prince"]
caracteristicas["animal"] = ["cavalos", "gatos", "cachorros", "pássaros", "peixes"]


def insert(m, key, combinacoes, elementos):
    for i in range(5):
        m[key].append(elementos[combinacoes[i]])


permList = []
genComb = permutations([0, 1, 2, 3, 4], 5)
for subset in genComb:
     permList.append(subset)


m= {}
tam = len(permList)
resolvido = 0
for c1 in range(tam):
    m["cor"] = []
    insert(m, "cor", permList[c1], caracteristicas["cor"])
    for c2 in range(tam):
        m["nacionalidade"] = []
        insert(m, "nacionalidade", permList[c2], caracteristicas["nacionalidade"])
        for c3 in range(tam):
            m["bebida"] = []
            insert(m, "bebida", permList[c3], caracteristicas["bebida"])
            for c4 in range(tam):
                m["cigarro"] = []
                insert(m, "cigarro", permList[c4], caracteristicas["cigarro"])
                for c5 in range(tam):
                    m["animal"] = []
                    insert(m, "animal", permList[c5], caracteristicas["animal"])
                    #print(ft.fitnessByRules(m))
                    if(ft.fitnessByRules(m)>=15):
                        for key in m:
                            print(m[key])
                        #print(m)
                        print(ft.fitnessByRules(m))
                        resolvido = 1
                        break
                if(resolvido):
                    break
            if (resolvido):
                break
        if(resolvido):
            break
    if(resolvido):
        break


