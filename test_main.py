from main import *  # Get all our functions from main.py


def test_multiply():
    # Let's test our multiplication with different scenarios

    # Basic tests - like checking if 2x2=4
    assert quadratic_multiply(BinaryNumber(2), BinaryNumber(2)) == 2 * 2
    assert quadratic_multiply(BinaryNumber(3), BinaryNumber(3)) == 3 * 3
    assert quadratic_multiply(BinaryNumber(10), BinaryNumber(5)) == 10 * 5

    # Testing bigger numbers - making sure it works for harder cases
    assert quadratic_multiply(BinaryNumber(100),
                              BinaryNumber(100)) == 100 * 100
    assert quadratic_multiply(BinaryNumber(256),
                              BinaryNumber(256)) == 256 * 256

    # Testing with zero - anything times zero should be zero!
    assert quadratic_multiply(BinaryNumber(0), BinaryNumber(5)) == 0
    assert quadratic_multiply(BinaryNumber(5), BinaryNumber(0)) == 0

    # Testing with one - anything times one should be itself
    assert quadratic_multiply(BinaryNumber(1), BinaryNumber(10)) == 10
    assert quadratic_multiply(BinaryNumber(10), BinaryNumber(1)) == 10


def test_timing():
    # Let's see how fast our code runs with different size numbers
    # Like timing how long it takes to solve easy vs. hard problems

    # Test with powers of 2 (2, 4, 8, 16, etc.)
    numbers = [(BinaryNumber(2**i), BinaryNumber(2**i)) for i in range(8)]
    times = []

    # Time each multiplication and print the results
    for x, y in numbers:
        time_taken = time_quadratic_multiply(x, y, quadratic_multiply)
        times.append(time_taken)
        print(
            f"Time for {x.decimal_val} * {y.decimal_val}: {time_taken:.2f}ms")
