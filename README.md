# Algorithm1_project_pm2.5
Program Description: Visualizing Pollution Monitoring Stations Graph

## Overview
This Python project models a network of pollution monitoring stations as a graph and provides functionality to find the least pollution path between two stations.
![Station Graph](C:\Users\Sunthorn\Algorithm1_project_pm2.5\Graph_station.png)
## Graph Representation
- **Vertices**: Pollution monitoring stations, labeled with their station names (e.g., 'Station1', 'Station2', etc.).
- **Edges**: Connections between stations, representing the proximity or distance between them. They are undirected edges.
- **Weights**: Each edge has a weight representing the distance between connected stations, measured in kilometers.

## Problem Statement
The problem addressed by this project is to find the least pollution path from a given source station to a destination station. The least pollution path minimizes the sum of the PM2.5 values along the path.

## Algorithm Used
The project uses Dijkstra's algorithm to find the least pollution path:
- Dijkstra's algorithm is a graph search algorithm that finds the shortest paths from a source vertex to all other vertices in a weighted graph.

## Running Time Complexity
The running time of the entire algorithm, including graph construction and Dijkstra's algorithm, is as follows:
- **Graph Construction**: \( O(n * m) \), where \( n \) is the number of stations and \( m \) is the number of neighbors per station.
- **Dijkstra's Algorithm**: \( O((n + m) log n) \).
- **Total Running Time**: \( O(n * m + (n + m) \log n) \).

## Usage
- You can provide your pollution monitoring station data, specifying the stations and their connections.
- After providing the data, the program will calculate and display the shortest path between two given stations,
PM2.5 values along the path and total distance along the path

## Dependencies
- `networkx`: A Python library for creating and manipulating graphs and networks.
- `matplotlib`: A plotting library for creating static, interactive, and animated visualizations in Python.

## How to Run
1. Install the required dependencies using `pip install networkx matplotlib`.
2. Run the Python script `main.py` to find the shortest path and pollution for each station.
