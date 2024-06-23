import numpy as np
import random

class Organism:
    def __init__(self, name, x, y, energy=100):
        self.name = name
        self.x = x
        self.y = y
        self.energy = energy
        self.hunger = 0
        self.q_table = np.zeros((100, 2))  # Zustand: Hunger, Aktion: 0=Bewegen, 1=Essen

    def choose_action(self):
        state = self.hunger
        if np.random.rand() < 0.1:  # 10% Zufallswahrscheinlichkeit für Exploration
            return np.random.choice([0, 1])
        return np.argmax(self.q_table[state])

    def update_q_table(self, state, action, reward, next_state):
        alpha = 0.1  # Lernrate
        gamma = 0.9  # Diskontierungsfaktor
        best_next_action = np.argmax(self.q_table[next_state])
        self.q_table[state, action] = self.q_table[state, action] + alpha * (reward + gamma * self.q_table[next_state, best_next_action] - self.q_table[state, action])

    def move(self):
        self.x += random.randint(-10, 10)
        self.y += random.randint(-10, 10)
        self.x = max(0, min(self.x, 800))
        self.y = max(0, min(self.y, 600))
        self.energy -= 1
        self.hunger += 1

    def eat(self):
        self.energy += random.randint(20, 50)
        self.hunger = 0

    def live_one_day(self):
        state = self.hunger
        action = self.choose_action()

        if action == 1:  # Essen
            self.eat()
            reward = 10 if self.energy > 0 else -100
        else:  # Bewegen
            self.move()
            reward = -1 if self.energy > 0 else -100

        next_state = self.hunger
        self.update_q_table(state, action, reward, next_state)

        if self.energy <= 0:
            print(f'{self.name} ist gestorben.')
            return False
        return True
