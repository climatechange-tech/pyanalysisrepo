#! /usr/bin/gnuplot

set term pngcairo size 900,900 font "Latin Modern Roman"

set out "regs_era5Land_lekeitio_sesgocorr_zg0_era5.png"

set key at graph 0.36,0.67

set multiplot layout 2,1 rowsfirst

#
#Temperatura maxima
#

set title "{/:Bold {/=17 Linear regression of maximum temperature. Lekeitio (1997-2016) \n{/=14 Normalized to mean sea level by ERA5 geopotential}"

set xlabel "{/=14 AEMET observed temperature ({/Symbol \260}C)}"
set ylabel "{/=14 ERA5 LAND temperature ({/Symbol \260}C)}"

set label at graph 0.6,0.32 "{/:Bold r_{Tmax} = 0.93}"
set label at graph 0.1,0.78 "{/:Bold 27.6 ({/Symbol \260}C)}"
set label at graph 0.67,0.1 "{/:Bold 30 ({/Symbol \260}C)}"

set arrow front from 30, graph 0 to 30, graph 1 nohead lw 2

ymax(x)=A+B*x

fit ymax(x) 'Tdata_LEKEITIO_sesgocorr_zg0_era5.dat' u 1:2 via A,B

p 'Tdata_LEKEITIO_sesgocorr_zg0_era5.dat' u 1:2 w p lt 7 ps 1 lc rgb "red" notitle,\
  ymax(x) w l lw 3 t "T_{ERA5} = -4.47 + 1.07T_{OBS} ({/Symbol \260}C)",27.55 lw 2 lc rgb "black" notitle

#
#Temperatura minima
#

set title "{/:Bold {/=17 Linear regression of minimum temperature. Lekeitio (1997-2016) \n{/=14 Normalized to mean sea level by ERA5 geopotential}"

unset label
set xlabel "{/=14 AEMET observed temperature ({/Symbol \260}C)}"
set ylabel "{/=14 ERA5 LAND temperature ({/Symbol \260}C)}"

set label at graph 0.53,0.26 "{/:Bold r_{Tmin} = 0.96}"
set label at graph 0.1,0.78 "{/:Bold 15.1 ({/Symbol \260}C)}"
set label at graph 0.71,0.1 "{/:Bold 19 ({/Symbol \260}C)}"

set arrow front from 19, graph 0 to 19, graph 1 nohead lw 2

ymin(x)=C+D*x

fit ymin(x) 'Tdata_LEKEITIO_sesgocorr_zg0_era5.dat' u 3:4 via C,D

p 'Tdata_LEKEITIO_sesgocorr_zg0_era5.dat' u 3:4 w p lt 7 ps 1 lc rgb "red" notitle,\
  ymin(x) w l lw 3 t "T_{ERA5} = -4.05 + 1.01T_{OBS} ({/Symbol \260}C)",15.06 lw 2 lc rgb "black" notitle


unset multiplot
