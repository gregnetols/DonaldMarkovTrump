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


class MarkovProcess(object):
    def __init__(self):
        self.state_dict = {}
        self.num_states = 0

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
        #self.state_dict[to].add_neighbor(self.state_dict[frm])

    def get_states(self):
        return self.state_dict.keys()


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




    for v in markov_chain:
        for w in v.get_connections():
            vid = v.get_state()
            wid = w.get_state()
            print ('( %s , %s, %3d)'  % ( vid, wid, v.get_occurences(w)))

    for v in markov_chain:
        print ('g.vert_dict[%s]=%s' %(v.get_state(), markov_chain.state_dict[v.get_state()]) )

    for v in markov_chain:
        print(v.adjacent)



