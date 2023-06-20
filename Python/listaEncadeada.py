"""""
Algo muito importante a se entender, é que na lista comum quando eu preciso crescer a minha lista, eu preciso recriar, pois ela já é definida quando criada,
se tornando um valor fixo a alocação de memória inicial.
Jááááá, na lista encadeada, os valores nao sao sequenciais, mas espalhadas nos espaços de memória do computador. O encadeamento serve para linkar os valores para que eles
parecçam estar em sequencia, mas na verdade eles utilizam um ponteiro para referenciar o próximo valor da lista.
Isso ajuda a "economizar espaço", pois nao precisa se alocar uma quantidade de espaço a mais para adicionar valores posteriores, a lista cresce a medida que eu vou
adicionando valores na lista.

Obs: como os valores estão a locados em diferentes espaços, nao podemos usar o indice como parametro, mas sim o nó(ponteiro) para unir os dados da lista.

IMPORTANTE: Embora uma lista encadeada tenha uma organização interna diferente no que desrespeita a alocação de memória e o funcionamento de algumas operações, ela ainda
é uma lista. Então, é importante que ela ofereça operações semelhantes aquela que estamos acostumados a usar na lista sequencial.
em outras palavras, uma lista de alocação sequencial e uma lista encadeada compartilham uma intrface em comum, ou seja, a forma como interagimos com elas é a mesma independente da implementação.
Essas difereças internas irão se manifestar apenas na complexidade das operações que são realizadas com essas listas (seq. e encad.) e ai dependedo do problema ser mais eficiente usar uma ou outra.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
