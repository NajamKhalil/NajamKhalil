clc; clear all; close all;
ts=0.00001;
t= -0.1:ts:0.1;
m=cos(2*pi*10*t);
c=cos(2*pi*1000*t);
A=1;
g=(A+m).*c;
y=abs(g);
cutoff=500;
[a b]=butter(5,2*cutoff*ts);
z=filter(a,b,y);
figure (1)
subplot(2,1,1)
plot(t,m)
title('Message Signal')
subplot(2,1,2)
plot(t,c)
title(' Carrier Signal')
figure (2)
subplot(3,1,1)
plot(t,g)
title('Modulated Signal')
subplot(3,1,2)
plot(t,y)
title('For demodulation')
subplot(3,1,3)
plot(t,(z-A/2))
title('Recovered Signal')