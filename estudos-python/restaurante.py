class Restaurante:
    restaurantes = []
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        Restaurante.restaurantes.append(self)
    def __str__(self):
        return f"Restaurante: {self.nome}, Categoria: {self.categoria}, Ativo: {self.ativo}"
    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f"{restaurante}")    

restaurante_praca = Restaurante('Praça', 'gourmet')
restaurante_pizza = Restaurante('Pizza Express', 'italiana')

restaurantes = [restaurante_praca, restaurante_pizza]    
print(vars(restaurante_praca))
print(vars(restaurante_pizza))
