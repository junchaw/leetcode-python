import argparse
import importlib
import time


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("problem", nargs='?', type=int)

    args = parser.parse_args()

    problem_number = args.problem

    if problem_number is None:
        print("Which problem?")
        return

    try:
        problem = importlib.import_module(
            'problems.problem{}'.format(problem_number))
        start_time = time.time()
        problem.solve()
        print("--- {} seconds used ---".format(time.time() - start_time))
    except ImportError as e:
        print("Problem {} not exist.".format(problem_number))


if __name__ == '__main__':
    main()
