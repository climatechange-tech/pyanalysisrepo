#! /usr/bin/gnuplot

set term pngcairo size 900,900 font "Latin Modern Roman"

set out "regs_era5Land_bilbo_aero.png"

set key at graph 0.39,0.65

set multiplot layout 2,1 rowsfirst

#
#Temperatura maxima
#

set title "{/:Bold {/=17 Linear regression of maximum temperature. Bilbao Airport (1986-2016)"

set xlabel "{/=14 AEMET observed temperature ({/Symbol \260}C)}"
set ylabel "{/=14 ERA5 LAND temperature ({/Symbol \260}C)}"

set label at graph 0.8,0.4 "{/:Bold r_{Tmax} = 0.96}"
set label at graph 0.1,0.87 "{/:Bold 28.6 ({/Symbol \260}C)}"
set label at graph 0.69,0.1 "{/:Bold 35 ({/Symbol \260}C)}"

set arrow front from 35, graph 0 to 35, graph 1 nohead lw 2

ymax(x)=A+B*x

fit ymax(x) 'Tdata_BILBO_AERO.dat' u 4:11 via A,B

p 'Tdata_BILBO_AERO.dat' u 4:11 w p lt 7 ps 1 lc rgb "red" notitle,\
  ymax(x) w l lw 3 t "T_{ERA5} = 0.35 + 0.81T_{OBS} ({/Symbol \260}C)",28.56 lw 2 lc rgb "black" notitle

#
#Temperatura minima
#

set title "{/:Bold {/=17 Linear regression of minimum temperature. Bilbao Airport (1986-2016)"

unset label
set xlabel "{/=14 AEMET observed temperature ({/Symbol \260}C)}"
set ylabel "{/=14 ERA5 LAND temperature ({/Symbol \260}C)}"

set label at graph 0.8,0.4 "{/:Bold r_{Tmin} = 0.94}"
set label at graph 0.14,0.79 "{/:Bold 16.6 ({/Symbol \260}C)}"
set label at graph 0.68,0.1 "{/:Bold 17 ({/Symbol \260}C)}"

set arrow front from 17, graph 0 to 17, graph 1 nohead lw 2

ymin(x)=C+D*x

fit ymin(x) 'Tdata_BILBO_AERO.dat' u 3:12 via C,D

p 'Tdata_BILBO_AERO.dat' u 3:12 w p lt 7 ps 1 lc rgb "red" notitle,\
  ymin(x) w l lw 3 t "T_{ERA5} = 2.48 + 0.83T_{OBS} ({/Symbol \260}C)",16.63 lw 2 lc rgb "black" notitle


unset multiplot
