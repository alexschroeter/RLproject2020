import numpy as np

from Agent import Agent
from Environment import Environment


class GridworldPlayground:
    def __init__(self):
        self.gui = None
        self.environment = None
        self.agent = None
        self.msDelay = None
        self.showEveryNsteps = None

    def set_gui(self, gui):
        self.gui = gui

    def visualize_gui(self):
        data = {"agentPosition": self.agent.state}
        self.gui.visualize(data)  # gwp gathers data, then calls visualize method of gwp. This method should all GUIs have.

    def initialize(self, data):
        self.msDelay = data["msDelay"]
        self.showEveryNsteps = data["showEveryNsteps"]
        self.environment = Environment(data)
        self.agent = Agent(self.environment)
        self.run(timestepsLeft=data["maxTimeSteps"])

    def run(self, timestepsLeft):
        #print(timestepsLeft)
        self.visualize_gui()
        if not timestepsLeft:
            self.plot()
            del self.agent
            return
        for t in range(self.showEveryNsteps):
            if self.agent.episodeFinished:
                self.agent.start_episode()
            self.agent.step()
        self.gui.process.after(self.msDelay, lambda: self.run(timestepsLeft-self.showEveryNsteps))

    def plot(self):
        pass
