import numpy as np

def square(x):
    return x*x

def coulomb(r):
    assert type(r) in [float, int], "You passed an invalid argument"
    if r == 0:
        raise ValueError("r cannot equal 0")
    return 1/abs(r)

# def central_difference(f, x, h):
#     """
#     f(x + h) - f(x - h)
#     ------------------- \approx f'(x)
#             2*h
#     """
#     return (f(x+h)-f(x-h))/(2*h)
#
# if __name__ == "__main__":
#     for i in range(2, 8):
#         h = 10**(-i)
#         print("{}\t{}".format(h,abs(central_difference(np.sin, 0.0, h) - 1)))
