import sys
import argparse

from birthday import Model


def run_model(iterations: int, people_min: int, people_max: int):
    for people in range(people_min, people_max):
        results = []
        for i in range(iterations):
            model = Model(people)
            results.append(model.has_coincidence)
            sys.stdout.write(f'{i}/{iterations}\r')

        probability = sum(results) / len(results)
        sys.stdout.write('People: {:<3} | probability: {:.2f}%\n'.format(people, probability * 100))


def main():
    parser = argparse.ArgumentParser(description='')
    # parser.add_argument('people', type=int, help='People number')
    parser.add_argument('-i', '--iter', '--iterations', dest='iterations', type=int, default=1000,
                        help='Number of iterations')
    parser.add_argument('-d', '--debug', dest='debug', action='store_true', help='set debug log level')

    args = parser.parse_args()

    try:
        run_model(args.iterations, 2, 366)
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    sys.exit(main())
