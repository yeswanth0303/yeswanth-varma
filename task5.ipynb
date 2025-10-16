{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "984e670a-43db-4aac-8e0b-d3dc08b9d4f0",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/var/folders/th/wqjsxyss0qb4j9ll94jbvl940000gn/T/ipykernel_2650/3543024658.py:22: RuntimeWarning: divide by zero encountered in divide\n",
      "  visibility = 1/d\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Best path: [1. 2. 5. 2. 1. 1.]\n",
      "Cost of the best path: 36.0\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "from numpy import inf\n",
    "\n",
    "d = np.array([\n",
    "    [0,10,12,11,14],\n",
    "    [10,0,13,15,8],\n",
    "    [12,13,0,9,14],\n",
    "    [11,15,9,0,16],\n",
    "    [14,8,14,16,0]\n",
    "])\n",
    "\n",
    "iteration = 100\n",
    "n_ants = 5\n",
    "n_citys = 5\n",
    "\n",
    "m = n_ants\n",
    "n = n_citys\n",
    "e = .5\n",
    "alpha = 1\n",
    "beta = 2\n",
    "\n",
    "visibility = 1/d\n",
    "visibility[visibility == inf] = 0\n",
    "pheromone = .1 * np.ones((n, n))\n",
    "\n",
    "best_route = None\n",
    "best_cost = float('inf')\n",
    "\n",
    "for ite in range(iteration):\n",
    "    routes = np.ones((m, n+1))\n",
    "    for k in range(m):\n",
    "        for j in range(1, n):\n",
    "            cur = int(routes[k][j-1]) - 1\n",
    "            prob = np.power(pheromone[cur], alpha) * np.power(visibility[cur], beta)\n",
    "            prob[cur] = 0\n",
    "            prob = prob / np.sum(prob)\n",
    "            next_city = np.random.choice(range(n), p=prob)\n",
    "            routes[k][j] = next_city + 1\n",
    "        routes[k][-1] = 1\n",
    "\n",
    "    dist_cost = np.zeros(m)\n",
    "    for i in range(m):\n",
    "        s = 0\n",
    "        for j in range(n):\n",
    "            s += d[int(routes[i][j])-1, int(routes[i][j+1])-1]\n",
    "        dist_cost[i] = s\n",
    "\n",
    "    idx = np.argmin(dist_cost)\n",
    "    if dist_cost[idx] < best_cost:\n",
    "        best_cost = dist_cost[idx]\n",
    "        best_route = routes[idx]\n",
    "\n",
    "    pheromone = (1 - e) * pheromone\n",
    "    for i in range(m):\n",
    "        for j in range(n):\n",
    "            pheromone[int(routes[i][j])-1, int(routes[i][j+1])-1] += 1 / dist_cost[i]\n",
    "\n",
    "print(\"Best path:\", best_route)\n",
    "print(\"Cost of the best path:\", best_cost)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0f8b645c-dfda-4fee-ac4c-f6f18083a8a9",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
