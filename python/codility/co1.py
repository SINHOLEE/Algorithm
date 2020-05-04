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

    def add_load(self):
        self._load += 1

    def get_load(self):
        return self._load

    def get_skills(self):
        return self._skills

    def get_len_skills(self):
        return self._len_skills


class Ticket(object):
    _id = ""
    _restrictions = []

    def __init__(self, id, restrictions):
        self._id = id
        self._restrictions = restrictions

    def get_restrictions(self):
        return self._restrictions

    def get_id(self):
        return self._id


class FinderPolicy(object):
    def _filter_loaded_agents(self, agents: List[Agent]) -> List[Agent]:
        if len(agents) == 0:
            raise NoAgentFoundException("no agents")

        agents = list(filter(lambda x: x.get_load() < 3, agents))
        return agents

    def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:
        raise NoAgentFoundException("asdasd")


class LeastLoadedAgent(FinderPolicy):
    def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:
        if len(agents) == 0:
            raise NoAgentFoundException("no agents")
        agents = self._filter_loaded_agents(agents)
        if len(agents) == 0:
            raise NoAgentFoundException("load3 보다 적은 agent가 없습니다.")
        agents = sorted(agents, key=lambda x: x.get_load())
        agents[0].add_load()
        return agents[0]


class LeastFlexibleAgent(FinderPolicy):
    def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:
        if len(agents) == 0:
            raise NoAgentFoundException("입력값이 없습니다.")
        agents = self._filter_loaded_agents(agents)
        if len(agents) == 0:
            raise NoAgentFoundException("load3 보다 적은 agent가 없습니다.")

        temp = []
        for agent in agents:
            flag = False
            for skill in agent.get_skills():
                if skill in ticket.get_restrictions():
                    temp.append(agent)
                    flag = True
                    break
                if flag:
                    break

        if len(temp) == 0:
            raise NoAgentFoundException("티켓과 매칭되는 스킬을 지닌 agent가 없습니다.")
        temp = sorted(temp, key=lambda x: x.get_len_skills())
        temp[0].add_load()
        return temp[0]


ticket = Ticket(id="1", restrictions=["English"])
agent1 = Agent(name="A", skills=["English"], load=2)
agent2 = Agent(name="B", skills=["English", "Japanese"], load=0)

print(ticket)
print(agent1)
print(agent2)

least_loaded_policy = LeastLoadedAgent()
print(least_loaded_policy.find(ticket, []))
