% EXPERIMENT 1: Pulse Code Modulation and Demodulation
% 3-bit uniform PCM; no toolboxes needed
clc; clear; close all;
A = 4; fm = 2; fs = 100*fm;
t = 0:1/fs:1;
x = A*sin(2*pi*fm*t);

% Quantize to 8 levels: -3.5, -2.5, ..., +3.5
levels = -3.5:1:3.5;
index = min(8, max(1, ceil(x + 4)));
xq = levels(index);

% 3-bit PCM encoder, then decoder
words = dec2bin(index-1, 3);       % 000 to 111
bits = reshape((words.' - '0'), 1, []);
rx = reshape(bits, 3, []).';
decoded = reshape(levels(rx*[4;2;1] + 1), 1, []);

% Manual uses a sixth-order Butterworth LPF; provide toolbox-free fallback
if exist('butter','file') == 2
    [b,a] = butter(6,4*fm/fs);
    reconstructed = filter(b,a,decoded);
    disp('LPF: sixth-order Butterworth (matches manual)');
else
    alpha = 1-exp(-2*pi*(2*fm)/fs);
    reconstructed = filter(alpha,[1 alpha-1],decoded);
    disp('LPF: simple first-order fallback (no toolbox)');
end

fprintf('Sampling frequency = %d Hz, PCM rate = %d bits/s\n',fs,3*fs);
fprintf('First 12 PCM words:\n'); disp(words(1:12,:));
fprintf('Quantization MSE = %.4f\n', mean((x-xq).^2));

figure('Name','Exp 1 - PCM','Position',[100 100 1000 700]);
subplot(3,2,1); plot(t,x); title('Original message'); grid on;
subplot(3,2,2); stem(t,x,'.'); title('Sampled message'); grid on;
subplot(3,2,3); stairs(t,xq); title('Quantized signal'); grid on;
subplot(3,2,4); stairs(0:59,bits(1:60));
title('PCM bits (first 60)'); ylim([-0.2 1.2]); grid on;
subplot(3,2,5); stairs(t,decoded); title('Decoded signal'); grid on;
subplot(3,2,6); plot(t,x,'k--',t,reconstructed,'b');
title('Reconstructed (LPF)'); legend('Original','Reconstructed'); grid on;
saveas(gcf,'Exp1_PCM_Output.png');
