from dataclasses import dataclass
from typing import Optional 

@dataclass
class Curso:
    codigo: str
    titulo: str
    preco: float
    tipo: int
    desconto_percentual: float = 0.0

    def __post_init__(self):
        if self.preco < 0:
            raise ValueError("Preço não pode ser negativo")
        if self.tipo not in [1, 2]: 
            raise ValueError
        if self.tipo == 1:
            self.preco = 0.0 
            self.desconto_percentual = 0.0
        
        
    @property
    def preco_final(self) -> float:
        if self.tipo == 1:
            return 0.0
            
        # desconto nunca é negativo
        desconto = max(0.0, self.desconto_percentual or 0.0)
        
        # calcula o valor com o desconto
        valor_desconto = self.preco * (desconto / 100)
        
        # mostra o preco final que tb nao pode ser negativo. pois nao existe preco negativo
        preco_final = self.preco - valor_desconto
        return max(0.0, preco_final)