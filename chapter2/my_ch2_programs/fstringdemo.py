### f string demo
### demos left, center and right

def main():
    n = 64
    rt2 = n ** 0.5        #to the power of 2
    rt3 = n ** (1/3)      #to the power of 3

    print(f'|{n:<10.2f}|{rt2:^10.3f}|{rt3:>10.4f}|')
    #n is left aligned in a 10 character column with 2 decimals
    #rt2 is center aligned in a 10 character column with 3 decimal places
    #rt3 is right aligned in a 10 character column with 4 decimal places
    #pipe is just to show separation when printed

main()