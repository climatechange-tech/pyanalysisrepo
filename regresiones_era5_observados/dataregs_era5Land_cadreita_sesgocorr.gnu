#! /usr/bin/gnuplot

set term pngcairo size 900,900 font "Latin Modern Roman"

set out "regs_era5Land_cadreita_sesgocorr.png"

set key at graph 0.4,0.7

set multiplot layout 2,1 rowsfirst

#
#Temperatura maxima
#

set title "{/:Bold {/=17 Linear regression of maximum temperature. Cadreita (1991-2016) \n{/=14 ERA5Land data normalized to actual station level}"

set xlabel "{/=14 AEMET observed temperature ({/Symbol \260}C)}"
set ylabel "{/=14 ERA5 LAND temperature ({/Symbol \260}C)}"

set label at graph 0.7,0.35 "{/:Bold r_{Tmax} = 0.97}"
set label at graph 0.1,0.9 "{/:Bold 32 ({/Symbol \260}C)}"
set label at graph 0.79,0.1 "{/:Bold 36 ({/Symbol \260}C)}"

set arrow front from 36, graph 0 to 36, graph 1 nohead lw 2

ymax(x)=A+B*x

fit ymax(x) 'Tdata_CADREITA_sesgocorr.dat' u 1:2 via A,B

p 'Tdata_CADREITA_sesgocorr.dat' u 1:2 w p lt 7 ps 1 lc rgb "red" notitle,\
  ymax(x) w l lw 3 t "T_{ERA5} = -3.13 + 0.98T_{OBS} ({/Symbol \260}C)",31.98 lw 2 lc rgb "black" notitle

#
#Temperatura maxima
#

set title "{/:Bold {/=17 Linear regression of minimum temperature. Cadreita (1991-2016) \n{/=14 ERA5Land data normalized to actual station level}"

unset label
set xlabel "{/=14 AEMET observed temperature ({/Symbol \260}C)}"
set ylabel "{/=14 ERA5 LAND temperature ({/Symbol \260}C)}"

set label at graph 0.67,0.36 "{/:Bold r_{Tmin} = 0.96}"
set label at graph 0.1,0.81 "{/:Bold 15.3 ({/Symbol \260}C)}"
set label at graph 0.71,0.1 "{/:Bold 18 ({/Symbol \260}C)}"

set arrow front from 18, graph 0 to 18, graph 1 nohead lw 2

ymin(x)=C+D*x

fit ymin(x) 'Tdata_CADREITA_sesgocorr.dat' u 3:4 via C,D

p 'Tdata_CADREITA_sesgocorr.dat' u 3:4 w p lt 7 ps 1 lc rgb "red" notitle,\
  ymin(x) w l lw 3 t "T_{ERA5} = -1.63 + 0.94T_{OBS} ({/Symbol \260}C)",15.25 lw 2 lc rgb "black" notitle


unset multiplot
