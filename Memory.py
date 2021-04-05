class Memory:
    # TODO: talk about depth convention here
    def __init__(self):
        self.memory = []  # TODO: No need for middle access if G is tracked, so use deque. #I think vanilla python list is faster than collections.deque and numpy.array for the purpose of this class, since you have to not only push and pop things to/from the endings, but also have to access multiple reward elements in one update step when running n-step algorithms (n >> 1). Am I right? Any suggestion for a faster data structure?

    def memorize_state_action_reward(self, S_A_R_triple):
        self.memory.insert(0, S_A_R_triple)

    def get_size(self):
        return len(self.memory)

    def get_state(self, depth=1):
        return self.memory[depth-1][0]

    def get_action(self, depth=1):
        return self.memory[depth-1][1]

    def get_reward(self, depth=1):
        return self.memory[depth-1][2]

    def forget_state_action_reward(self, depth=1):
        del self.memory[-depth:]
