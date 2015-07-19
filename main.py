from BFSSolution import *
from AStarSolution import *
from HillClimbingSolution import *

def main():
    """A function demonstrating the use of the GameTreeNode class.
    """ 
    # read input.txt
    with open('input.txt', 'r') as input_file:
        game_state_as_array = input_file.read().split()

    # write report into output.txt
    with open('output.txt','a') as output_file:
        solution = BFSSolution(game_state_as_array)
        solution.performSearchMethod()
        output_file.write("Algorithm: "+solution.method_name+"\n")
        output_file.write("Heuristic function: "+solution.heuristic_estimate+"\n")
        output_file.write("Elapsed time: "+str(solution.elapsed_time)+" s\n")
        output_file.write("Number of steps required: "+str(solution.countStep())+"\n\n")
        output_file.write(solution.showPath())
        output_file.write("--------------------------------------------------\n\n")

        solution = HillClimbingSolution_H1(game_state_as_array)
        solution.performSearchMethod()
        output_file.write("Algorithm: "+solution.method_name+"\n")
        output_file.write("Heuristic function: "+solution.heuristic_estimate+"\n")
        output_file.write("Elapsed time: "+str(solution.elapsed_time)+" s\n")
        output_file.write("Number of steps required: "+str(solution.countStep())+"\n\n")
        output_file.write(solution.showPath())
        output_file.write("--------------------------------------------------\n\n")

        solution = HillClimbingSolution_H2(game_state_as_array)
        solution.performSearchMethod()
        output_file.write("Algorithm: "+solution.method_name+"\n")
        output_file.write("Heuristic function: "+solution.heuristic_estimate+"\n")
        output_file.write("Elapsed time: "+str(solution.elapsed_time)+" s\n")
        output_file.write("Number of steps required: "+str(solution.countStep())+"\n\n")
        output_file.write(solution.showPath())
        output_file.write("--------------------------------------------------\n\n")

        solution = HillClimbingSolution_H3(game_state_as_array)
        solution.performSearchMethod()
        output_file.write("Algorithm: "+solution.method_name+"\n")
        output_file.write("Heuristic function: "+solution.heuristic_estimate+"\n")
        output_file.write("Elapsed time: "+str(solution.elapsed_time)+" s\n")
        output_file.write("Number of steps required: "+str(solution.countStep())+"\n\n")
        output_file.write(solution.showPath())
        output_file.write("--------------------------------------------------\n\n")

        solution = AStarSolution_H1(game_state_as_array)
        solution.performSearchMethod()
        output_file.write("Algorithm: "+solution.method_name+"\n")
        output_file.write("Heuristic function: "+solution.heuristic_estimate+"\n")
        output_file.write("Elapsed time: "+str(solution.elapsed_time)+" s\n")
        output_file.write("Number of steps required: "+str(solution.countStep())+"\n\n")
        output_file.write(solution.showPath())
        output_file.write("--------------------------------------------------\n\n")

        solution = AStarSolution_H2(game_state_as_array)
        solution.performSearchMethod()
        output_file.write("Algorithm: "+solution.method_name+"\n")
        output_file.write("Heuristic function: "+solution.heuristic_estimate+"\n")
        output_file.write("Elapsed time: "+str(solution.elapsed_time)+" s\n")
        output_file.write("Number of steps required: "+str(solution.countStep())+"\n\n")
        output_file.write(solution.showPath())
        output_file.write("--------------------------------------------------\n\n")

        solution = AStarSolution_H3(game_state_as_array)
        solution.performSearchMethod()
        output_file.write("Algorithm: "+solution.method_name+"\n")
        output_file.write("Heuristic function: "+solution.heuristic_estimate+"\n")
        output_file.write("Elapsed time: "+str(solution.elapsed_time)+" s\n")
        output_file.write("Number of steps required: "+str(solution.countStep())+"\n\n")
        output_file.write(solution.showPath())
        output_file.write("--------------------------------------------------\n\n")

if __name__ == '__main__':
    main()
