import argparse

import problem1
import problem141
import problem142
import problem206
import problem24


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
        24: problem24.solve,
        141: problem141.solve,
        142: problem142.solve,
        206: problem206.solve,
    }

    if problem in problems:
        problems[problem]()
    else:
        print("Problem {} not exist.".format(problem))


if __name__ == '__main__':
    main()
