#! /usr/bin/gnuplot

set term pngcairo size 900,900 font "Latin Modern Roman"

set out "regs_era5Land_igeldo_sesgocorr.png"

set multiplot layout 2,1 rowsfirst

#
#Temperatura maxima
#

set title "{/:Bold {/=16 Linear regression of maximum temperature. Igeldo, San Sebastian (1986-2016) \n{/=14 ERA5Land data normalized to actual station level}"

set key at graph 0.38,0.68

set xlabel "{/=14 AEMET observed temperature ({/Symbol \260}C)}"
set ylabel "{/=14 ERA5 LAND temperature ({/Symbol \260}C)}"

set label at graph 0.6,0.35 "{/:Bold r_{Tmax} = 0.96}"
set label at graph 0.1,0.8  "{/:Bold 28.3 ({/Symbol \260}C)}"
set label at graph 0.65,0.1 "{/:Bold 30 ({/Symbol \260}C)}"

set arrow front from 30, graph 0 to 30, graph 1 nohead lw 2


ymax(x)=A+B*x

fit ymax(x) 'Tdata_IGELDO_sesgocorr.dat' u 1:2 via A,B

p 'Tdata_IGELDO_sesgocorr.dat' u 1:2 w p lt 7 ps 1 lc rgb "red" notitle,\
  ymax(x) w l lw 3 t "T_{ERA5} = -2.03 + 1.01T_{OBS} ({/Symbol \260}C)",28.31 lw 2 lc rgb "black" notitle

#
#Temperatura minima
#

set title "{/:Bold {/=16 Linear regression of minimum temperature. Igeldo, San Sebastian (1986-2016) \n{/=14 ERA5Land data normalized to actual station level}"

set key at graph 0.39,0.65 font "Latin Modern Roman"

unset label
set xlabel "{/=14 AEMET observed temperature ({/Symbol \260}C)}"
set ylabel "{/=14 ERA5 LAND temperature ({/Symbol \260}C)}"

set label at graph 0.63,0.34 "{/:Bold r_{Tmin} = 0.96}"
set label at graph 0.13,0.84 "{/:Bold 16.2 ({/Symbol \260}C)}"
set label at graph 0.74,0.1 "{/:Bold 19 ({/Symbol \260}C)}"

set arrow front from 19, graph 0 to 19, graph 1 nohead lw 2

ymin(x)=C+D*x

fit ymin(x) 'Tdata_IGELDO_sesgocorr.dat' u 3:4 via C,D

p 'Tdata_IGELDO_sesgocorr.dat' u 3:4 w p lt 7 ps 1 lc rgb "red" notitle,\
  ymin(x) w l lw 3 t "T_{ERA5} = -2.53 + 0.98T_{OBS} ({/Symbol \260}C)",16.15 lw 2 lc rgb "black" notitle


unset multiplot
