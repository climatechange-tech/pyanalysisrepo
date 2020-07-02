#! /usr/bin/gnuplot

set term pngcairo size 900,900 font "Latin Modern Roman"

set out "regs_era5Land_pamplona_aero.png"

set key at graph 0.4,0.74

set multiplot layout 2,1 rowsfirst

#
#Temperatura maxima
#

set title "{/:Bold {/=16.5 Linear regression of maximum temperature. Pamplona Airport (1986-2016)"

set xlabel "{/=14 AEMET observed temperature ({/Symbol \260}C)}"
set ylabel "{/=14 ERA5 LAND temperature ({/Symbol \260}C)}"

set label at graph 0.65,0.4 "{/:Bold r_{Tmax} = 0.98}"
set label at graph 0.1,0.87 "{/:Bold 31.2 ({/Symbol \260}C)}"
set label at graph 0.71,0.1 "{/:Bold 36 ({/Symbol \260}C)}"

set arrow front from 36, graph 0 to 36, graph 1 nohead lw 2

ymax(x)=A+B*x

fit ymax(x) 'Tdata_PAMPLONA_AERO.dat' u 1:2 via A,B

p 'Tdata_PAMPLONA_AERO.dat' u 1:2 w p lt 7 ps 1 lc rgb "red" notitle,\
  ymax(x) w l lw 3 t "T_{ERA5} = -0.66 + 0.88T_{OBS} ({/Symbol \260}C)",31.18 lw 2 lc rgb "black" notitle

#
#Temperatura maxima
#

set title "{/:Bold {/=16.5 Linear regression of minimum temperature. Pamplona Airport (1986-2016)"

unset label
set xlabel "{/=14 AEMET observed temperature ({/Symbol \260}C)}"
set ylabel "{/=14 ERA5 LAND temperature ({/Symbol \260}C)}"

set label at graph 0.65,0.35 "{/:Bold r_{Tmin} = 0.96}"
set label at graph 0.1,0.84 "{/:Bold 16.9 ({/Symbol \260}C)}"
set label at graph 0.73,0.1 "{/:Bold 18 ({/Symbol \260}C)}"

set arrow front from 18, graph 0 to 18, graph 1 nohead lw 2

ymin(x)=C+D*x

fit ymin(x) 'Tdata_PAMPLONA_AERO.dat' u 3:4 via C,D

p 'Tdata_PAMPLONA_AERO.dat' u 3:4 w p lt 7 ps 1 lc rgb "red" notitle,\
  ymin(x) w l lw 3 t "T_{ERA5} = -0.18 + 0.95T_{OBS} ({/Symbol \260}C)",16.91 lw 2 lc rgb "black" notitle


unset multiplot
