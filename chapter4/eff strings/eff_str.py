# eff_str.py
# demos left, center, and right alignment and decimals
# this will be very important in Chapter 4

def main():

    n = 64
    rt2 = n ** 0.5      ## square root of n
    rt3 = n ** (1/3)    ## cube  root of n

    # n is LEFT-aligned with 2 decimals in a 10-character column
    # rt2 is CENTERED with 5 decimals in a 12-character column
    # rt3 is RIGHT-aligned with 5 decimals in a 12-character column
    
    print(f'|{n:<10.2f}|{rt2:^12.5f}|{rt3:>12.5f}|')
    print(f'|{n:<10.2f}|{rt2:^12.5f}|{rt3:>12.5f}|')
    print(f'|{n:<10.2f}|{rt2:^12.5f}|{rt3:>12.5f}|')    
main()
    
