#
# Maze Solver
#
# Machine Learning project on reinforcement learning by teaching
# an agent how to go through a maze in optimal steps without running
# into objects along the way
#
#   authors: David Gilstad, Ian Schwind
#   created: October 9, 2020
#
import numpy as np

alpha, epsilon, gamma = 0.05, 1, 0.9  # TODO: Find out what are good values and explain in paper
height = width = 6
episodes = 10000
maxSteps = 100

# locations of the following objects on the grid
start = [0, 5]
end = [5, 4]
walls = [[2, 2], [2, 3], [3, 5], [4, 3], [4, 4]]

min_steps = 10  # minimum number of steps from start to finish
Rend, Rwall, Rdistance = 5, -1, 0.5  # reward values


class TD_agent:
    def __init__(self):
        self.prev_loc, self.curr_loc = None, start  # keep track of agent's location
        self.v_values = np.zeros([width, height])  # values of each state in the grid
        self.actions = [self.left, self.right, self.up, self.down]

    # get values at each state the agent can move to
    def getValues(self):
        values = [-1, -1, -1, -1]
        if self.curr_loc[0] != 0:
            values[0] = self.v_values[self.curr_loc[0] - 1, self.curr_loc[1]]
        if self.curr_loc[0] < width - 1:
            values[1] = self.v_values[self.curr_loc[0] + 1, self.curr_loc[1]]
        if self.curr_loc[1] != 0:
            values[2] = self.v_values[self.curr_loc[0], self.curr_loc[1] - 1]
        if self.curr_loc[1] < height - 1:
            values[3] = self.v_values[self.curr_loc[0], self.curr_loc[1] + 1]
        return values

    # movements: move to the selected state, reward the start state
    # based on
    def left(self):
        if self.curr_loc[0] == 0:
            self.action()  # try doing a different action if at a boundary
        else:  # do action
            self.prev_loc, self.curr_loc[0] = self.curr_loc, self.curr_loc[0] - 1

    def right(self):
        if self.curr_loc[0] == width - 1:
            self.action()
        else:  # do action
            self.prev_loc, self.curr_loc[0] = self.curr_loc, self.curr_loc[0] + 1

    def up(self):
        if self.curr_loc[1] == 0:
            self.action()
        else:  # do action
            self.prev_loc, self.curr_loc[1] = self.curr_loc, self.curr_loc[1] - 1

    def down(self):
        if self.curr_loc[1] == height - 1:
            self.action()
        else:  # do action
            self.prev_loc, self.curr_loc[1] = self.curr_loc, self.curr_loc[1] + 1

    # pick the action
    def greedy(self):
        values = self.getValues()
        return self.actions[values.index(max(values))]

    # try a random option
    def explore(self):
        return self.actions[np.random.choice([0, 1, 2, 3])]

    def chooseOption(self):
        # choose an action
        chosenAction = np.random.choice([self.greedy(), self.explore()], p=[1 - epsilon, epsilon])
        return chosenAction

    # choose an action greedily, i.e. the max value action with probability
    # 1-epsilon, and a random action with probability epsilon
    def action(self):
        action = self.chooseOption()
        action()
        return self.curr_loc, action

    def sarsa(self):
        t = 0
        state1 = start
        temp = self.action()
        action1 = temp[1]
        while(t<maxSteps):
            self.action()
            state2 = self.curr_loc
            action2 = self.chooseOption


if __name__ == '__main__':
    a, count = TD_agent(), 0
    while (a.curr_loc != end):
        temp = a.action()
        count += 1
        print(count, a.curr_loc, temp[1])

    print("ended at:", a.curr_loc)
    print("number of iterations:", count)
