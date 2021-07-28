clc;clear all;close all;
im= rgb2gray(imread("lina.png"));
%imshow(im);
fileID = fopen('codecopy.txt','w');
[r,c,m]=size(im);
fprintf(fileID,"int row = %d;\n",r);
fprintf(fileID,"int col = %d;\n",c);
fprintf(fileID,"int rowcol[%d][%d];\n",r,c);
for i=1:r 
  for j=1:c 
    fprintf(fileID,"rowcol[%d][%d]=%d;\n",i-1,j-1,im(i,j));
  endfor
endfor
fclose(fileID);
imshow(im);
