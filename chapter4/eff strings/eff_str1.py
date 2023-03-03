# eff_str1.py
# demos left, center, and right alignment

def main():

    for n in range(1,5):
        rt2 = n ** 0.5
        rt3 = n ** (1/3)
        print(f'|{n:<10.2f}|{rt2:<12.5f}|{rt3:<12.5f}|')
    print()
    for n in range(1,5):
        rt2 = n ** 0.5
        rt3 = n ** (1/3)
        print(f'|{n:^10.2f}|{rt2:^12.5f}|{rt3:^12.5f}|')
    print()
    for n in range(1,5):
        rt2 = n ** 0.5
        rt3 = n ** (1/3)
        print(f'|{n:>10.2f}|{rt2:>12.5f}|{rt3:>12.5f}|')
        
main()
    
