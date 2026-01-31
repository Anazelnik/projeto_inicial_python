---
marp: true
theme: uncover
paginate: true
---

## Aula de programação orientada a objetos
- Classe
Exemplo **(Pessoa)**

- O que é INSTANCIAR? 
**Criar algo real a partir da classe**
Classe pronta
p1 = Pessoa()
**Toda vez que usamos Classe(), você está instanciando.**
**p1 -> pessoa real criada a partir da classe**

- Atributos são características - nome, idade, altura
- Métodos são ações / comportamentos
Método é uma função dentro da classe **(sempre passamos o self como primeiro parâmetro)**

## Métodos utilizados na aula 02 em POO
- Método __init__ é o construtor da classe, chamado quando uma nova instância é criada
- Método __str__ define a representação em string do objeto
- Métodos de classe (como listar_restaurantes) são chamados na própria classe, não na instância
- dir mostra todos os atributos e métodos de um objeto
- vars mostra os atributos de um objeto em forma de dicionário
- self representa a própria instância do objeto
- @property permite definir métodos que podem ser acessados como atributos
- Métodos e atributos privados são indicados por um underscore (_) no início do nome
- title() e upper() são métodos de string para formatar texto / tittle > Primeira letra maiúscula / upper > Tudo maiúsculo
- ljust() alinha o texto à esquerda com um comprimento especificado
- @classmethod indica que o método pertence à classe e não à instância