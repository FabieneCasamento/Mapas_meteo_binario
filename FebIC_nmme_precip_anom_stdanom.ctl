dset ^FebIC_nmme_precip_anom_stdanom.dat
undef 9.999E+20
title prate.bin
options little_endian
xdef 360 linear 0.000000 1.0
ydef 181 linear -90.0 1.0
tdef 6 linear 15Mar2024 1mo
zdef 1 linear 1 1
vars 4
precip 0,1,0   0,1,7,0 ** precip mm/day
clim 0,1,0   0,1,7,0 ** precip mm/day
anom 0,1,0   0,1,7,0 ** precip anom mm/day
stdan 0,1,0   0,1,7,0 ** stdanom
ENDVARS
