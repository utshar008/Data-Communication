import matplotlib.pyplot as plt

def unipolar_encoding(signal):
    encoded_signal = []
    for bit in signal:
        if bit == '0':
            encoded_signal.extend([0] * 10)  # Represent '0' with 5 zeros
        elif bit == '1':
            encoded_signal.extend([1] * 10)  # Represent '1' with 5 ones
    return encoded_signal

def nrz_l_encoding(data):
    signal = []
    voltage_level = 1# Initial voltage level
    
    for bit in data:
        if bit == '0':
            
            signal.extend([voltage_level] * 10)
            #voltage_level = -voltage_level# High voltage level for '1'
              # Alternate voltage level for consecutive bits
        else:
            signal.extend([-voltage_level] * 10)  # Low voltage level for '0'

    return signal

def nrzi_encoding(data):
    signal = []
    voltage_level = 1  # Initial voltage level
    
    for bit in data:
        if bit == '1':
            # Invert voltage level for '1', maintain for '0'
            voltage_level = -voltage_level
        signal.extend([voltage_level] * 10)  # Represent each bit by 10 consecutive voltage levels

    return signal

def rz_encoding(data):
    
    signal = []
    
    for bit in data:
        if bit == '0':
            signal.extend([-1,0])  # Represent '1' as high for first half and low for second half
        elif bit == '1':
            signal.extend([1,0]) 
            
       # Represent '0' as low for first half and high for second half

    return signal

def manchester_encoding(data):
    signal = []
    
    for bit in data:
        if bit == '0':
            signal.extend([1, -1])  # Represent '1' as high to low transition
        else:
            signal.extend([-1, 1])  # Represent '0' as low to high transition

    return signal
def differential_manchester(data):
    lv=1
    encoded_data = []
    

    for bit in data:
        if bit == '0':
           
            encoded_data.extend([- lv, lv])
             
        else:
            
            encoded_data.extend([lv,-lv])
            lv=-lv

    return encoded_data





data =input("Enter The Signal:") 

unipolar = unipolar_encoding(data)
nrz_l=nrz_l_encoding(data)
nrzi=nrzi_encoding(data)
rz=rz_encoding(data)
man=manchester_encoding(data)
dman=differential_manchester(data)



plt.figure(figsize=(10, 6))
plt.subplot(2,3,1)
plt.step(range(len(unipolar)), unipolar, where='post')
plt.title('Unipolar Encoding')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.ylim(-1.50, 1.5)
plt.xlim(0,100)
plt.yticks([-1,0, 1])
plt.grid(True)
plt.tight_layout()

plt.subplot(2,3,2)
plt.step(range(len(nrz_l)), nrz_l, where='post')
plt.title('NRZ_L')
plt.xlabel('Time')
plt.ylabel('voltage_level')
plt.ylim(-1.5, 1.5)
plt.xlim(0,100)
plt.yticks([-1,0, 1])
plt.grid(True)
plt.tight_layout()

plt.subplot(2,3,3)
plt.step(range(len(nrzi)), nrzi, where='post')
plt.title('NRZ_I')
plt.xlabel('Time')
plt.ylabel('voltage_level')
plt.ylim(-1.5, 1.5) 
plt.xlim(0,100)
plt.yticks([-1,0, 1])
plt.grid(True)
plt.tight_layout()

plt.subplot(2,3,4)
plt.step(range(len(rz)),rz, where='post')
plt.title('RZ')
plt.xlabel('Time')
plt.ylabel('voltage_level')
plt.ylim(-1.5, 1.5)
plt.xlim(0,10)
plt.yticks([-1,0, 1])
plt.grid(True)
plt.tight_layout()

plt.subplot(2,3,5)
plt.step(range(len(man)),man, where='post')
plt.title('Manchester')
plt.xlabel('Time')
plt.ylabel('voltage_level')
plt.ylim(-1.5, 1.5)
plt.xlim(0,15)
plt.yticks([-1,0, 1])
plt.grid(True)
plt.tight_layout()

plt.subplot(2,3,6)
plt.step(range(len(dman)),dman, where='post')
plt.title('Differential Manchester')
plt.xlabel('Time')
plt.ylabel('voltage_level')

plt.ylim(-1.5, 1.5) 
plt.xlim(0,15)
plt.yticks([-1,0, 1])
plt.grid(True)
plt.tight_layout()




plt.show()

