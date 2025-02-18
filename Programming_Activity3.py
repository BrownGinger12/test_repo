n = int(input("input subnet mask: "))

bits = 32 - n

total_ip_address = 1

while bits > 0:
    if bits < 8:
        bin = 2 ** bits
        total_ip_address = total_ip_address * bin
        break
    else:
        total_ip_address = total_ip_address * 256
        bits -= 8

print("total ip address: ", total_ip_address)