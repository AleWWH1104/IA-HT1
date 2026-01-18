import random

class Environment:
    "Clase que representa el entorno"

    def __init__(self):
        # Temperatura actual aleatoriamente entre 10 y 35 grados.
        self.temperature = random.uniform(10, 35)

    def get_percept(self):
        # Sensor que devuelve temperatura
        return self.temperature

    def update(self, action):
        # Modifica temperaturas
        if action == "enfriar":
            self.temperature -= 2.0
        elif action == "calentar":
            self.temperature += 2.0
        # Si la acción es 'esperar', no se hace nada
        self.temperature = max(0, self.temperature)


class Agent:
    "Clase que representa el agente inteligente"

    def act(self, perception):
        # Recibe la percepción y decide qué acción tomar.
        temperature = perception
        if temperature > 25:
            return "enfriar"
        elif temperature < 18:
            return "calentar"
        else:
            return "esperar"


