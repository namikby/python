# Sound Signal Processing

import matplotlib.pyplot as plt
import sounddevice as sd
from scipy.fftpack import fft
import numpy as np
from scipy import signal

i=1
j=0

while i==1:
    plt.close('all')
    
    # enter input characteristics
    print('Input characteristics:')
    try:
        Fs=int(input('Sampling frequency(Hz):'))
    except ValueError:
        print('Input error!')
            
    try:
        t=int(input('Length in time(sec):'))
    except ValueError:
        print('Input error!')
            
    # output for start of recording
    print('Recording!')
    
    # sound input commands
    snd=sd.rec(int(t*Fs),Fs,1,blocking='True')
    
    # sound to 1D matrix
    snd=snd.flatten()
    
    # sound replay
    sd.play(snd,Fs)
    
    # sound plot
    plt.figure(1)
    plt.plot(snd); plt.title('Recorded sound')
    
    # Spectre analysis of sound
    Xf=fft(snd)
    n=np.size(snd)
    f=(Fs/2)*np.linspace(0,1,round(n/2))
    Xm=(2/n)*abs(Xf[0:np.size(f)])
    
    # Plot of spectre analysis
    plt.figure(2)
    plt.plot(f,Xm); plt.xlabel('Frequency(Hz)');
    plt.ylabel('Amplitude'); plt.title('Sound spectre');
    
    # Filter design
    try:
        j=int(input('Filter type? 1-lowpass 2-highpass:'))
    except ValueError:
        print('Input error!')
    
    if j==1:
        print('Design of lowpass filter')
        try:
            Wn=float(input('Nyquist frequency percentage(0.00-1.00):'))
        except ValueError:
            print('Input error!')
            
        try:
            N=int(input('Filter order:'))
        except ValueError:
            print('Input error!')
            
        # Design Butterworth filter using coefficient and function filtfilt
        b,a=signal.butter(N,Wn,'lowpass')
        filtsnd=signal.filtfilt(b,a,snd)
        
        # Reproduction of filtered sound
        sd.play(filtsnd,Fs)
        
        # Plot of filtered sound
        plt.figure(3)
        plt.plot(filtsnd); plt.title('Filtered sound')
        
        # Spectre analysis of filtered sound
        Xf1=fft(filtsnd)
        n1=np.size(filtsnd)
        f1=(Fs/2)*np.linspace(0,1,round(n1/2))
        Xm1=(2/n1)*abs(Xf1[0:np.size(f1)])
        
        # Plot of spectre analysis of filtered sound
        plt.figure(4)
        plt.plot(f1,Xm1); plt.xlabel('Frequency(Hz)');
        plt.ylabel('Amplitude'); plt.title('Spectre of filtered sound');
    
    elif j==2:
        print('Design of highpass filter')
        try:
            Wn=float(input('Nyquist frequency percentage(0.00-1.00):'))
        except ValueError:
            print('Input error!')
            
        try:
            N=int(input('Filter order:'))
        except ValueError:
            print('Input error!')    
            
        # Design Butterworth filter using coefficient and function filtfilt
        b,a=signal.butter(N,Wn,'highpass')
        filtsnd=signal.filtfilt(b,a,snd)
        
        # Reproduction of filtered sound
        sd.play(filtsnd,Fs)
        
        # Plot of filtered sound
        plt.figure(3)
        plt.plot(filtsnd); plt.title('Filtered sound')
        
        # Spectre analysis of filtered sound
        Xf1=fft(filtsnd)
        n1=np.size(filtsnd)
        f1=(Fs/2)*np.linspace(0,1,round(n1/2))
        Xm1=(2/n1)*abs(Xf1[0:np.size(f1)])
        
        # Plot of spectre analysis of filtered sound
        plt.figure(4)
        plt.plot(f1,Xm1); plt.xlabel('Frequency(Hz)');
        plt.ylabel('Amplitude'); plt.title('Spectre of filtered sound');
        
    else:
        print('Input error!')
    
    # Repeat loop
    try:
        i=int(input('Repeat? 1-Yes 2-No :'))
    except ValueError:
        print('Input error!')