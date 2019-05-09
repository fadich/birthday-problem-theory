import sys
import argparse

from birthday import Model


def people_number_validator(value):
    if value is None:
        return value
    if not value.isdigit():
        raise argparse.ArgumentTypeError('People number should be positive integer')

    value = int(value)
    if value < 2:
        raise argparse.ArgumentTypeError('People number should not be less than 2')

    return value


def run_model(iterations: int, people_min: int, people_max: int):
    for people in range(people_min, people_max + 1):
        results = []
        for i in range(iterations):
            model = Model(people)
            results.append(model.has_coincidence)
            sys.stdout.write(f'{i}/{iterations}\r')

        probability = sum(results) / len(results)
        sys.stdout.write('People: {:<3} | probability: {:.2f}%\n'.format(people, probability * 100))


def main():
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('-p', '-n', '--people', dest='people', type=people_number_validator, help='People number')
    parser.add_argument('-i', '--iter', '--iterations', dest='iterations', type=int, default=1000,
                        help='Number of iterations')
    parser.add_argument('-d', '--debug', dest='debug', action='store_true', help='set debug log level')

    args = parser.parse_args()

    try:
        run_model(
            iterations=args.iterations,
            people_min=args.people or 2,
            people_max=args.people or 365)
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    sys.exit(main())
