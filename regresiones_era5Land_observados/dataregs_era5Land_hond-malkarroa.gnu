#! /usr/bin/gnuplot

set term pngcairo size 900,900 font "Latin Modern Roman"

set out "regs_era5Land_hondarribia.png"

set multiplot layout 2,1 rowsfirst

#
#Temperatura maxima
#

set title "{/:Bold {/=15 Linear regression of maximum temperature. Hondarribia-Malkarroa (1986-2016)"

set key at graph 0.35,0.68

set xlabel "{/=14 AEMET observed temperature ({/Symbol \260}C)}"
set ylabel "{/=14 ERA5 LAND temperature ({/Symbol \260}C)}"

set label at graph 0.72,0.4 "{/:Bold r_{Tmax} = 0.94}"
set label at graph 0.1,0.8 "{/:Bold 27 ({/Symbol \260}C)}"
set label at graph 0.72,0.1 "{/:Bold 30 ({/Symbol \260}C)}"

set arrow front from 30, graph 0 to 30, graph 1 nohead lw 2


ymax(x)=A+B*x

fit ymax(x) 'Tdata_HONDARRIBIA.dat' u 1:2 via A,B

p 'Tdata_HONDARRIBIA.dat' u 1:2 w p lt 7 ps 1 lc rgb "red" notitle,\
  ymax(x) w l lw 3 t "{/=11 T_{ERA5} = -4.36 + 1.05T_{OBS} ({/Symbol \260}C)",27.05 lw 2 lc rgb "black" notitle

#
#Temperatura minima
#

set title "{/:Bold {/=15 Linear regression of minimum temperature. Hondarribia-Malkarroa (1986-2016)"

set key at graph 0.4,0.62

unset label
set xlabel "{/=14 AEMET observed temperature ({/Symbol \260}C)}"
set ylabel "{/=14 ERA5 LAND temperature ({/Symbol \260}C)}"

set label at graph 0.69,0.4 "{/:Bold r_{Tmin} = 0.96}"
set label at graph 0.1,0.8 "{/:Bold 15.68 ({/Symbol \260}C)}"
set label at graph 0.72,0.1 "{/:Bold 19 ({/Symbol \260}C)}"

set arrow front from 19, graph 0 to 19, graph 1 nohead lw 2

ymin(x)=C+D*x

fit ymin(x) 'Tdata_HONDARRIBIA.dat' u 3:4 via C,D

p 'Tdata_HONDARRIBIA.dat' u 3:4 w p lt 7 ps 1 lc rgb "red" notitle,\
  ymin(x) w l lw 3 t "T_{ERA5} = -2.40 + 0.95T_{OBS} ({/Symbol \260}C)",15.68 lw 2 lc rgb "black" notitle


unset multiplot
