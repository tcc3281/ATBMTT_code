from modernblockcode import AES

if __name__ == '__main__':
    matrix = [['87', 'F2', '4D', '97'], ['6E', '4C', '90', 'EC'],
              ['46', 'E7', '4A', 'C3'], ['A6', '8C', 'D8', '95']]
    k = AES.mixcolumns(matrix)
    print(k)
    k_1 = AES.invmixcolumns(k)
    print(k_1)
