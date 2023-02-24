#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by: Robert Duncan
# File Name: TSP.py
# Date Created: February 7th, 2023
# Date Last Modified: February 24th, 2023
"""
This script serves as a rendition of the common Travelling Sales Person problem, to accurately
sketch the shortest possible path for a set of given cities.
"""


cities = ["New York City", "Denver", "Chicago", "Houston", "Philadelphia", "Phoenix", "San Antonio"]

# All distances are Air Travel Distances for most accurate representation of miles from
# one destination to another
distances = [
    [0, 1629, 714, 1419, 81, 2144, 1583],  # Distances from New York City
    [1629, 0, 916, 878, 1574, 585, 802],  # Distances from Denver
    [714, 916, 0, 938, 666, 1453, 1050],  # Distances from Chicago
    [1419, 878, 938, 0, 1341, 1016, 190],  # Distances from Houston
    [81, 1574, 666, 1341, 0, 2082, 1507],  # Distances from Philadelphia
    [2144, 585, 1453, 1016, 2082, 0, 848],  # Distances from Phoenix
    [1583, 802, 1050, 190, 1507, 848, 0]  # Distances from San Antonio
]

tspDictionary = {}
lowestDistance = 999999
numberOfCities = len(cities)
for c in range(numberOfCities):
    visitedCities = [0] * numberOfCities
    currentCity = c
    orderOfVisit = []
    numVisited = 0
    nextCity = 0
    totalDistance = 0
    while numVisited < numberOfCities:
        for i in range(numberOfCities):
            min_dist = max(distances[currentCity])
            for j in range(numberOfCities):
                if j != currentCity and visitedCities[j] != 1:
                    if distances[currentCity][j] < min_dist:
                        min_dist = distances[currentCity][j]
                        nextCity = j
            visitedCities[currentCity] = 1
            orderOfVisit.append(currentCity)
            totalDistance += distances[currentCity][nextCity]
            numVisited += 1
            currentCity = nextCity
    if totalDistance < lowestDistance:
        lowestDistance = totalDistance
    tspDictionary[totalDistance] = orderOfVisit

print("The optimal order the cities should be visited for the lowest distance travelled is:")
for cityNumber in tspDictionary[lowestDistance]:
    print(cities[cityNumber])
print("The total distance for this path is", lowestDistance, " miles")

