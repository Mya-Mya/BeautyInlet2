from typing import Callable
from abc import ABC, abstractmethod

class TakeFierer(ABC):
    @abstractmethod
    def run(self,fire:Callable):
        pass