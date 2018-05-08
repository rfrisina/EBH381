#!/usr/bin/env python
# -*- coding: ASCII -*-

import string
from sys import argv
import gzip

filein=argv[1]#'HG00096.sort.RG.Mkdup.vcf.gz'#argv[1]
fileout=argv[2]#'test.vcf.gz'

fileout=gzip.open(fileout,'w')

file=gzip.open(filein,'r')

count=0

x=file.readline()

while x<>'':
    if x[0]=='#':
        fileout.write(x)
    else:
        y=string.split(x[:-1])
        out=string.join(y[:7],'\t')+'\t.'
        format_st=string.split(y[8],':')
        try:
            GT=format_st.index('GT')
        except:
            GT=-9

        if GT>=0:
            out=out+'\tGT\t'+string.split(y[9],':')[GT]+'\n'
            fileout.write(out)
            count+=1
            if count%10000==0:
                print string.join(y[:2],'\t')
            
    x=file.readline()
