clear
close all
clc

load('damping_ratio_free.mat')

sensitivity = 10.47; %millivolts/(m/s^2)
acceleration = voltage_out*1000/sensitivity;

sf = 1/dt;
N = size(acceleration,2);
time = [0:N-1]*dt;
zf = figure(1); clf
za = axes;
zp = plot(time, acceleration);
xlabel('Time (s)')
ylabel('Acceleration (m/s^2)')
grid on
set(za,'xlim',[0 3])
set(za,'fontsize', 14)
set(zp,'linewidth',2)
%print(zf, '-dpng', '-r300')
%---------------------------------------------
freq = [0:N-1]/N*sf ;
ACCELERATION = 2/N*fft(acceleration');
%VOLTAGE_IN = 2/N*fft(voltage_in');
zf = figure(2);clf
za = axes;
zp = semilogx(freq, abs(ACCELERATION));
xlabel('Frequency (Hz)')
ylabel('Acceleration (m/s^2)')
grid
set(za,'xlim',[0 sf/2])
set(za,'fontsize', 14)
set(zp,'linewidth',2)
%print(zf, '-dpng', '-r300')
%---------------------------------------------
[x(1), indx] = max(acceleration);
accel_crop = acceleration(indx:end);
N = size(accel_crop,2);
time_crop = [0:N-1]*dt;
zf = figure(3); clf
za = axes;
zp = plot(time_crop, accel_crop);
xlabel('Time (s)')
ylabel('Acceleration (m/s^2)')
grid on
set(za,'xlim',[0 3])
set(za,'fontsize', 14)
set(zp,'linewidth',2)



%% FIGURE OUT THIS
for nn = 1:50
[val ,indx_min] = min(accel_crop);
accel_crop = accel_crop(indx_min:end);
[x(nn+1), indx_max] = max(accel_crop);
accel_crop = accel_crop(indx_max:end);
end

for nn = 1:length(x)-1
    
zeta(nn) = (1/nn*log(x(1)/x(nn+1))/sqrt(4*pi^2 + (1/nn*log(x(1)/x(nn+1))^2)));    
    
end

zf = figure(4); clf
za = axes;
zp = plot(zeta, 'o');
xlabel('Estimation #')
ylabel('\zeta')
grid on
set(za,'ylim',[0 .04])
set(za,'fontsize', 14)
set(zp,'linewidth',2)
