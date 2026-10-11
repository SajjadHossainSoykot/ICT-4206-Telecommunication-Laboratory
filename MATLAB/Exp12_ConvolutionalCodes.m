% EXPERIMENT 12: (2,1,2) Convolutional Encoder
% Generator bits: g1=111, g2=101 (rate 1/2, memory 2)
clc; clear; close all;
m = [1 0 1 1];
inputBits = [m 0 0];              % flush two memory elements
d1 = 0; d2 = 0;
code = zeros(length(inputBits),2);

for k = 1:length(inputBits)
    bit = inputBits(k);
    code(k,1) = xor(xor(bit,d1),d2);
    code(k,2) = xor(bit,d2);
    d2 = d1; d1 = bit;
end
serial = reshape(code.',1,[]);
disp('Input (with tail bits):'); disp(inputBits);
disp('Encoded pairs (one pair per row):'); disp(code);
fprintf('Encoded stream: '); fprintf('%d',serial); fprintf('\n');

figure('Name','Exp 12 - Convolutional Code');
subplot(2,1,1); stairs(0:length(m),[m m(end)]);
title('Original message'); ylim([-0.2 1.2]); grid on;
subplot(2,1,2); stairs(0:length(serial),[serial serial(end)]);
title('Convolutionally encoded stream'); ylim([-0.2 1.2]); grid on;
xlabel('Bit number');
saveas(gcf,'Exp12_ConvolutionalCodes_Output.png');
