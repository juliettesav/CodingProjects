# Tuples are immutable array-like structures 

point = (5, 2)

x = point[0]
y = point[1]

def calc(side_len):
    area = side_len * side_len
    preimeter = 4 * side_len
    return(area, preimeter)

result = calc(side_len=5)
print(f'Area: {result[0]}')
print(f'Perimeter: {result[1]}')

def calc_rec(side1_len, side2_len):
    area = side1_len *  side2_len
    return(area)

rec_result = calc_rec(side1_len=6,side2_len=7)
print(f'Rectange Perimeter: {rec_result}')