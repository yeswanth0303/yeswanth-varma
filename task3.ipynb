{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "0ea6c450-1c9f-462d-a0d6-e86756b407cf",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Following is the A* Algorithm:\n",
      "Path found: ['A', 'F', 'G', 'I', 'J']\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "['A', 'F', 'G', 'I', 'J']"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "def aStarAlgo(start_node, stop_node):\n",
    "    open_set = set([start_node])\n",
    "    closed_set = set()\n",
    "    g = {}\n",
    "    parents = {}\n",
    "\n",
    "    g[start_node] = 0\n",
    "    parents[start_node] = start_node\n",
    "\n",
    "    while len(open_set) > 0:\n",
    "        n = None\n",
    "        for v in open_set:\n",
    "            if n is None or g[v] + heuristic(v) < g[n] + heuristic(n):\n",
    "                n = v\n",
    "\n",
    "        if n is None:\n",
    "            print('Path does not exist!')\n",
    "            return None\n",
    "\n",
    "        if n == stop_node:\n",
    "            path = []\n",
    "            while parents[n] != n:\n",
    "                path.append(n)\n",
    "                n = parents[n]\n",
    "            path.append(start_node)\n",
    "            path.reverse()\n",
    "            print('Path found:', path)\n",
    "            return path\n",
    "\n",
    "        for (m, weight) in get_neighbors(n):\n",
    "            if m not in open_set and m not in closed_set:\n",
    "                open_set.add(m)\n",
    "                parents[m] = n\n",
    "                g[m] = g[n] + weight\n",
    "            else:\n",
    "                if g[m] > g[n] + weight:\n",
    "                    g[m] = g[n] + weight\n",
    "                    parents[m] = n\n",
    "                    if m in closed_set:\n",
    "                        closed_set.remove(m)\n",
    "                        open_set.add(m)\n",
    "\n",
    "        open_set.remove(n)\n",
    "        closed_set.add(n)\n",
    "\n",
    "    print('Path does not exist!')\n",
    "    return None\n",
    "\n",
    "\n",
    "def get_neighbors(v):\n",
    "    if v in Graph_nodes:\n",
    "        return Graph_nodes[v]\n",
    "    else:\n",
    "        return None\n",
    "\n",
    "\n",
    "def heuristic(n):\n",
    "    h_dist = {\n",
    "        'A': 11, 'B': 6, 'C': 5, 'D': 7,\n",
    "        'E': 3, 'F': 6, 'G': 5, 'H': 3,\n",
    "        'I': 1, 'J': 0\n",
    "    }\n",
    "    return h_dist[n]\n",
    "\n",
    "\n",
    "Graph_nodes = {\n",
    "    'A': [('B', 6), ('F', 3)],\n",
    "    'B': [('A', 6), ('C', 3), ('D', 2)],\n",
    "    'C': [('B', 3), ('D', 1), ('E', 5)],\n",
    "    'D': [('B', 2), ('C', 1), ('E', 8)],\n",
    "    'E': [('C', 5), ('D', 8), ('I', 5), ('J', 5)],\n",
    "    'F': [('A', 3), ('G', 1), ('H', 7)],\n",
    "    'G': [('F', 1), ('I', 3)],\n",
    "    'H': [('F', 7), ('I', 2)],\n",
    "    'I': [('E', 5), ('G', 3), ('H', 2), ('J', 3)]\n",
    "}\n",
    "\n",
    "print(\"Following is the A* Algorithm:\")\n",
    "aStarAlgo('A', 'J')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5f47596d-ebc4-4411-aa79-92df15cc8c61",
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
