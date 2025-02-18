ip_address = input("input ip address and subnet: ")
val = ip_address.split("/")
n = int(val[1])
list = val[0].split(".")
bits = 32 - n
total_ip_address = 1

def and_mask(octet, mask):
    octet_to_mask = ""
    if len(octet) < 8:
        for i in range(8 - len(octet)):
            octet_to_mask += "0"
        octet_to_mask += octet
    else:
        octet_to_mask = octet
    masked_octet = ""
    for i in range(8):
        if i < mask:
            masked_octet += octet_to_mask[i]
        else:
            masked_octet += "0"
    return masked_octet

octet = []
octet_index = 0
broadcast_octet = []

while n > 0:
    binary = bin(int(list[octet_index]))
    if n < 8:
        octet.append(int(and_mask(binary[2:], n), 2))
        broadcast_octet.append(int(and_mask(binary[2:], n), 2))
        octet_index += 1
        break
    else:
        octet.append(int(and_mask(binary[2:], n), 2))
        broadcast_octet.append(int(and_mask(binary[2:], n), 2))
        n -= 8
        octet_index += 1

if len(octet) < 4:
    for i in range(4 - len(octet)):
        octet.append(0)
        broadcast_octet.append(0)

broadcast_index = 3

while bits > 0:
    if bits < 8:
        mul = 2 ** bits
        broadcast_octet[broadcast_index] += mul-1
        total_ip_address = total_ip_address * mul
        break
    else:
        broadcast_octet[broadcast_index] += 255
        broadcast_index -= 1
        total_ip_address = total_ip_address * 256
        bits -= 8

print("total ip address: ", total_ip_address)
print("usable host: ", total_ip_address-2)
print("usable range: ", octet[0], ".",octet[1], ".",octet[2], ".",octet[3]+1, " - ", broadcast_octet[0], ".",broadcast_octet[1], ".",broadcast_octet[2], ".",broadcast_octet[3]-1)
print("network address: ", octet[0], ".",octet[1], ".",octet[2], ".",octet[3])
print("broadcast address: ", broadcast_octet[0], ".",broadcast_octet[1], ".",broadcast_octet[2], ".",broadcast_octet[3])




