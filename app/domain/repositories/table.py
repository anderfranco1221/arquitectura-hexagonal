from abc import ABC, abstractmethod

class TableRepository(ABC):

    @abstractmethod
    def get_count_row(self, nameTable: str) -> int: 
        raise NotImplemented