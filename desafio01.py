# DICAS SOBRE PYTHON:
# FUNÇÃO input(): Ela recebe como parâmetro uma String que será visível ao usuário, 
# onde geralmente informa que tipo de informação ele está esperando receber;
# FUNÇÃO print(): Ela é a responsável por imprimir os dados e informar os valores no terminal;
# MÉTODO split(): permite dividir o conteúdo da variável de acordo com as condições especificadas 
# em cada parâmetro da função ou com os valores predefinidos por padrão;

# Abaixo segue um exemplo de código que você pode ou não utilizar

n, x, y  = map(int, input().split())

icm = n / (x + y)

print("{:.2f}".format(icm)) 

# Todo: Calcule o ICM da comunicação dos Palatír de Sauron e Saruman, com 2 casas decimais no espaço #em branco abaixo: