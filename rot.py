def rotl(num, bits):
    bit = num & (1 << (bits-1))
    num <<= 1
    if(bit):
        num |= 1
    num &= (2**bits-1)

    return num

def rotr(num, bits):
    num &= (2**bits-1)
    bit = num & 1
    num >>= 1
    if(bit):
        num |= (1 << (bits-1))

    return num


print rotl(255,8);
print rotr(255,8);
numr=1;
numl=1;
for i in range(0,10):
    print "0x%02X (%d)" % (numr,numr)
    print "0x%02X (%d)" % (numl,numl)
    numr = rotr(numr,8) 
    numl = rotl(numl,8)
