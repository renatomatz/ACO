import sys
sys.path.insert(0, "../ACO")

import numpy as np
from ACO import AntColonyOptimizer

num_points = 100
rng = np.random.default_rng(42)

distance_matrix = rng.uniform(1, 9, [num_points, num_points])

optimizer = AntColonyOptimizer(ants=10, evaporation_rate=.1, 
                               intensification=2, alpha=1, beta=1,
                               beta_evaporation_rate=0, choose_best=.1)
 
best = optimizer.fit(distance_matrix, 100)
optimizer.plot()
