"""
This script plots magnitude and phase of a transfer function based on numerator and denominator coefficients 

Inputs:
Format of function needed: 1/(jw/wc + 1)
Numerators/Denominators: Entered  with square brackets such as [1/4000*pi, 1]
Range1, Range2: Entered as raw int
"""
from pylab import *
import pylab
from scipy import signal
import math

print("Enter transfer function in the form 1/(jw/wc + 1)")
numerators = eval(input("Enter numerators of trasnfer function in square brackets "))
denominators = eval(input("Enter denominators of transfer function in square brackets "))
range1 = math.log10(int(input("Enter frequency range as f1 ")))
range2 =  math.log10(int(input("Enter frequency range as f2 ")))

system =  signal.lti(numerators, denominators)
f = logspace(range1, range2) #10^1 to 10^5
w=2 * pi * f

w, mag, phase = signal.bode(system, w)
plt.figure(0)
title('Magnitude Bode plot of function')
xlabel('Frequency (hz)')
ylabel('Magnitude (dB)')
semilogx(f,mag)

plt.figure(1)
title('Phase Bode plot of function')
xlabel('Frequency (hz)')
ylabel('Magnitude (dB)')
semilogx(f, phase)
pylab.show()