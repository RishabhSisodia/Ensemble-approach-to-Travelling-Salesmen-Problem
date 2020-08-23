# Project Title
### Ensemble Approach to Travelling Salesman Problem

## Getting Started
* Clone the repo
* ```run TSPGenetic.py```

## Description
The traveling-salesman problem is one of the classical NP-Complete problems. No current algorithms are available which can solve these problems in polynomial time, that is, the number of steps grows as a polynomial according to the size of the input. The traveling-salesman problem involves a salesman who must make a tour of a number of cities using the shortest path available. For each number of cities n, the number of paths which must be explored is n!, causing this problem to grow exponentially rather than as a polynomial. Three separate algorithms **(Genetic, Greedy and Branch & Bound)** are examined and analyzed against the **Ensembled alogrithm** consisting all three of them. These four algorithms were tested on four variations of TSP - **Burma14, Ulysses22, Bays29, Berlin52**. 

## Results
``` Yaxis = Fitness = 1/optimal distance to travel all cities``` 

<p align="center">
  <img src="https://github.com/RishabhSisodia/Ensemble-approach-to-Travelling-Salesmen-Problem/blob/master/Burma14.JPG" alt="Project Layout" width="400px" height="300px"/>
</p>
<p align="center">
  <img src="https://github.com/RishabhSisodia/Ensemble-approach-to-Travelling-Salesmen-Problem/blob/master/Ulysses22.JPG" alt="Project Layout" width="400px" height="300px"/>
</p>
<p align="center">
  <img src="https://github.com/RishabhSisodia/Ensemble-approach-to-Travelling-Salesmen-Problem/blob/master/Bays29.JPG" alt="Project Layout" width="400px" height="300px"/>
</p>
<p align="center">
  <img src="https://github.com/RishabhSisodia/Ensemble-approach-to-Travelling-Salesmen-Problem/blob/master/Berlin52.JPG" alt="Project Layout" width="400px" height="300px"/>
</p>

## Conclusion
From the graphs we can observe that although the normal Genetic Algorithm code for TSP works faster than the code for greedy and branch and bound, it is way far from the optimum solution. In some cases like Ulysses22 cities problem, the normal GA algorithm provided a better solution. For some problems like Burma14 with very less number of cities, both the algorithms provided optimum solutions in the number of generations specified.
We can hereby conclude that for problems with larger number of cities, the GA with greedy and branch and bound seed, code for TSP works way better than the normal GA code.


## Contributors
Created the project in a team with ***[Saikat Bhattacharyya](https://github.com/sai-kat)***.


## License
This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/RishabhSisodia/Ensemble-approach-to-Travelling-Salesmen-Problem/blob/master/LICENSE) file for details
