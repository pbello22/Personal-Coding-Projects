clear
close all
clc

load('damping_ratio_forced.mat')
sensitivity = 10.47; %millivolts/(m/s^2)
acceleration = voltage_out*1000/sensitivity;

sf = 1/dt;
N = size(acceleration,2);
time = [0:N-1]*dt;
zf = figure(1); clf
za = axes;
zp = plot(time, acceleration(5,:));
xlabel('Time (s)')
ylabel('Acceleration (m/s^2)')
grid on
set(za,'xlim',[0 02])
set(za,'fontsize', 14)
set(zp,'linewidth',2)
print(zf, '-dpng', '-r300')
%---------------------------------------------

freq = [0:N-1]/N*sf ;
ACCELERATION = 2/N*fft(acceleration');

zf = figure(2);clf
za = axes;
zp = semilogx(freq, abs(ACCELERATION(:,5)));
xlabel('Frequency (Hz)')
ylabel('Acceleration (m/s^2)')
grid
set(za,'xlim',[0 sf/2])
set(za,'fontsize', 14)
set(zp,'linewidth',2)
print(zf, '-dpng', '-r300')
%---------------------------------------------
for n = 1:size(voltage_out,1)
    freq_diff = freq - f_exc(n);
    [~,index1] = find(freq_diff>=0);
    [~,index2] = find(freq_diff<=0);
    amp_out(n) = max(abs(ACCELERATION(index1(1),n)), abs(ACCELERATION(index2(end),n)));
    
end

grid on
zf = figure(3);clf
za = axes;
zp = semilogx(f_exc, amp_out, 'o');
xlabel('Frequency (Hz)')
ylabel('Acceleration (m/s^2)')
grid
set(za,'fontsize', 14)
set(zp,'linewidth',2)
%Set up better graph for plot
figsize = [5 3];
set(zf,'papersize',figsize)
set(zf,'paperposition', [0 0 figsize]);
%------------------------------------------------------------
velocity = amp_out./(2*pi*f_exc);

zf = figure(4);clf
za = axes;
zp = semilogx(f_exc, velocity, 'o');
xlabel('Frequency (Hz)')
ylabel('Velocity (m/s)')
grid
set(za,'fontsize', 14)
set(zp,'linewidth',2)
%Set up better graph for plot
figsize = [5 3];
set(zf,'papersize',figsize)
set(zf,'paperposition', [0 0 figsize]);





%% This is the Experimental Data
EXP_f = f_exc(:)'; %frequency vector
EXP_vel = velocity; %vel at each freq
%% Based on the data, make an initial guess at the parameters
% Peak Estimate = 6 m/s
% f n Estimate = 350 Hz
% width at 70% = 20 Hz
init_params = [.2 17 3];
%% Next, set up the anonymous function for sum of squared error
% Note that this function shares the first two inputs as the
% lorentzian and the third input (a) will be the experimentally
% determined velocities. This function then subtracts the
% experimental value from the fit at each frequency, and squares
% the result. We want to minimize this error.
sse = @(p,f,a) sum((lorentzian(p,f)-a).^2);
%% Call the minimization program.
% fminsearch will modify the parameters of the lorentzian until
% the sse is at its minimum value, giving us the best fit.
% Note that the empty sqaure brackets are the options for fminsearch
% (see help fminsearch). The way this code function is called,
% init params will be sent to p of sse, EXP f will go to f of sse
% and EXP vel will go to a of sse.
params=fminsearch(sse,init_params,[],EXP_f,EXP_vel)
%% Now generate the fit
% First, we want to create a frequency vector with more resolution
% for our fit, say 10x higher
df = EXP_f(2)-EXP_f(1);
FIT_f = [EXP_f(1):df/10:EXP_f(end)]';
% Now we'll run the new frequency vector through our lorentzian
% function to generate the curve fit
FIT_vel = lorentzian(params,FIT_f);
%% Plot the Data
plot(EXP_f,EXP_vel,'o',FIT_f,FIT_vel);
grid;
ylabel('velocity (m/s)')
xlabel('frequency (Hz)')
legend('Experimental Data','Fit')


zeta = params(3)/params(2)/2
