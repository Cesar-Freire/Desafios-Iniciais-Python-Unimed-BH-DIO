# DICAS SOBRE PYTHON:
# FUNÇÃO input(): Ela recebe como parâmetro uma String que será visível ao usuário, 
# onde geralmente informa que tipo de informação ele está esperando receber;
# FUNÇÃO print(): Ela é a responsável por imprimir os dados e informar os valores no terminal;
# MÉTODO split(): permite dividir o conteúdo da variável de acordo com as condições especificadas 
# em cada parâmetro da função ou com os valores predefinidos por padrão;

# Abaixo segue um exemplo de código que você pode ou não utilizar

tempo_gasto, velocidade_media = map(int, input().split())

quantidade_de_litros = (tempo_gasto * velocidade_media) / 12

print("{:.3f}".format(quantidade_de_litros))

# TODO:  Calcule quantidade de litros necessária para realizar a viagem e imprima com TRÊS dígitos após o ponto decimal