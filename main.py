from pprint import pprint

import numpy as np
import galois

P = 0x73eda753299d7d483339d80809a1d80553bda402fffe5bfeffffffff00000001

def main():

    m = transpose(read_file("leaked_message_hashes.txt"))
    u = read_file("username_hash.txt")[0]
    print(u)
    GF = galois.GF(P)
    c = GF(u)

    x = invert_matrix(m, P)
    pprint(x)

    res = np.matmul(x,c)

    pprint(res)


    write_file("coefficients.txt", res)


def read_file(filename: str) -> list:
    with open(filename, "r") as f:
        lines = f.readlines()
    m = [[None]*256 for i in range(len(lines))]
    for i in range(len(lines)):
        line = lines[i].strip()
        if line:
            for j in range(len(line)):
                m[i][j] = int(line[j])
    return m


def transpose(m: list) -> list:
    return list(map(list, zip(*m)))


def write_file(filename: str, x) -> None:
    outfile = open(filename, "w")
    out = ""
    for xi in x:
        out += str(xi) + " "

    outfile.write(out.strip())
    outfile.close()


def invert_matrix(m: list, P: int) -> list:
    GF = galois.GF(P)
    x = GF(m)
    y = np.linalg.inv(x)
    return y





if __name__ == "__main__":
    main()