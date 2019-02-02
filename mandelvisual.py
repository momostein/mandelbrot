import pygame
from mandelmath import mandelbrot

WIDTH, HEIGHT = (600, 600)
running = False

SHOW = 0
CLICK = 1


def main():
    global running
    screen = pygame.display.set_mode([WIDTH, HEIGHT])

    running = True

    z_max = complex(0.8, 1.5)
    z_min = complex(-2.2, -1.5)

    pxArray = pygame.PixelArray(screen)
    calculate(z_min, z_max, pxArray)

    state = SHOW

    first = (0, 0)
    second = (0, 0)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                print("muis")
                if state == SHOW:
                    first = pygame.mouse.get_pos()
                    print("first")
                    state = CLICK
                    continue

                if state == CLICK:
                    print("second")
                    second = pygame.mouse.get_pos()
                    state = SHOW

                    new_min = transform(z_min, z_max, first)
                    new_max = transform(z_min, z_max, second)

                    calculate(new_min, new_max, pxArray)

                    z_min = new_min
                    z_max = new_max

                    continue

        if state == CLICK:
            rect = calc_rect(first, pygame.mouse.get_pos())
            pygame.draw.rect(screen, pygame.Color(255, 255, 255),
                             rect, 2)

        pygame.display.flip()
    pygame.quit()


def transform(z_min, z_max, pos):
    z = complex(*pos)

    dz = z_max - z_min

    return z_min + complex(z.real * dz.real / WIDTH, z.imag * dz.imag / HEIGHT)


def calculate(min, max, pxArray):
    global running
    shape = pxArray.shape
    for i in range(shape[0]):
        for j in range(shape[1]):

            c = transform(min, max, (i, j))

            color = calc_color(*mandelbrot(c))

            pxArray[i, j] = color

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()


def calc_color(mandel, n):
    if mandel:
        return pygame.Color(0, 0, 0)
    else:
        color = pygame.Color(0, 0, 0)
        hue = int(n * 36 / 20) % 360
        color.hsva = (int(hue),
                      100,
                      100,
                      100)

        return color


def calc_rect(first, second):
    size = (second[0] - first[0],
            second[1] - first[1])

    return pygame.Rect(first, size)


if __name__ == '__main__':
    main()
