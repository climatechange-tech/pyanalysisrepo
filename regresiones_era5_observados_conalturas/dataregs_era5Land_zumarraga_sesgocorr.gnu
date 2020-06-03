#! /usr/bin/gnuplot

set term pngcairo size 900,900 font "Latin Modern Roman"

set out "regs_era5Land_zumarraga_sesgocorr.png"

set multiplot layout 2,1 rowsfirst

#
#Temperatura maxima
#

set title "{/:Bold {/=16 Linear regression of maximum temperature. Zumarraga (2007-2016) \n{/=14 ERA5Land data normalized to actual station level}"

set key at graph 0.4,0.62

set xlabel "{/=14 AEMET observed temperature ({/Symbol \260}C)}"
set ylabel "{/=14 ERA5 LAND temperature ({/Symbol \260}C)}"

set label at graph 0.6,0.35 "{/:Bold r_{Tmax} = 0.98}"
set label at graph 0.1,0.83 "{/:Bold 30.2 ({/Symbol \260}C)}"
set label at graph 0.8,0.1 "{/:Bold 35 ({/Symbol \260}C)}"

set arrow front from 35, graph 0 to 35, graph 1 nohead lw 2


ymax(x)=A+B*x

fit ymax(x) 'Tdata_ZUMARRAGA_sesgocorr.dat' u 1:2 via A,B

p 'Tdata_ZUMARRAGA_sesgocorr.dat' u 1:2 w p lt 7 ps 1 lc rgb "red" notitle,\
  ymax(x) w l lw 3 t "T_{ERA5} = -1.99 + 0.92T_{OBS} ({/Symbol \260}C)",30.15 lw 2 lc rgb "black" notitle

#
#Temperatura minima
#

set title "{/:Bold {/=16 Linear regression of minimum temperature. Zumarraga (2007-2016) \n{/=14 ERA5Land data normalized to actual station level}"

set key at graph 0.37,0.62

unset label
set xlabel "{/=14 AEMET observed temperature ({/Symbol \260}C)}"
set ylabel "{/=14 ERA5 LAND temperature ({/Symbol \260}C)}"

set label at graph 0.55,0.3 "{/:Bold r_{Tmin} = 0.96}"
set label at graph 0.1,0.79 "{/:Bold 15 ({/Symbol \260}C)}"
set label at graph 0.68,0.1 "{/:Bold 17 ({/Symbol \260}C)}"

set arrow front from 17, graph 0 to 17, graph 1 nohead lw 2

ymin(x)=C+D*x

fit ymin(x) 'Tdata_ZUMARRAGA_sesgocorr.dat' u 3:4 via C,D

p 'Tdata_ZUMARRAGA_sesgocorr.dat' u 3:4 w p lt 7 ps 1 lc rgb "red" notitle,\
  ymin(x) w l lw 3 t "T_{ERA5} = -2.36 + 0.99T_{OBS} ({/Symbol \260}C)",14.99 lw 2 lc rgb "black" notitle


unset multiplot
