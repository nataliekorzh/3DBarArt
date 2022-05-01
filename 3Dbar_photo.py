import sys
import random

def parse_image(fileName):
    rows = 0
    cols = 0
    image = []
    with open(fileName, 'r') as file:
        file.readline()
        dimensions = file.readline().strip().split()
        rows = int(dimensions[0])
        cols = int(dimensions[1])
        maxPixel = file.readline()
        for i in range(rows):
            image.append([])
            for j in range(cols):
                image[i].append(int(file.readline().strip()))

    return image, rows, cols

def make_bars(maxX, maxY, x, y, color):
    output = ""
    sw = 4
    if x > maxX - 0.07*maxX and x < maxX + 0.07*maxX and y > maxY - 0.07*maxY and y < maxY + 0.07*maxY:
        #x and y both close to axis
        output += make_line(x, y, sw, color, "square") 
    elif x > maxX/2 - 0.07*maxX/2 and x < maxX/2 + 0.07*maxX/2:
        # only x close to axis
        m = make_m(y, maxY/2)
        if y > maxY/2:
            output += make_line(x, y, sw, color, "above", m)
        else:
            output += make_line(x, y, sw, color, "below", m)
    elif y > maxY/2 - 0.07*maxY/2 and y < maxY/2 + 0.07*maxY/2:
        # only x close to axis 
        m = make_m(x, maxX/2)
        if x > maxX/2:
            output += make_line(x, y, sw, color, "right", m)
        else:
            output += make_line(x, y, sw, color, "left", m)
    else:
        # neither
        m1 = make_m(x, maxX/2)
        m2 = make_m(y, maxY/2)
        if x > maxX/2:
            if y > maxY/2:
                output += make_line(x, y, sw, color, "top_right", m1, m2)
            else:
                output += make_line(x, y, sw, color, "bottom_right", m1, m2)
        else:
            if y > maxY/2:
                output += make_line(x, y, sw, color, "top_left", m1, m2)
            else:
                output += make_line(x, y, sw, color, "bottom_left", m1, m2)
    return output

def make_m(val, maxVal):
    if val < maxVal:
        return 8*(maxVal - val)/maxVal
    else:
        return 8*(val - maxVal)/maxVal

def make_line(x, y, sw, color, function, m1 = 0, m2 = 0):
    if function == "square":
        return str(x) + " " + str(y) + " " + str(sw) + " " + str(color) + " square\n"
    if function == "above" or function == "below" or function == "left" or function == "right":
        return str(x) + " " + str(y) + " " + str(sw * 0.93) + " " + str(sw) + " " + str(m1) + " " + str(color) + " " + function + "\n"
    if function == "top_left" or function == "top_right" or function == "bottom_left" or function == "bottom_right":
        return str(x) + " " + str(y) + " " + str(m1) + " " + str(m2) + " " + str(sw * 0.93) + " " + str(sw) + " " + str(color) + " " + function + "\n"
        
def main():
    fileName = 'output.eps'
    rules = ""
    imageFile = sys.argv[1]

    with open('3Dbar_functions.txt', 'r') as file:
        rules_list = file.readlines()
        for line in rules_list:
            rules += line
        rules += '\n\n'
    
    image, maxX, maxY = parse_image(imageFile)
    sw = 8
    with open(fileName, 'w') as file:
        file.write('%!PS-Adobe-3.0 EPSF-3.0\n')
        file.write('%%BoundingBox: 0 0 ' + str(sw*maxX) + ' ' + str(sw*maxY) + '\n\n')
        file.write(rules)
        on = 255
        for i in range(maxX):
            for j in range(maxY):
                x = sw + sw*j
                y = sw + sw*(maxX-1-i)
                if image[i][j] < 100:
                    if image[i][j] < 75:
                        file.write(make_bars(sw*maxX, sw*maxY, x, y, 0))
                    else:
                        file.write(make_bars(sw*maxX, sw*maxY, x, y, 255))
                    #print((image[i][j]/255)/0.3)
                    #file.write(make_bars(sw*maxX, sw*maxY, x, y, (image[i][j]/255)/0.3)) #for grey scale
                    #file.write(make_bars(sw*maxX, sw*maxY, x, y, 255))
                    #if on == 0:
                    #    on = 255
                    #elif on == 255:
                    #    on = 0
                #elif image[i][j] == 0:
                    #file.write(make_bars(sw*maxX, sw*maxY, x, y, 0))
        file.write('showpage')

main()
