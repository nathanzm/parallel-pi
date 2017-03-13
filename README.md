# Monte Carlo Approach to Pi
## Desciption:
This Python program calculates the value of pi through the simulation of throwing darts at dartboard. 

Specifically, there are multiple processes run in parallel to represent varied simulations of dartboards, which allows for many estimated values of pi to be combined into an average for a more accurate result.

In general, the more darts thrown and the more total dartboard simulations there are, the more accurate the calculation of pi is. It is also interesting to see how different execution times react to the number of processes generated for the program. These results will vary depending on your processor, but generally the program becomes increasingly deficient once the number of processes exceeds your CPU's number of cores.

## Usage:
### Input:
The program requires 2 positive integers: the first one representing the number of dartboards there are (the number of individual processes created), the second one representing the number of darts to be thrown at each dartboard.

For example, if you ran from terminal: `python multi-dartboard.pi 1000 8`, there would conceptually be 8 dartboards, and each one would have 1000 darts thrown at them randomly.

### Output:
The program outputs Python's `math` module value of pi along with the estimated value of pi as determined by the average of results from each process.