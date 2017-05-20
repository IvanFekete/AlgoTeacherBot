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

categoriesList = ["/sorting", "/searching", "/string", "/recursion", "/miscellaneous", "/math", "/greedy",
                  "/graphs", "/geometry", "/dp", "/datastruct", "/compression"]

nameByCategory = {
    "/sorting" : "Sorting Algorithms",
    "/searching" : "Searching Algorithms",
    "/string" : "String Algorithms",
    "/recursion" : "Recursion, Backtracking etc",
    "/miscellaneous" : "Miscellaneous",
    "/math" : "Mathematical Algorithms",
    "/greedy" : "Greedy Algorithms",
    "/graphs" : "Graph Algorithms",
    "/geometry" : "Geometric Algorithms",
    "/dp" : "Dynamic Programming",
    "/datastruct" : "Data Structures",
    "/compression" : "Compression Algorithms"
}



def formButton(category) :
    keyboard = types.InlineKeyboardMarkup()
    for algorithm in algoStructure[nameByCategory[category]] :
        keyboard.add(types.InlineKeyboardButton(text = algorithm, callback_data = nameByCategory[category] + "/" + algorithm))
    return keyboard



categoriesInlineKeyboardMarkup = {
    category : formButton(category) for category in categoriesList
}

listOfCategoriesForShow = ["%s - %s" % (item[0], item[1]) for item in sorted(nameByCategory.items())]

startMessage = """ Hi, I'm a AlgoTeacher bot. I will help you to find out something new about the most common algorithms. 
Please enter a name of an algorithm or choose the category from this list :
%s
""" % ',\n'.join(listOfCategoriesForShow)

helpMessage = """ This bot can help you to find out something new about the most common algorithms. 
/start - start to work with me
/help - get a help information about me
Commands for categories :
%s
""" % ',\n'.join(listOfCategoriesForShow)
