#! /usr/bin/gnuplot

set term pngcairo size 900,900 font "Latin Modern Roman"

set out "regs_era5Land_guenes.png"

set key at graph 0.4,0.7

set multiplot layout 2,1 rowsfirst

#
#Temperatura maxima
#

set title "{/:Bold {/=17 Linear regression of maximum temperature, Gueñes (1986-2016)"

set xlabel "{/=14 AEMET observed temperature ({/Symbol \260}C)}"
set ylabel "{/=14 ERA5 LAND temperature ({/Symbol \260}C)}"

set label at graph 0.65,0.4 "{/:Bold r_{Tmax} = 0.97}"
set label at graph 0.1,0.82 "{/:Bold 31 ({/Symbol \260}C)}"
set label at graph 0.83,0.1 "{/:Bold 35 ({/Symbol \260}C)}"

set arrow front from 35, graph 0 to 35, graph 1 nohead lw 2

ymax(x)=A+B*x

fit ymax(x) 'Tdata_GUENES.dat' u 1:2 via A,B

p 'Tdata_GUENES.dat' u 1:2 w p lt 7 ps 1 lc rgb "red" notitle,\
  ymax(x) w l lw 3 t "T_{ERA5} = 0.78 + 0.86T_{OBS} ({/Symbol \260}C)",31.02 lw 2 lc rgb "black" notitle

#
#Temperatura maxima
#

set title "{/:Bold {/=17 Linear regression of minimum temperature, Gueñes (1986-2016)"

unset label
set xlabel "{/=14 AEMET observed temperature ({/Symbol \260}C)}"
set ylabel "{/=14 ERA5 LAND temperature ({/Symbol \260}C)}"

set label at graph 0.61,0.4 "{/:Bold r_{Tmin} = 0.96}"
set label at graph 0.1,0.82 "{/:Bold 16.7 ({/Symbol \260}C)}"
set label at graph 0.78,0.1 "{/:Bold 17 ({/Symbol \260}C)}"

set arrow front from 17, graph 0 to 17, graph 1 nohead lw 2

ymin(x)=C+D*x

fit ymin(x) 'Tdata_GUENES.dat' u 3:4 via C,D

p 'Tdata_GUENES.dat' u 3:4 w p lt 7 ps 1 lc rgb "red" notitle,\
  ymin(x) w l lw 3 t "T_{ERA5} = 0.79 + 0.94T_{OBS} ({/Symbol \260}C)",16.7 lw 2 lc rgb "black" notitle


unset multiplot
