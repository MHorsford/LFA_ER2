class FiniteAutomaton:
    def __init__(self):
        self.states = {'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7'}
        self.initial_state = 'q0'
        self.final_states = {'q3', 'q7'}
        self.transitions = {
            ('q0', 'a'): 'q1',
            ('q0', 'b'): 'q4',
            ('q0', 'c'): 'q4',
            ('q1', 'a'): 'q2',
            ('q2', 'a'): 'q3',
            ('q3', 'b'): 'q3',
            ('q3', 'c'): 'q3',
            ('q4', 'a'): 'q5',
            ('q4', 'b'): 'q4',
            ('q4', 'c'): 'q4',
            ('q5', 'a'): 'q6',
            ('q6', 'a'): 'q7'
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


inputs = ['aaabcbcbc', 'bcbcbcaaa', 'aaa', 'aac', 'abaaa', 'aabcbcbc']
for input_str in inputs:
    result = automaton.process_input(input_str)
    print(f'The input "{input_str}" is accepted: {result}')
