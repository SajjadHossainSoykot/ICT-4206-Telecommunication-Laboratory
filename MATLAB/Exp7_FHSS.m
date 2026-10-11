% EXPERIMENT 7: Frequency Hopping Spread Spectrum (FHSS)
% Fixed hopping pattern keeps plots repeatable in an exam.
clc; clear; close all;
data = [1 0 1 1 0 0 1 0 1 1];
hopIndex = [7 3 5 1 4 6 2 7 2 5];  % picks 1 of 7 frequencies
freq = [1 2 3 4 6 12 24];        % cycles per bit
N = 120; localT = (0:N-1)/N;
t = (0:length(data)*N-1)/N;

polar = kron(2*data-1,ones(1,N));
baseCarrier = repmat(cos(2*pi*localT),1,length(data));
bpsk = polar.*baseCarrier;
hopCarrier = zeros(size(bpsk));
for k = 1:length(data)
    ix = (k-1)*N + (1:N);
    hopCarrier(ix) = cos(2*pi*freq(hopIndex(k))*localT);
end
fhss = bpsk.*hopCarrier;           % mix BPSK with hopping carrier

% Ideal synchronized receiver: multiply by both known carriers
received = zeros(1,length(data));
for k = 1:length(data)
    ix = (k-1)*N + (1:N);
    received(k) = sum(fhss(ix).*hopCarrier(ix).*baseCarrier(ix)) > 0;
end
fprintf('Chosen hop frequencies: '); disp(freq(hopIndex));
fprintf('Sent bits:     '); fprintf('%d',data); fprintf('\n');
fprintf('Received bits: '); fprintf('%d',received); fprintf('\n');

figure('Name','Exp 7 - FHSS','Position',[100 100 1000 750]);
subplot(4,1,1); stairs(t,polar); title('Original polar bits'); ylim([-1.5 1.5]); grid on;
subplot(4,1,2); plot(t,bpsk); title('BPSK signal'); grid on;
subplot(4,1,3); plot(t,hopCarrier); title('Hopping carrier (7 frequencies)'); grid on;
subplot(4,1,4); plot(t,fhss); title('FHSS signal'); grid on;
xlabel('Time (bit periods)');
saveas(gcf,'Exp7_FHSS_Output.png');
