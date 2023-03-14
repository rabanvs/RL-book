from typing import TypeVar, Iterable

from project.tac import TacState
from rl.markov_decision_process import MarkovDecisionProcess
from rl.markov_process import NonTerminal

A = TypeVar('A')

class TacGame(MarkovDecisionProcess[TacState]):

    def actions(self, state: NonTerminal[TacState]) -> Iterable[A]:
        pass

    def step(self, state: NonTerminal[TacState], action: A) -> NonTerminal[TacState]:
        pass
