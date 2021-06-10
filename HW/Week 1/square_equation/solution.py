import sys

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])


if __name__ == "__main__":
    print(int((-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)))
    print(int((-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)))
