import matplotlib.pyplot as plt
import numpy as np

carrierf = int( input("Enter The Carrier frequency:"))
carrieramp = int( input("Enter The Carrier amplitude:"))

modf = int(input("Enter The Modulating frequency:"))  
modamp =float(input("Enter The Modulating amplitude:")) 

samplef = int(input("Enter The Sampling frequency:") ) 
time = np.arange(0, 4, 1/ samplef)  


Csignal = carrieramp * np.sin(2 * np.pi * carrierf * time)


Msignal = modamp * np.sin(2 * np.pi * modf * time)


am= (1 + Msignal) * Csignal
fm=np.sin(2 * np.pi * (carrierf + Msignal) * time)
pm=np.sin(2 * np.pi * carrierf * time + np.pi * Msignal)




plt.figure(figsize=(10, 6))

plt.subplot(3,3,1)
plt.plot(time, Csignal, label='Carrier Signal')
plt.title('Carrier Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.legend()

plt.subplot(3,3,2)
plt.plot(time, Msignal, label='Modulating Signal')
plt.title('Modulating Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.legend()

plt.subplot(3,3,3)
plt.plot(time, am, label='AM Signal', color='red')
plt.title('Amplitude Modulated Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.legend()

plt.tight_layout()
plt.subplot(3,3,4)
plt.plot(time, Csignal, label='Carrier Signal')
plt.title('Carrier Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.legend()

plt.subplot(3,3,5)
plt.plot(time, Msignal, label='Modulating Signal')
plt.title('Modulating Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.legend()



plt.subplot(3, 3, 6)
plt.plot(time, fm, color='green')
plt.title('Frequency Modulated Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.legend()

plt.subplot(3,3,7)
plt.plot(time, Csignal, label='Carrier Signal')
plt.title('Carrier Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.legend()

plt.subplot(3,3,8)
plt.plot(time, Msignal, label='Modulating Signal')
plt.title('Modulating Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.legend()


plt.tight_layout()
plt.subplot(3, 3, 9)
plt.plot(time, pm, color='grey')
plt.title('Phase Modulated Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.legend()

plt.tight_layout()
plt.show()
