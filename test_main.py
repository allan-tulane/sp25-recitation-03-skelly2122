from main import *

def test_multiply():
    # Test basic multiplication
    assert quadratic_multiply(BinaryNumber(2), BinaryNumber(2)) == 2*2
    assert quadratic_multiply(BinaryNumber(3), BinaryNumber(3)) == 3*3
    assert quadratic_multiply(BinaryNumber(10), BinaryNumber(5)) == 10*5
    
    # Test with larger numbers
    assert quadratic_multiply(BinaryNumber(100), BinaryNumber(100)) == 100*100
    assert quadratic_multiply(BinaryNumber(256), BinaryNumber(256)) == 256*256
    
    # Test with zero
    assert quadratic_multiply(BinaryNumber(0), BinaryNumber(5)) == 0
    assert quadratic_multiply(BinaryNumber(5), BinaryNumber(0)) == 0
    
    # Test with one
    assert quadratic_multiply(BinaryNumber(1), BinaryNumber(10)) == 10
    assert quadratic_multiply(BinaryNumber(10), BinaryNumber(1)) == 10

def test_quadratic_multiply_time():
    # Test running time for various input sizes
    numbers = [(BinaryNumber(2**i), BinaryNumber(2**i)) for i in range(8)]
    times = []
    
    for x, y in numbers:
        time_taken = test_quadratic_multiply(x, y, quadratic_multiply)
        times.append(time_taken)
        print(f"Time for {x.decimal_val} * {y.decimal_val}: {time_taken:.2f}ms")
