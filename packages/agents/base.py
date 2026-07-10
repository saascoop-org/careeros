from abc import ABC, abstractmethod
from typing import Any


class CareerAgent(ABC):
    name: str
    mission: str

    @abstractmethod
    def run(self, context: dict[str, Any]) -> dict[str, Any]:
        """Execute the agent task using a structured context."""
