# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"

    # Essa funcao retorna uma lista de acoes que o pacman deve fazer para achar seu objetivo

    # pega o no inicial do espaco de estados
    noInicial = problem.getStartState()

    # se o no inicial for o objtivo, retorna uma lista vazia
    if problem.isGoalState(noInicial):
        return []

    # se nao for objetivo, comeca a busca

    # inicializa lista de nos visitados como vazia
    nosVisitados = []

    # utiliza-se uma lista de prioridade para definir a fronteira
    fronteira = util.PriorityQueue()

    # cada item da lista eh uma tupla, dada por (estado/coordenada do no atual, acao necessaria para chegar ao no atual, custo do no atual)
    # ao adionar uma elemento na fronteira, passa-se da seguinte forma: (tupla,prioridade=custototal+heuristica)
    # no caso do no inicial, a lista de acoes eh vazia, o custo eh zero e a prioridade eh 0 (prioridade maxima)
    fronteira.push((noInicial, [], 0), 0)

    # Enquanto a fronteira nao estiver vazia
    while not fronteira.isEmpty():

        # pega tupla com menor custo da fronteira, ou seja, no mais "barato"
        noAtual, acoes, custoAnterior = fronteira.pop()

        # se o no atual ainda nao foi visita, coloca na lista de visitados e analisa
        if noAtual not in nosVisitados:
            nosVisitados.append(noAtual)

            # verifica se eh o no meta
            if problem.isGoalState(noAtual):
                return acoes

            # se nao for no meta analisa os filhos, ou sucessores
            filhos = problem.getSuccessors(noAtual)

            # pega numero de filhos que o no possui (tamanho da lista)
            numeroDeFilhos=len(filhos)

            # loop que analisa nos filhos e calcula custo de cada um (custo total + custo heuristico)
            for i in range(0, numeroDeFilhos):
                
                # varre nos vizinhos
                noFilho = (filhos[i])
                # pega valores
                proximoNo, acao, custo = noFilho

                # acoes necessarias pra fechar ate o no filho em questao
                acaoTotal = acoes + [acao]
                # custo total para chegar ate o no filho em questao
                custoTotal = custoAnterior + custo
                # custo heristico ate o no em questao (custo total + valor da funcao heuristica)
                custoHeuristico = custoTotal + heuristic(proximoNo,problem)
                # adiciona no filho na fronteira, prioridade de acordo com o custo heuristico
                fronteira.push((proximoNo, acaoTotal, custoTotal),custoHeuristico)
    
    util.raiseNotDefined()

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
