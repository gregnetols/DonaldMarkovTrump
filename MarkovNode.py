import random

class MarkovState(object):
    def __init__(self, state):
        self.state = state
        self.adjacent = {}

    def __str__(self):
        return str(self.state) + ' adjacent: ' + str([x.state for x in self.adjacent])

    def add_neighbor(self, neighbor):
        if neighbor in self.adjacent:
            self.adjacent[neighbor] += 1
        else:
            self.adjacent[neighbor] = 1

    def get_connections(self):
        return self.adjacent.keys()

    def get_state(self):
        return self.state

    def get_occurences(self, neighbor):
        return self.adjacent[neighbor]

    def get_neighbors(self):
        return self.adjacent


class MarkovProcess(object):
    def __init__(self):
        self.state_dict = {}
        self.num_states = 0
        self.start_states = []

    def __iter__(self):
        return iter(self.state_dict.values())

    def add_state(self, state):
        self.num_states += 1
        new_state = MarkovState(state)
        self.state_dict[state] = new_state
        return new_state

    def get_state(self, n):
        if n in self.state_dict:
            return self.state_dict[n]
        else:
            return None

    def add_transition(self, frm, to):
        if frm not in self.state_dict:
            self.add_state(frm)
        if to not in self.state_dict:
            self.add_state(to)

        self.state_dict[frm].add_neighbor(self.state_dict[to])

    def get_states(self):
        return self.state_dict.keys()

    def transition_states(self, state):
        neighbor_dict = state.get_neighbors()

        value_sum = 0
        for key in neighbor_dict:
            value = neighbor_dict[key]
            value_sum += value

        next_state_number = random.randint(0, value_sum)

        value_sum = 0
        for key in neighbor_dict:
            value = neighbor_dict[key]
            value_sum += value
            if value_sum >= next_state_number:
                return key

        return None

    def create_sentence(self, starting_state):
        current_state = starting_state
        print("")
        print(current_state.state, end=" ")

        while current_state.state != '':

            next_state = self.transition_states(current_state)

            print(next_state.state, end=" ")

            current_state = next_state

        print("")



if __name__ == '__main__':
    markov_chain = MarkovProcess()

    markov_chain.add_state('a')
    markov_chain.add_state('cat')
    markov_chain.add_state('with')
    markov_chain.add_state('a')
    markov_chain.add_state('map')
    markov_chain.add_state('is')
    markov_chain.add_state('on')
    markov_chain.add_state('my')
    markov_chain.add_state('lap')

    markov_chain.add_transition('a', 'cat')
    markov_chain.add_transition('cat', 'with')
    markov_chain.add_transition('with', 'a')
    markov_chain.add_transition('a', 'map')
    markov_chain.add_transition('map', 'is')
    markov_chain.add_transition('is', 'on')
    markov_chain.add_transition('on', 'my')
    markov_chain.add_transition('my', 'lap')
    markov_chain.add_transition('lap', '')

    next_state = markov_chain.transition_states(markov_chain.get_state("a"))

    print(markov_chain.get_state("a"))
    print(next_state)

    markov_chain.create_sentence(markov_chain.get_state("a"))



"""
    for v in markov_chain:
        for w in v.get_connections():
            vid = v.get_state()
            wid = w.get_state()
            print ('( %s , %s, %3d)'  % ( vid, wid, v.get_occurences(w)))

    for v in markov_chain:
        print ('g.vert_dict[%s]=%s' %(v.get_state(), markov_chain.state_dict[v.get_state()]) )

    for v in markov_chain:
        print(v.adjacent)

    node = markov_chain.get_state('a')
    print(node.get_neighbors())
"""


