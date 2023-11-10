import networkx as nx
import matplotlib.pyplot as plt

class Automaton:
    def __init__(self, word):
        # Inicializa o autômato com a palavra a ser encontrada
        self.word = word
        # O estado inicial é 0
        self.initial_state = 0
        # O estado final é o comprimento da palavra
        self.final_state = len(word)
        # Inicializa o estado atual como o estado inicial
        self.current_state = self.initial_state
        # Inicializa a lista de transições como uma lista vazia
        self.transitions = []

    def add_transition(self, source_state, destination_state, character):
        # Adiciona uma transição à lista de transições
        self.transitions.append((source_state, destination_state, character))

    def transition(self, character):
        # Procura na lista de transições por uma transição que corresponda ao estado atual e ao caractere
        for transition in self.transitions:
            if transition[0] == self.current_state and transition[2] == character:
                return transition[1]
        # Se nenhuma transição corresponder, retorna 0
        return 0

    def process(self, text):
        # Inicializa a lista de índices onde a palavra foi encontrada
        indices = []

        # Itera por todos os caracteres no texto
        for i, character in enumerate(text):
            # Atualiza o estado atual com base na transição
            self.current_state = self.transition(character)

            # Se o estado atual for o estado final, adiciona o índice à lista
            if self.current_state == self.final_state:
                indices.append(i - self.final_state + 1)

            # Imprime o estado atual e o caractere para cada iteração
            print(f"Estado Atual: {self.current_state}, Caractere: {character}")

        # Retorna a lista de índices
        return indices

    def visualize(self):
        # Cria um grafo
        G = nx.DiGraph()

        # Adiciona os estados ao grafo
        for i in range(self.final_state + 1):
            G.add_node(i)

        # Adiciona as transições ao grafo
        for transition in self.transitions:
            G.add_edge(transition[0], transition[1], label=transition[2])

        pos = nx.spring_layout(G)
        nx.draw_networkx_nodes(G, pos)
        nx.draw_networkx_labels(G, pos)
        nx.draw_networkx_edges(G, pos)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, 'label'))
        plt.show()

def main():
    text = "O computador é uma máquina capaz de variados tipos de tratamento automático de informações ou processamento de dados. Entende-se por computador um sistema físico que realiza algum tipo de computação. Assumiu-se que os computadores pessoais e laptops são ícones da era da informação. O primeiro computador eletromecânico foi construído por Konrad Zuse (1910–1995). Atualmente, um microcomputador é também chamado computador pessoal ou ainda computador doméstico."

    automaton = Automaton("computador")
    for i in range(len(automaton.word)):
        automaton.add_transition(i, i + 1, automaton.word[i])
    indices = automaton.process(text)

    print("A palavra 'computador' foi encontrada nas seguintes posições:", indices)

    print("Estado Inicial:", automaton.initial_state)
    print("Estado Final:", automaton.final_state)

    automaton.visualize()

if __name__ == "__main__":
    main()
