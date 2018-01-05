import addmath
import math

def pascalTriangle(length):

    assert length>5 and type(length)==int

    length+=1
    triangle=[[1], [1, 1]]

    rcursor=2
    vcursor=0

    while(len(triangle)<length):
        triangle.append([1, ])
        while(True):
            try:
                triangle[rcursor].append(triangle[rcursor-1][vcursor]+triangle[rcursor-1][vcursor+1])
                vcursor+=1
            except:
                triangle[rcursor].append(1)
                vcursor=0
                rcursor += 1
                break

    return triangle

def pascalLookup(row, column):
    triangle=pascalTriangle(row+1)
    return triangle[row][column]

def ouputPascalResults(n):
    file=open("outfile.txt", "w")
    triangle=pascalTriangle(n)

    centered=True

    for i in range(len(triangle)):
        row=triangle[i]

        if(centered):
            whitespaceNum=int(len(str(triangle[-1]))/2-len(str(row))/2)
            for x in range(whitespaceNum):
                print(" ", end="")
                file.write(" ")

        line=str(row)
        line=line.replace(",", "")
        if(centered):
            line=line.replace(" ", "  ")
        print(line[1:-1])
        file.write(line[1:-1]+'\n')

print(pascalLookup(1000, 500))