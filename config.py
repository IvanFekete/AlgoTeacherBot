import os
from telebot import types
TOKEN = "397605652:AAEvceq-GSOpiiAH6yu3fGqkYO4qQiZWGJg"


algoStructure = {
    "Compression Algorithms" : ['Huffman Coding'],
    "Data Structures" : ['Binary Indexed Tree', 'Binary Search Tree', 'Binomial Heap', 'Bit Queue', 'Circular Doubly-Linked List', 'Disjoint Set Union', 'Fibonacci Heap', 'Link-cut Tree', 'Pairing Heap', 'Priority Queue', 'Proto-vEB Tree', 'Segment Tree', 'Splay Tree', 'Suffix Array + LCP Array', 'Suffix Automaton', 'Trie', 'van Emde Boas Tree', 'XOR Linked List'],
    "Dynamic Programming" : ['0-1 Knapsack', 'Longest Common Subsequence', 'Matrix Chain Multiplication', 'Needleman-Wunsch', 'Nussinov Algorithm', 'Segmented Least Squares', 'Unbounded Knapsack'],
    "Geometric Algorithms" : ['Graham Scan', 'Point in Convex Polygon', 'Segment Intersection'],
    "Graph Algorithms" : ['Bellman-Ford Algorithm', 'Breadth-First Search', 'Connected Components', 'Cycle Detection', 'Depth-First Search', "Dijkstra's Algorithm", "Dinic's Algorithm", 'Edmonds-Karp Algorithm', 'Floyd-Warshall Algorithm', 'Ford-Fulkerson Algorithm', 'Heavy-Light Decomposition', "Kosaraju's Algorithm", "Kruskal's Algorithm", "Prim's Algorithm", "Tarjan's SCC Algorithm", 'Topological Sorting'],
    "Greedy Algorithms" : ['First-Fit Bin Packing', 'Interval Scheduling'],
    "Mathematical Algorithms" : ['Euclidean Algorithm', 'Exponentiation by Squaring', 'Extended Euclidean Algorithm', 'Matrix Exponentiation', 'Matrix Multiplication', 'PageRank', "Pascal's Triangle", 'Sieve of Eratosthenes', 'Simplex Algorithm', "Strassen's Algorithm"],
    "Miscellaneous" : ['Fast Input (Thanks to Ermin Hodzic)'],
    "Recursion, Backtracking etc" : ['K-Combinations', 'Permutations', 'Power Set'],
    "Searching Algorithms" : ['Binary Search', 'Quickselect', 'Ternary Search'],
    "Sorting Algorithms" : ['Bitonic Sorter', 'Bubble Sort', 'Counting Sort', 'Heapsort', 'Insertion Sort', 'Merge Sort', 'Quicksort', 'Selection Sort'],
    "String Algorithms" : ['Knuth-Morris-Pratt', 'Z Algorithm']
}

categoriesList = ["/sorting", "/searching", "/string", "/recursion"]

nameByCategory = {
    "/sorting" : "Sorting Algorithms",
    "/searching" : "Searching Algorithms"
}


def formButton(category) :
    keyboard = types.InlineKeyboardMarkup()
    for algorithm in algoStructure[nameByCategory[category]] :
        keyboard.add(types.InlineKeyboardButton(text = algorithm, callback_data = algorithm))
    return keyboard

categoriesInlineKeyboardMarkup = {
    "/sorting" : formButton("/sorting")
}

startMessage = """ Hi, I'm a AlgoTeacher bot. I will help you to know something about the most common algorithms. 
Please enter a name of an  algorithm or choose the category from this list :
%s
""" % ',\n'.join(categoriesList)

helpMessage = """ This bot can help you to know something about the most common algorithms. 
/start - start to work with me
/help - get a help information about me
Commands for categories :
%s
""" % ',\n'.join(categoriesList)
