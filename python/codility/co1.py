from typing import List, Text


class NoAgentFoundException(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


class Agent(object):
    _name = ""
    _skills = []
    _load = 0
    _len_skills = 0

    def __init__(self, name, skills, load):
        self._name = name
        self._skills = skills
        self._load = load
        self._len_skills = len(skills)

    def __str__(self):
        return "<Agent: {}>".format(self._name)


class Ticket(object):
    _id = ""
    _restrictions = []

    def __init__(self, id, restrictions):
        self._id = id
        self._restrictions = restrictions


class FinderPolicy(object):
    def _filter_loaded_agents(self, agents: List[Agent]) -> List[Agent]:
        if len(agents) == 0:
            raise NoAgentFoundException("no agents")

        agents = sorted(agents, key=lambda x: (x._len_skills, x._load), reverse=True)
        # raise NoAgentFoundException("asdasd")
        return agents

    def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:
        if len(agents) == 0:
            raise NoAgentFoundException("no agents")

        agents = self._filter_loaded_agents(agents)

        return agents[0]
        # raise NoAgentFoundException("asdasd")


class LeastLoadedAgent(FinderPolicy):
    def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:
        if len(agents) == 0:
            raise NoAgentFoundException("no agents")

        temp = FinderPolicy().find(ticket, agents)
        if temp[0]._load == 3:
            raise  NoAgentFoundException("no more load")
        else:
            temp[0]._load += 3
        return temp[0]

class LeastFlexibleAgent(FinderPolicy):
    def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:
        if len(agents) == 0:
            raise NoAgentFoundException("no agents")
        temp = FinderPolicy().find(ticket, agents)

        if temp[0]._load == 3:
            raise  NoAgentFoundException("no more load")
        else:
            temp[0].load += 3


ticket = Ticket(id="1", restrictions=["English"])
agent1 = Agent(name="A", skills=["English"], load=2)
agent2 = Agent(name="B", skills=["English", "Japanese"], load=0)

print(ticket)
print(agent1)
print(agent2)

least_loaded_policy = LeastLoadedAgent()
print(least_loaded_policy.find(ticket, [agent1, agent2]))
