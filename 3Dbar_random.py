import sys
import random

def make_m(val, maxVal):
    return (10*abs(val))/(0.4*maxVal)

def make_line(x, y, sw, function, m1 = 0, m2 = 0):
    if function == "square":
        return str(x) + " " + str(y) + " " + str(sw) + " " + str(255) + " square\n"
    if function == "above" or function == "below" or function == "left" or function == "right":
        return str(x) + " " + str(y) + " " + str(sw * 0.93) + " " + str(sw) + " " + str(m1) + " " + str(255) + " " + function + "\n"
    if function == "top_left" or function == "top_right" or function == "bottom_left" or function == "bottom_right":
        return str(x) + " " + str(y) + " " + str(m1) + " " + str(m2) + " " + str(sw * 0.93) + " " + str(sw) + " " + str(255) + " "  + function + "\n"

def make_bars(maxX, maxY, num):
    output = ""
    sw = 2
    for i in range(num):
        x = random.uniform(-0.4*(maxX), 0.4*maxX)
        y = random.uniform(-0.4*maxY, 0.4*maxY)
        
        if abs(x) < 0.07*maxX and abs(y) < 0.07*maxY:
            #x and y both close to axis
            output += make_line(x, y, sw, "square") 
        elif abs(x) < 0.07*maxX:
            # only x close to axis
            m = make_m(y, maxY)
            if y > 0:
                output += make_line(x, y, sw, "above", m)
            else:
                output += make_line(x, y, sw, "below", m)
        elif abs(y) < 0.07*maxY:
            # only y close to axis 
            m = make_m(x, maxX)
            if x > 0:
                output += make_line(x, y, sw, "right", m)
            else:
                output += make_line(x, y, sw, "left", m)
        else:
            # neither
            m1 = make_m(x, maxX)
            m2 = make_m(y, maxY)
            if x > 0:
                if y > 0:
                    output += make_line(x, y, sw, "top_right", m1, m2)
                else:
                    output += make_line(x, y, sw, "bottom_right", m1, m2)
            else:
                if y > 0:
                    output += make_line(x, y, sw, "top_left", m1, m2)
                else:
                    output += make_line(x, y, sw, "bottom_left", m1, m2)
    return output

def main():
    fileName = '3Dbar_random3.eps'
    rules = ""
    maxX = int(sys.argv[1])
    maxY = int(sys.argv[2])
    num = int(sys.argv[3])

    with open('3Dbar_functions.txt', 'r') as file:
        rules_list = file.readlines()
        for line in rules_list:
            rules += line
        rules += '\n\n'
    
    with open(fileName, 'w') as file:
        file.write('%!PS-Adobe-3.0 EPSF-3.0\n')
        file.write('%%BoundingBox: 0 0 ' + str(maxX) + ' ' + str(maxY) + '\n\n')
        file.write(str(maxX/2) + ' ' + str(maxY/2) + ' translate\n\n')
        file.write(rules)
        file.write(make_bars(maxX, maxY, num))
        file.write('showpage')
main()