class FiniteAutomaton:
    def __init__(self):
        self.states = {'q0', 'q1', 'q2', 'q3'}
        self.initial_state = 'q0'
        self.final_states = {'q0', 'q1', 'q2', 'q3'}
        self.transitions = {
            ('q0', 'a'): 'q1',
            ('q1', 'a'): 'q1',
            ('q1', 'b'): 'q2',
            ('q1', 'c'): 'q3',
            ('q2', 'a'): 'q1',
            ('q2', 'b'): 'q2',
            ('q2', 'c'): 'q3',
            ('q3', 'a'): 'q1',
            ('q3', 'c'): 'q3'
        }

    def process_input(self, input_string):
        current_state = self.initial_state
        for symbol in input_string:
            transition = (current_state, symbol)
            if transition in self.transitions:
                current_state = self.transitions[transition]
            else:
                return False  # Undefined transition for the symbol
        return current_state in self.final_states


automaton = FiniteAutomaton()

inputs = ['a', 'abc', 'aaaaaaa', 'babca', 'cbca']
for input_str in inputs:
    result = automaton.process_input(input_str)
    print(f'The input "{input_str}" is accepted: {result}')
