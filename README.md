# string-to-number

📓Descrição:

Este programa converte números escritos por extenso (em português) para sua representação em algarismos numéricos. O sistema inclui um mecanismo de correção que permite identificar e corrigir pequenos erros de digitação nos números escritos.

✅Funcionalidades:

    Converte números por extenso ex: "dois mil e quinhentos" -> 2,500
    ou "quato milhoes e quatrocentos sesssenta" -> 4,000,460
    Corrige automaticamente pequenos erros de ortografia ou digitação
    Suporta números inteiros de 0 a 999.999 (e além, dependendo da configuração)
    Opcionalmente utiliza o pacote python-Levenshtein para melhor performance na correção
    
✅Pré-requisitos:

    Python 3.x
    (Opcional) python-Levenshtein para melhor performance na correção de erros:
    pip install python-Levenshtein

😭Limitações:

    Atualmente suporta apenas números inteiros positivos de 1 até 999,999,999
    Não há correção de números inexistentes, como "trinta e treze"
    A correção de erros pode não funcionar para erros muito grandes
    O desempenho pode diminuir para números muito extensos
