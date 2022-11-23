#Importa nosso arquivo Pessoa.py no diretório model
from model.Pessoa import Pessoa

#Exemplo de uso
fran = Pessoa(1, "Francislaine")
print(fran)

#Quero mostrar só nome
print(fran.nome)