# eff_str2.py
# demos center-formatted table

def main():
    
    # column headings first
    print('+----------+------------+------------+')
    print(f'|{"Number":^10}|{"SQ. ROOT":^12}|{"CUBE ROOT":^12}|')
    print('+----------+------------+------------+')

    # now the numbers
    for n in range(1,11):
        rt2 = n ** 0.5
        rt3 = n ** (1/3)
        print(f'|{n:^10.2f}|{rt2:^12.5f}|{rt3:^12.5f}|')
        print('+----------+------------+------------+')                       
        
main()
    
