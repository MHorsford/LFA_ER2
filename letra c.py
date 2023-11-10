class FiniteAutomaton:
    def __init__(self):
        self.states = {'q0q1q2', 'q1q4', 'q3', 'q3q4', 'q4'}
        self.initial_state = 'q0q1q2'
        self.final_states = {'q1q4', 'q3', 'q3q4', 'q4'}
        self.transitions = {
            ('q0q1q2', 'a'): 'q1q4',
            ('q0q1q2', 'b'): 'q3',
            ('q1q4', 'a'): 'q1',
            ('q1q4', 'b'): 'q3q4',
            ('q1', 'a'): 'q1',
            ('q1', 'b'): 'q3',
            ('q3q4', 'b'): 'q4',
            ('q4', 'b'): 'q4'
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

inputs = ['aaab', 'b', 'a', 'abbbb', 'aa', 'aac', 'abaaa']
for input_str in inputs:
    result = automaton.process_input(input_str)
    print(f'The input "{input_str}" is accepted: {result}')
