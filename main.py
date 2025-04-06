from fuzzywuzzy import fuzz
# python-Levenshtein package para melhor performance
# input: tres milhoes
# output: 3,000,000
#
# com erros ->
# input: quientos mil e oitossentos e trinta e dois
# output: 500,832

def verify_correlation(string = str, possibilities = []):
    best_fuzzy = []
    for group in possibilities:
        for word in group:
            similarity = fuzz.ratio(string, word)
            best_fuzzy.append((similarity, word))
    best_fuzzy.sort(key=lambda x: x[0], reverse=True)
    #print(f"corrigido -> {best_fuzzy[0][1]}")
    return best_fuzzy[0][1] # melhor correspondencia

if __name__ == '__main__':
    unidade = {"um": 1, "dois": 2, "tres": 3, "quatro": 4, "cinco": 5,
               "seis": 6, "sete": 7, "oito": 8, "nove": 9}
    unidade_dezena = {"onze": 11, "doze":12, "treze": 13, "quatorze": 14, "quinze": 15,
                      "dezesseis": 16, "dezessete": 17, "dezoito": 18, "dezenove": 19}
    dezena = {"dez": 10, "vinte": 20, "trinta": 30, "quarenta": 40, "cinquenta": 50,
              "sessenta": 60, "setenta": 70, "oitenta": 80, "noventa": 90}
    centena = {"cento": 100,"duzentos": 200, "trezentos": 300, "quatrocentos": 400, "quinhentos":500,
               "seiscentos": 600, "setecentos": 700, "oitocentos": 800, "novecentos": 900}
    milhar = {"mil": 1000}
    milhao = {"milhao": 1000000, "milhoes": 1000000}

    input = str(input("input: "))

    words = input.split()
    result = 0
    result_milhao = 0 # tem de ser tratado de uma maneira diferente
    cont = 0
    lista = list((unidade.keys(),dezena.keys(),unidade_dezena.keys(),centena.keys(),milhar.keys(),milhao.keys()))
    word = words[cont]
    while True:
        if word == "e":
            cont += 1
            word = words[cont]
            continue
        elif word.lower() in unidade:
            if (cont + 1 >= len(words) or words[cont + 1].lower() not in milhar or words[cont + 1].lower() not in milhao
                    or cont == 0):
                result += unidade[word]
            else:
                result *= unidade[word]
        elif word.lower() in unidade_dezena:
            if words[cont + 1].lower() not in milhar or words[cont + 1].lower() not in milhao or cont == 0:
                result += unidade_dezena[word]
            else:
                result *= unidade_dezena[word]
        elif word.lower() in dezena:
            result += dezena[word]
        elif word.lower() in centena:
            result += centena[word]
        elif word.lower() in milhar:
            if cont == 0:
                result += milhar[word]
            else:
                result *= milhar[word]
        elif word.lower() in milhao:
            result *= milhao[word]
            result_milhao += result
            result = 0
        else:
            word = verify_correlation(word.lower(), lista)
            continue
        cont+=1
        if cont >= len(words): break
        word=words[cont]

    result += result_milhao
    result = str(result)
    # coloca as vírgulas
    for pos in range(len(result), 0, -3):
        if pos != len(result):
            result = result[:pos] + ',' +result[pos:]

    print(f"output: {result}")