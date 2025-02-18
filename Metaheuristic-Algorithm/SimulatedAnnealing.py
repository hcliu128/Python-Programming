from utils.DistanceMatrix import distance_matrix
from itertools import permutations 
import random
import math


class SimulatedAnnealing:
    '''
    Simulated Annealing algorithm for TSP (Traveling Salesman Problem)
    '''
    def __init__(self, ncities=15, temperature=1000, cooling_rate=0.03, num_iterations=100, tmin = 1e-3):
        self.ncities = ncities
        self.distance_matrix = distance_matrix # from import
        self.temperature = temperature
        self.cooling_rate = cooling_rate
        self.num_iterations = num_iterations
        self.tmin = tmin
        self.route = random.sample(range(1, ncities + 1), ncities)
        self.route.append(self.route[0]) # back to source
        self.distance = self.get_distance(self.route)
        self.best_route = self.route # init
        self.best_distance = self.distance # init
        self.history = [self.best_distance]
    
    def get_distance(self, route):
        '''
        Get the total distance of two given points
        '''
        distance = 0
        for i in range(self.ncities):
            distance += self.distance_matrix[route[i]-1][route[i+1]-1]
        return distance
    
    def simulated_annealing(self):
        '''
        Simulated Annealing algorithm
        '''
        while True:
            if self.temperature < self.tmin:
                break
            current_route = self.route
            current_distance = self.get_distance(current_route)
            for i in range(self.num_iterations):
                new_route = self.getSwap(current_route.copy()[:-1])
                new_route.append(new_route[0])
                new_distance = self.get_distance(new_route)
                if new_distance < current_distance:
                    self.route = new_route
                    self.distance = new_distance
                    if new_distance < self.best_distance:
                        best_route = new_route
                        best_distance = new_distance
                else:
                    if random.random() < self.acceptance_probability(current_distance, new_distance, self.temperature):
                        self.route = new_route
                        self.distance = new_distance
            self.temperature *= (1 - self.cooling_rate)
            self.history.append(best_distance)
        return best_route, int(best_distance)
    
    def acceptance_probability(self, current_distance, new_distance, temperature):
        '''
        Calculate acceptance probability of a new solution
        accept with probability exp(-(diff) / temperature)
        '''
        return math.exp((current_distance - new_distance) / temperature) 
    
    def getSwap(self, route):
        '''
        Swap two cities in a route randomly
        '''
        city1 = random.randint(1, self.ncities - 1)
        city2 = random.randint(1, self.ncities - 1)
        while city1 == city2:
            city2 = random.randint(1, self.ncities - 1)
        route[city1], route[city2] = route[city2], route[city1]
        return route


    def exhaustive(self, route):
        '''
        Exhaustive search for the best route (brute force)
        '''
        r = route[:]
        d = []
        perm = list(permutations(r[1:-1]))
        for i in range(len(perm)):
            perm[i].insert(0, r[0])
            perm[i].append(r[-1])
            d.append(self.get_distance(perm[i]))
        smallest_distance = min(d)
        arr = perm.index(smallest_distance)
        smallest_route = d[arr]
        return smallest_route, smallest_distance

    def plot(self):
        '''
        Plot the history of distances over iterations
        '''
        import matplotlib.pyplot as plt
        plt.plot(self.history)
        plt.ylabel('Distance')
        plt.xlabel('Iteration')
        plt.show()


if __name__ == "__main__":
    SA = SimulatedAnnealing()
    print(f"Init route: {SA.route}")
    print(f"Init distance: {SA.get_distance(SA.route)}")
    print(f"After executing simulated annealing: {SA.simulated_annealing()}")
    # print("IDEAL: " + SA.exhaustive(SA.route))
    SA.plot()