def prefix2mask(prefix):
    out = [0, 0, 0, 0]
    i = 0
    while prefix >= 8:
        out[i] = 255
        prefix -= 8
        i += 1
    for j in range(7, 8-prefix-1, -1):
        out[i] += 2**j
    return out

def broadcast(address, prefix):
    out = address.copy()
    ones = 32-prefix
    for i in range(ones):
        j = 3 - i//8
        out[j]+=2**(i-8*(i//8))
    return out

def first(address, prefix):
    out = address.copy()
    out[3] += 1
    return out

def last(address, prefix):
    out = broadcast(address, prefix)
    out[3] -= 1
    return out

def next_address(address, prefix):
    to_add = 2**(32-prefix)
    address[3]+=to_add
    while address[3] > 255:
        address[3] -= 256
        address[2] += 1
    while address[2] > 255:
        address[2] -= 256
        address[1] += 1
    while address[1] > 255:
        address[1] -= 256
        address[0] += 1


def to_ipv4(address):
    out = ""
    for i, octet in enumerate(address):
        out+=str(octet)
        if i < len(address)-1:
            out+='.'
    return out
    


def main():
    base = input("Base network: ")
    base, mask = base.split("/")
    base = base.split(".")
    print(base, mask)
    subnets_q = int(input("Number of subnets: "))

    subnet_data = []
    for i in range(subnets_q):
        data = int(input("subnet # {} num of hosts: ".format(i)))
        size = 2
        while size-2 < data:
            size *= 2
        subnet_data.append((data, size-2))

    print()
    current_address = [int(x) for x in base]
    current_mask = int(mask)
    for i in range(len(subnet_data)):
        while(True):
            if(2**(32-current_mask)-2 >= subnet_data[i][1] and 2**(32-current_mask-1)-2 < subnet_data[i][1]):
                break
            current_mask += 1
        
        broadcast_address = broadcast(current_address, current_mask)
        first_usable = first(current_address, current_mask)
        last_usable = last(current_address, current_mask)
        print("subnet {}: ".format(i), to_ipv4(current_address))
        print("mask:", to_ipv4(prefix2mask(current_mask)), current_mask)
        print("broadcast:", to_ipv4(broadcast_address))
        print("size:", subnet_data[i][1])
        print("first usable:", to_ipv4(first_usable))
        print("last usable:", to_ipv4(last_usable))
        print()

        next_address(current_address, current_mask)


if __name__ == "__main__":
    main()
    # print(broadcast([255,0,0,0], 27))
    # print(first([255,0,0,0], 27))
    # print(last([255,0,0,0], 27))
    # for i in range(32):
    #     print(i, prefix2mask(i))