def main():
    N = int(input()) 
    A = input()

    def solve_node(left, length):
        if length == 1:
            bit = int(A[left])
            if bit == 0:
                return (0, 1, 0)
            else:
                return (1, 0, 1)

        seg = length // 3
        c0_1, c1_1, f1 = solve_node(left, seg)
        c0_2, c1_2, f2 = solve_node(left + seg, seg)
        c0_3, c1_3, f3 = solve_node(left + 2 * seg, seg)

        s = f1 + f2 + f3
        if s >= 2:
            finalBit = 1
        else:
            finalBit = 0

        cost0 = min(
            c0_1 + c0_2 + c0_3,  
            c0_1 + c0_2 + c1_3,  
            c0_1 + c1_2 + c0_3,  
            c1_1 + c0_2 + c0_3   
        )

        cost1 = min(
            c1_1 + c1_2 + c1_3, 
            c1_1 + c1_2 + c0_3,  
            c1_1 + c0_2 + c1_3, 
            c0_1 + c1_2 + c1_3  
        )

        return (cost0, cost1, finalBit)

    cost0, cost1, finalBit = solve_node(0, 3**N)

    if finalBit == 0:
        print(cost1)
    else:
        print(cost0)

if __name__ == '__main__':
    main()