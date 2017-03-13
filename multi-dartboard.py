import random, math, argparse
import multiprocessing as mp

def throwDarts(object, darts):
	""" Simulates throwing darts at a dartboard.

	This function places random points (darts) on a representational
	square plane that contains a circle. The results are then used to
	estimate the value of pi.

	Args:
		object: a queue object used as a locking mechanism for multiprocessing.
		darts: a positive integer representing the number of darts to throw (the
		number of random points generated on the plane).
	"""
	total = 0
	for i in range(darts):
		x = random.uniform(-1,1)
		y = random.uniform(-1,1)
		if (x**2 + y**2)**0.5 <= 1: # dart falls within area of circle 
			total += 1
	object.put(total/darts * 4) # put estimated pi in queue object

def multiprocess(boards, darts):
	""" Simulates multiple dartboard situations.

	This function creates a given amount of processes and assigns the throwDarts
	function to each one individually. By utilizing a queue, this function computes
	the average estimated pi value of all the processes.

	Args:
		boards: a positive integer representing the number of dartboards (processes)
		to use.
		darts: a positive integer representing the number of darts to throw for each
		dartboard. This value is passed as a parameter for the throwDarts function.

	Returns:
		A positive float representing the average of all estimated pi's through all
		generated processes.
	"""
	processes = []
	queue = mp.Queue()

	# create the processes:
	for i in range(boards):
		job = mp.Process(target=throwDarts, args=(queue, darts))
		processes.append(job)
		job.start() # start the current process

	# join the processes:
	for process in processes:
		process.join()

	# add the results from each process in the queue to total:
	total = 0
	while not queue.empty():
		total += queue.get()

	return total / boards # calculate average of estimated pi values

def main():
	# use argparse for direct user input:
	parser = argparse.ArgumentParser()
	parser.add_argument('cores', type=int)
	parser.add_argument('darts', type=int)
	args = parser.parse_args()

	boards = args.cores		# the number of dartboards (processes)
	darts_to_throw = args.darts # the number of darts to throw for each board
	averageDartboards = multiprocess(boards, darts_to_throw)
	
	print("The real pi is:", math.pi)
	print("The calculated average of", boards, "dartboards is:", averageDartboards)

if __name__ == '__main__':
	main()