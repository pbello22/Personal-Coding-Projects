%% flow about a semi-oval shaped body 
clc
clear all
close all

% define spatial domain limits
xmax = 4;
xmin = -xmax;
ymax = xmax;
ymin = xmin;
spatial_step = .1;
[xmesh,ymesh] = meshgrid(xmin:spatial_step:xmax,ymin:spatial_step:ymax);

%% Uniform horizontal flow - strength = 50 m/s
q_uniform = 50; % (m/s)
U = q_uniform*ones(length(xmesh),length(xmesh));
alpha_degree = 0; % degrees
alpha_radiant = alpha_degree*pi/180;
u_unif = U.*cos(alpha_radiant);
v_unif = U.*sin(alpha_radiant);
phi_unif = u_unif.*xmesh+v_unif.*ymesh;
psi_unif = u_unif.*ymesh-v_unif.*xmesh;

zf(1) = figure;
% plot velocity vector in form of arrows
zp(1) = quiver(xmesh,ymesh,u_unif,v_unif);
hold on
% define isolines
isolines = [0:10:100];
% plot streamlines
[C,h] = contour(xmesh,ymesh,psi_unif,isolines,'ShowText','on');
h.LineWidth = 1;
% plot isopotential lines
hold on
[C,h] = contour(xmesh,ymesh,phi_unif,isolines,'ShowText','on');
h.LineWidth = 1;
h.LineStyle = ':';
% title(['V_{\infty} = ',num2str(q_uniform),' m/s'])
xlabel('distance (m)')
ylabel('distance (m)')
set(gca,'fontsize',12)
set(zp(1), 'linewidth',1);
xlim([min(min(xmesh)), max(max(xmesh))])
ylim([min(min(ymesh)), max(max(ymesh))])
axis equal
box on

ss = ['uniform_flow'];
figsize = [5 5];
set(zf(1),'papersize',figsize);
set(zf(1),'paperposition',[0 0 figsize]);
print(zf(1),'-dpng','-r300','-painters',ss)

%% Source flow at (0,0) - strength calculated so that the stagnation point is at (r,theta) = (2m,pi) m 
% define spatial domain limits
r_sp = 10/2/pi; % stagnation point radius "r". the angle is known to be theta = pi
q = 2*pi*q_uniform*r_sp; % source strength (m^2/s)
x0 = 0;
y0 = 0;
circulation = .8*4*pi.*v_unif;

type = 'source';
[u_source,v_source,psi_source,phi_source] = PotentialFlowElement(xmesh,ymesh,x0,y0,q,type);

zf(1) = figure;
% plot velocity vector in form of arrows
zp(1) = quiver(xmesh,ymesh,u_source,v_source);
hold on
% define isolines
isolines =  [-3: 0.5: 1];
% plot streamlines
[C,h] = contour(xmesh,ymesh,psi_source,isolines,'ShowText','on');
h.LineWidth = 1;
% plot isopotential lines
hold on
[C,h] = contour(xmesh,ymesh,phi_source,isolines,'ShowText','on');
h.LineWidth = 1;
h.LineStyle = ':';
% title(['\Lambda = ',num2str(q),' m^2/s'])
xlabel('distance (m)')
ylabel('distance (m)')
set(gca,'fontsize',12)
set(zp(1), 'linewidth',2);
xlim([min(min(xmesh)), max(max(xmesh))])
ylim([min(min(ymesh)), max(max(ymesh))])
axis equal
box on

ss = ['source_flow'];
figsize = [5 5];
set(zf(1),'papersize',figsize);
set(zf(1),'paperposition',[0 0 figsize]);
print(zf(1),'-dpng','-r300','-painters',ss)

%% Superposition uniform + source
u = u_unif + u_source;
v = v_unif + v_source;
phi = phi_unif + phi_source;
psi = psi_unif + psi_source;

zf(1) = figure;
% plot velocity vector in form of arrows
% zp(1) = quiver(xmesh,ymesh,u,v);
hold on
% define isolines
isolines = [-3: 0.5: 1];
% plot streamlines
[C,h] = contour(xmesh,ymesh,psi,isolines,'ShowText','on');
h.LineWidth = 1;
% plot isopotential lines
hold on
[C,h] = contour(xmesh,ymesh,phi,isolines,'ShowText','on');
h.LineWidth = 1;
h.LineStyle = ':';

xlabel('distance (m)')
ylabel('distance (m)')
set(gca,'fontsize',12)
set(zp(1), 'linewidth',2);
xlim([min(min(xmesh)), max(max(xmesh))])
ylim([min(min(ymesh)), max(max(ymesh))])
axis equal
box on

ss = ['semi_infinite_body_flow'];
figsize = [5 5];
set(zf(1),'papersize',figsize);
set(zf(1),'paperposition',[0 0 figsize]);
print(zf(1),'-dpng','-r300','-painters',ss)
