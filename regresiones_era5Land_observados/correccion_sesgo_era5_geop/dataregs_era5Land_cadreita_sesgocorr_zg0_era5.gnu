#! /usr/bin/gnuplot

set term pngcairo size 900,900 font "Latin Modern Roman"

set out "regs_era5Land_foronda_sesgocorr_zg0_era5.png"

set key at graph 0.37,0.67

set multiplot layout 2,1 rowsfirst

#
#Temperatura maxima
#

set title "{/:Bold {/=17 Linear regression of maximum temperature. Foronda-Txokiza (1986-2016) \n{/=14 Normalized to mean sea level by ERA5 geopotential}"

set xlabel "{/=14 AEMET observed temperature ({/Symbol \260}C)}"
set ylabel "{/=14 ERA5 LAND temperature ({/Symbol \260}C)}"

set label at graph 0.62,0.4 "{/:Bold r_{Tmax} = 0.98}"
set label at graph 0.1,0.82 "{/:Bold 28.2 ({/Symbol \260}C)}"
set label at graph 0.68,0.1 "{/:Bold 35 ({/Symbol \260}C)}"

set arrow front from 35, graph 0 to 35, graph 1 nohead lw 2

ymax(x)=A+B*x

fit ymax(x) 'Tdata_FORONDA_sesgocorr_zg0_era5.dat' u 1:2 via A,B

p 'Tdata_FORONDA_sesgocorr_zg0_era5.dat' u 1:2 w p lt 7 ps 1 lc rgb "red" notitle,\
  ymax(x) w l lw 3 t "T_{ERA5} = -2.83 + 0.89T_{OBS} ({/Symbol \260}C)",28.24 lw 2 lc rgb "black" notitle

#
#Temperatura maxima
#

set title "{/:Bold {/=17 Linear regression of minimum temperature. Foronda-Txokiza (1986-2016) \n{/=14 Normalized to mean sea level by ERA5 geopotential}"

unset label
set xlabel "{/=14 AEMET observed temperature ({/Symbol \260}C)}"
set ylabel "{/=14 ERA5 LAND temperature ({/Symbol \260}C)}"

set label at graph 0.64,0.4 "{/:Bold r_{Tmin} = 0.93}"
set label at graph 0.1,0.8 "{/:Bold 13.8 ({/Symbol \260}C)}"
set label at graph 0.65,0.1 "{/:Bold 17 ({/Symbol \260}C)}"

set arrow front from 17, graph 0 to 17, graph 1 nohead lw 2

ymin(x)=C+D*x

fit ymin(x) 'Tdata_FORONDA_sesgocorr_zg0_era5.dat' u 3:4 via C,D

p 'Tdata_FORONDA_sesgocorr_zg0_era5.dat' u 3:4 w p lt 7 ps 1 lc rgb "red" notitle,\
  ymin(x) w l lw 3 t "T_{ERA5} = -2.20 + 0.94T_{OBS} ({/Symbol \260}C)",13.84 lw 2 lc rgb "black" notitle


unset multiplot
