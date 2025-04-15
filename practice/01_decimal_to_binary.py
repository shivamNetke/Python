def dec_to_binary():
    dec_num = int(input("Enter decimal number value: "))
    original_dec = dec_num
    pow_10 = 1
    ans = 0

    while dec_num > 0:
        rem = dec_num % 2
        dec_num = dec_num // 2

        ans = ans + (pow_10 * rem)
        pow_10 = pow_10 * 10

    print(f"Binary value of {original_dec} is: {ans}")
    
dec_to_binary()



