import random
import stdio


def check(cols, rows):
    """
    Verifies size of barcode.
    """
    if cols and rows < 5:
        print "Make Column and row >= 5!"

def create_barcode(cols, rows, sym, sym1):
    '''
    Creates a barcode that is in a slanted shape.
    Cols and rows are int, sym and sym1 must be string.
    '''
    if check(cols, rows + 1):
        pass
    for i in range(1, cols):
        for j in  range(1, rows + 1):
            ran = random.randint(1, cols)
            if (i % j) % ran != 0:
                stdio.write(sym)
            stdio.write(sym1)
        stdio.writeln()

def slant_barcode(cols, rows, sym, sym1):
    '''
    Creates a barcode that is in a slanted shape.
    Cols and rows are int, sym and sym1 must be string.
    '''
    if check(cols, rows):
        pass
    for i in range(1, cols + 1):
        for j in range(1, rows + 1):
            ran = random.randint(1, cols)
            if (i * j) % ran != 0:
                stdio.write(sym)
            stdio.write(sym1)
        stdio.writeln()

def triang(cols, sym):
    '''
    Prints pattern in increasing order, shape of right triangle.
    Cols is an int, sym must be string.
    '''
    for i in range(1, cols + 1):
        for j in range(1, cols + 1):
            if i / j != 0:
                stdio.write(sym)
            stdio.write(' ')
        stdio.writeln()

def side_triang(cols, sym, sym1):
    """
    --In progress, Prints a trianle shape to the right with space on the left.
    intended to be reflection of triang().
    """
    col = cols + 1
    for i in range(1, cols + 1):
        col -= 1
        for j in range(1, cols + 1):
            if i % j == 0:
                stdio.write(sym)
            stdio.write(sym1 * col)
        stdio.writeln()

def opp_triang(cols, sym):
    """
    Prints an upside down right triangle.
    Cols is an int, sym must be string.
    """
    for i in range(2, cols + 2):
        for j in range(cols + 1, 0, -1):
            if j / i != 0:
                stdio.write(sym)
            stdio.write(' ')
        stdio.writeln()


def pyramid_down(cols, sym1):
    '''
    Prints upside down pyramid.
    Cols is an int, sym must be string.
    '''
    for i in range(1, cols + 1):
        for j in range(1, cols + 1):
            if j / i != 0:
                stdio.write(sym1)
            stdio.write(" ")
        stdio.writeln()

def pyramid_up(cols, sym1):
    """
    Draws a pyramid. Add a space to your sym1 parameter.
    Cols is an int, sym must be string.
    """
    for i in range(cols + 1, 0, -1):
        stdio.writeln(' ' * i + (sym1 + " ") * ((cols + 1) - i))



def square(cols, rows, sym1):
    '''
    Draws pattern in square form. Add a space to your sym parameter.
    Cols and Rows are int, sym must be string.
    '''
    for i in range(1, cols + 1):
        for j in range(1, rows + 1):
            if i > 0:
                stdio.write(sym1)
        stdio.writeln()

'''def circ(self, cols, rows)'''


def building(cols, sym1):
        pyramid_up(cols, sym1)
        pyramid_down(cols, sym1)

def main():
    sqare(10, 10, "* ")
    stdio.writeln("SQUARE")
    opp_triang(10, "*")
    stdio.writeln("OPP TRIANGLE")
    pyramid_up(10, "* ")
    stdio.writeln("PYRAMID")
    pyramid_down(10, '* ')
    stdio.writeln("UPSIDE DOWN PYRAMID")
    side_triang(6, "#", " ")
    stdio.writeln("SIDE TRIANGLE")
    triang(20, "*")
    stdio.writeln("TRIANGLE")
    create_barcode(10, 10, "* ", " *")
    stdio.writeln("BARCODE")
    slant_barcode(20, 20, "*", " ")
    stdio.writeln("SLANT BARCODE")


if __name__ == '__main__':
    main()
