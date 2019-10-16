import argparse
import time

from problems import problem232, problem236, problem141, problem24, problem142, \
    problem235, problem1, problem20, problem242, problem225, problem239, \
    problem206, problem25, problem98, problem703


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("problem", nargs='?', type=int)

    args = parser.parse_args()

    problem = args.problem

    if problem is None:
        print("Which problem?")
        return

    problems = {
        1: problem1.solve,
        20: problem20.solve,
        24: problem24.solve,
        25: problem25.solve,
        98: problem98.solve,
        141: problem141.solve,
        142: problem142.solve,
        206: problem206.solve,
        225: problem225.solve,
        232: problem232.solve,
        235: problem235.solve,
        236: problem236.solve,
        239: problem239.solve,
        242: problem242.solve,
        703: problem703.solve,
    }

    if problem in problems:
        start_time = time.time()
        problems[problem]()
        print("--- {} seconds used ---".format(time.time() - start_time))
    else:
        print("Problem {} not exist.".format(problem))


if __name__ == '__main__':
    main()
