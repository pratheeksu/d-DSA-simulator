import math

c = 3*10**8 #speed of light in meters
pi = 3.14
alpha = 2.8
rec_power = 3.16 * 10**(-13) # -75 dBm
        #TV, LTE, ISM, CBRS
trans_power = [4, 4, 1, 10]
freq = [600, 900, 2400, 3500]

d = [0 for i in range(4)]
for i in range(4):
    num = math.pow((trans_power[i]/rec_power), 1/alpha) * c
    den = 4 * pi * freq[i] * (10**6)
    d[i] = num/den
    print(freq[i], " ", d[i])
