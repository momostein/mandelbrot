# Mandelbrot set math


def mandelbrot(c, max_i=500):
    def f(z):
        return z**2 + c

    z = 0

    for i in range(max_i):
        z = f(z)

        if abs(z) > 2:
            return (False, i)

    return (True, max_i)


if __name__ == "__main__":
    print(mandelbrot(complex(-0.3, 0.1)))
    print(mandelbrot(complex(1, 0)))
