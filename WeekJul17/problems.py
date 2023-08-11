"""
Pete likes to bake some cakes. He has some recipes and ingredients. Unfortunately he is not good in maths. Can you help him to find out, how many cakes he could bake considering his recipes?

Write a function cakes(), which takes the recipe (object) and the available ingredients (also an object) and returns the maximum number of cakes Pete can bake (integer). For simplicity there are no units for the amounts (e.g. 1 lb of flour or 200 g of sugar are simply 1 or 200). Ingredients that are not present in the objects, can be considered as 0.
"""

def cakes(recipe, available):
    min_cakes = float('inf')
    for key in recipe: 
        try: 
            recipe_quotient = available[key]//recipe[key]
        except: 
            return 0
        if recipe_quotient < min_cakes: 
            min_cakes = recipe_quotient
    return min_cakes

"""In this kata we want to convert a string into an integer. The strings simply represent the numbers in words.

Examples:

"one" => 1
"twenty" => 20
"two hundred forty-six" => 246"""

def parse_int(string):
    num_map = {
        "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
        "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,
        "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14,
        "fifteen": 15, "sixteen": 16, "seventeen": 17, "eighteen": 18, "nineteen": 19,
        "twenty": 20, "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60,
        "seventy": 70, "eighty": 80, "ninety": 90,
        "hundred": 100, "thousand": 1000, "million": 1000000
    }

    split_words = string.replace("-", " ").split()
    result = 0
    current_number = 0
    last_multiplier = 1

    for word in split_words:
        if word == "and":
            continue

        # Handle compound numbers with hyphens
        word = word.replace("-", "")

        if word in num_map:
            value = num_map[word]

            # Handle multipliers (hundred, thousand, million)
            if value in [100, 1000, 1000000]:
                if value == 100 and current_number != 0:
                    current_number *= value
                else:
                    result += current_number * value
                    last_multiplier = value
                    current_number = 0
            else:
                current_number += value

    result += current_number
    return result

"""
Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.
"""

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        def backtrack(start, path):
            if len(path) == k:
                results_list.append(path[:])  # Make a copy of the current combination
                return
            
            for i in range(start, n + 1):
                path.append(i)
                backtrack(i + 1, path)
                path.pop()
"""
There is a secret string which is unknown to you. Given a collection of random triplets from the string, recover the original string.

A triplet here is defined as a sequence of three letters such that each letter occurs somewhere before the next in the given string. "whi" is a triplet for the string "whatisup".

As a simplification, you may assume that no letter occurs more than once in the secret string.

You can assume nothing about the triplets given to you other than that they are valid triplets and that they contain sufficient information to deduce the original string. In particular, this means that the secret string will never contain letters that do not occur in one of the triplets given to you.
"""

def recoverSecret(triplets):
    #triplets is a list of triplets from the secrent string. Return the string.
    #First we are going to create a dictionary with a list of values as keys
    solution_graph = dict()
    solution_string = ""
    #Go through each item in triplets and create a key if none exists otherwise 
    #add next elements to the letter's list
    for item in triplets:
        for i in range(len(item)):
            if item[i] not in solution_graph:
                solution_graph[item[i]] = []
            if i == 0: 
                if item[1] not in solution_graph[item[0]]:
                    solution_graph[item[0]].append(item[1])
                if item[2] not in solution_graph[item[0]]:
                    solution_graph[item[0]].append(item[2])
            elif i == 1: 
                if item[2] not in solution_graph[item[1]]:
                    solution_graph[item[1]].append(item[2])
    
    
    # Now let's add the DFS-based topological sort

    # Step 1: Define the DFS function
    def topologicalSort(node):
        visited[node] = True
        for neighbor in solution_graph[node]:
            if not visited[neighbor]:
                topologicalSort(neighbor)
        result.insert(0, node)

    # Step 2: Initialize variables for DFS
    visited = {node: False for node in solution_graph}
    result = []

    # Step 3: Perform topological sort for each unvisited node
    for node in solution_graph:
        if not visited[node]:
            topologicalSort(node)

    # Step 4: Convert result to the final string
    solution_string = ''.join(result)
    return solution_string

        results_list = []
        backtrack(1, [])
        return results_list
