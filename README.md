# Calculadora Python

Seja Bem-vindo! 👋 

Este projeto consiste no desenvolvimento de uma calculadora simples em Python, capaz de realizar as quatro operações matemáticas básicas: *soma*, *subtração*, *multiplicação* e *divisão*. 

A aplicação permite ao usuário inserir dois números e escolher a operação desejada. Após exibir o resultado, o usuário pode optar por realizar outra operação ou encerrar o programa. 

A interface de interação é simples e intuitiva, utilizando comandos de texto para continuidade (digitando "S" para continuar ou "N" para sair). 

## Especificações

*Objetivo do projeto:*

Desenvolver uma calculadora em Python que permite realizar operações matemáticas básicas (soma, subtração, multiplicação e divisão) entre dois números.

*Funcionalidade principal:*
O usuário deve ser capaz de inserir dois números e escolher a operação matemática que deseja realizar entre elas.

*Repetição do processo:*
A aplicação deve permitir que o usuário repita as operações quantas vezes quiser, podendo escolher realizar uma nova operação ou repetir uma operação anterior.

*Interação do usuário:*
O usuário pode optar por continuar realizando operações ou encerrar a aplicação, com as seguintes opções:
- Digitar "S" para continuar realizando operações.
- Digitar "N" para sair da aplicação.

![alt text](image-1.png)

# Explicação do Código

Na linha 1 é realizado o import da Biblioteca Colorama, seguido pela sua inicialização na linha 4.

Criei uma função principal chamada `calculadora`, na linha7. Adicionei um loop `While`, na linha 9, para que a calculadora fique em execução.

Nas linhas 11, 12 e 13, adicionei um cabeçalho para organizar melhor a calculadora de forma visual. Também podemos ver a utilizadação do `Fore.CYAN` e `Fore.YELLOW` onde é definido a cor do texto.

Na linha 16 adicionei um bloco try caso ocorra algo com a entrada informada, ele irá exibir uma mensagem de erro, sendo executado a linha 19 e 20 o except ValueError. 

Nas linhas 17 e 18, temos duas variáveis `num1`e `num2` do tipo float(número com casas decimais) e solicitamos com o `input()` a entrada dos números.



# Bibliotecas Utilizadas

- Colorama

# Ferramentas

- Visual Studio Code

# Documentação

[Documentação do Python](https://docs.python.org/pt-br/3/tutorial/index.html)

[Colorama](https://pypi.org/project/colorama/)


______________________

Feito de 💜 por Aline Antunes
