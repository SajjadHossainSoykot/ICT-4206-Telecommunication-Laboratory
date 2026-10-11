% EXPERIMENT 6: Direct Sequence Spread Spectrum (DSSS)
clc; clear; close all;
data = [1 0 1];                 % same message as lab manual
pn = [0 0 1 0 1 1 1];           % 7-chip PN sequence
L = length(pn); samples = 40;
pnPolar = 2*pn - 1;            % 0 -> -1, 1 -> +1

spread = [];
for k = 1:length(data)
    spread = [spread (2*data(k)-1)*pnPolar];
end
baseband = kron(spread,ones(1,samples));
t = (0:length(baseband)-1)/(L*samples);
carrier = cos(2*pi*10*t);
tx = baseband.*carrier;         % DSSS + BPSK

% Ideal synchronized receiver: despreading and correlation
pnSamples = kron(repmat(pnPolar,1,length(data)),ones(1,samples));
received = zeros(1,length(data));
for k = 1:length(data)
    ix = (k-1)*L*samples + (1:L*samples);
    received(k) = sum(tx(ix).*carrier(ix).*pnSamples(ix)) > 0;
end
fprintf('Sent bits:     '); fprintf('%d',data); fprintf('\n');
fprintf('Received bits: '); fprintf('%d',received); fprintf('\n');
fprintf('Processing gain = %d (%.2f dB)\n',L,10*log10(L));

figure('Name','Exp 6 - DSSS','Position',[100 100 1000 650]);
subplot(3,1,1); stairs(t,baseband); title('Baseband DSSS'); ylim([-1.5 1.5]); grid on;
subplot(3,1,2); plot(t,carrier); title('Carrier'); grid on;
subplot(3,1,3); plot(t,tx); title('DSSS-BPSK signal'); grid on;
xlabel('Time (bit periods)');
saveas(gcf,'Exp6_DSSS_Output.png');
