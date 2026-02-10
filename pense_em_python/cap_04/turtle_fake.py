class TurtleFake:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.angle = 0

    def fd(self, n):
        print(f"Avançando {n} passos")

    def lt(self, ang):
        print(f"Virando {ang} graus à esquerda")
    
    def bk(self, n):
        print(f'Dando {n} passo para trás')
        
    def rt(self, ang):
        print(f'Virando {ang} graaus à direita')
