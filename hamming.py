def detectposition(data):
    c1 = data[6] ^ data[4] ^ data[2] ^ data[0]
    c2 = data[5] ^ data[4] ^ data[1] ^ data[0]
    c3 = data[3] ^ data[2] ^ data[1] ^ data[0]

    c = c3 * 4 + c2 * 2 + c1
    if c == 0:
        print("There is no error")
    else:
        print("Error detected at position:", c)
        print("Error bit  is:", data[7 - c], "\nChange to:", 1 if data[c - 1] == '0' else 0)
a = input("Enter 7 bit  data: ")
raw_data = [int(i) for i in a]
detectposition(raw_data)