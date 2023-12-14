def crcgenerator(data, div):
    
    data_list = list(map(int, list(data)))
    div_list = list(map(int, list(div)))
    data_list.extend([0] * (len(div_list) - 1))

    
    while len(data_list) >= len(div_list):
        
        for i in range(len(div_list)):
            data_list[i] ^= div_list[i]
        
        while data_list and data_list[0] == 0:
            data_list.pop(0)

    while len(data_list) < len(div_list) - 1:
        data_list.insert(0, 0)
    
    crc = ''.join(map(str, data_list))
    return crc



data = input("Enter The Data:")

div = input("Enter The divisor:")
result = crcgenerator(data, div)
print("CRC value for {data} with div {div}:{result}")