def dec2bin(decimal):
    if type(decimal) is int:
        nth_power_of_two = []
        i=0
        z=1
        bin = ""
        while z<=decimal:
            nth_power_of_two.append(z)
            i+=1
            z = 2**i
        for i in range(len(nth_power_of_two)-1,-1,-1):
            if decimal>=nth_power_of_two[i]:
                bin+="1"
                decimal-=nth_power_of_two[i]
            else:
                bin+="0"
        return bin
    else:
        return "Wrong type of input"
def bin2dec(binary):
    if type(binary) is str:
        decimal = 0
        for i in range(len(binary)):
            if binary[i]!="0" and binary[i]!="1":
                print(binary[i])
                return "Wrong input"
            else:
                if binary[i]=="1":
                    z = 2**(len(binary)-i-1)
                    decimal+=z
        return decimal
    else:
        return "Wrong type of input"
print(bin2dec("100000"))
#print(dec2bin(678))
