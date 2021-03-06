#! /usr/bin/gnuplot

set term pngcairo size 900,900 font "Latin Modern Roman"

set out "regs_era5Land_igeldo_sesgocorr_zg0_era5.png"

set multiplot layout 2,1 rowsfirst

#
#Temperatura maxima
#

set title "{/:Bold {/=16 Linear regression of maximum temperature. Igeldo, San Sebastian (1986-2016) \n{/=14 Normalized to mean sea level by ERA5 geopotential}"

set key at graph 0.38,0.68

set xlabel "{/=14 AEMET observed temperature ({/Symbol \260}C)}"
set ylabel "{/=14 ERA5 LAND temperature ({/Symbol \260}C)}"

set label at graph 0.52,0.35 "{/:Bold r_{Tmax} = 0.96}"
set label at graph 0.1,0.8 "{/:Bold 27.1 ({/Symbol \260}C)}"
set label at graph 0.67,0.1 "{/:Bold 30 ({/Symbol \260}C)}"

set arrow front from 30, graph 0 to 30, graph 1 nohead lw 2


ymax(x)=A+B*x

fit ymax(x) 'Tdata_IGELDO_sesgocorr_zg0_era5.dat' u 1:2 via A,B

p 'Tdata_IGELDO_sesgocorr_zg0_era5.dat' u 1:2 w p lt 7 ps 1 lc rgb "red" notitle,\
  ymax(x) w l lw 3 t "T_{ERA5} = -3.20 + 1.01T_{OBS} ({/Symbol \260}C)",27.14 lw 2 lc rgb "black" notitle

#
#Temperatura minima
#

set title "{/:Bold {/=16 Linear regression of minimum temperature. Igeldo, San Sebastian (1986-2016) \n{/=14 Normalized to mean sea level by ERA5 geopotential}"

set key at graph 0.37,0.65

unset label
set xlabel "{/=14 AEMET observed temperature ({/Symbol \260}C)}"
set ylabel "{/=14 ERA5 LAND temperature ({/Symbol \260}C)}"

set label at graph 0.53,0.25 "{/:Bold r_{Tmin} = 0.96}"
set label at graph 0.1,0.77 "{/:Bold 15 ({/Symbol \260}C)}"
set label at graph 0.71,0.1 "{/:Bold 19 ({/Symbol \260}C)}"

set arrow front from 19, graph 0 to 19, graph 1 nohead lw 2

ymin(x)=C+D*x

fit ymin(x) 'Tdata_IGELDO_sesgocorr_zg0_era5.dat' u 3:4 via C,D

p 'Tdata_IGELDO_sesgocorr_zg0_era5.dat' u 3:4 w p lt 7 ps 1 lc rgb "red" notitle,\
  ymin(x) w l lw 3 t "T_{ERA5} = -3.64 + 0.98T_{OBS} ({/Symbol \260}C)",15.04 lw 2 lc rgb "black" notitle


unset multiplot
