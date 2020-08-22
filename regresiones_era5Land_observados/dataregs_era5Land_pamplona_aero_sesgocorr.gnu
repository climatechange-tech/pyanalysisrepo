#! /usr/bin/gnuplot

set term pngcairo size 900,900 font "Latin Modern Roman"

set out "regs_era5Land_pamplona_aero_sesgocorr.png"

set key at graph 0.4,0.76

set multiplot layout 2,1 rowsfirst

#
#Temperatura maxima
#

set title "{/:Bold {/=17 Linear regression of maximum temperature. Pamplona Airport (1986-2016) \n{/=14 ERA5Land data normalized to actual station level}"

set xlabel "{/=14 AEMET observed temperature ({/Symbol \260}C)}"
set ylabel "{/=14 ERA5 LAND temperature ({/Symbol \260}C)}"

set label at graph 0.65,0.4 "{/:Bold r_{Tmax} = 0.98}"
set label at graph 0.1,0.87 "{/:Bold 31.8 ({/Symbol \260}C)}"
set label at graph 0.72,0.1 "{/:Bold 36 ({/Symbol \260}C)}"

set arrow front from 36, graph 0 to 36, graph 1 nohead lw 2

ymax(x)=A+B*x

fit ymax(x) 'Tdata_PAMPLONA_AERO_sesgocorr.dat' u 1:2 via A,B

p 'Tdata_PAMPLONA_AERO_sesgocorr.dat' u 1:2 w p lt 7 ps 1 lc rgb "red" notitle,\
  ymax(x) w l lw 3 t "T_{ERA5} = -0.03 + 0.88T_{OBS} ({/Symbol \260}C)",31.82 lw 2 lc rgb "black" notitle

#
#Temperatura maxima
#

set title "{/:Bold {/=17 Linear regression of minimum temperature. Pamplona Airport (1986-2016) \n{/=14 ERA5Land data normalized to actual station level}"

unset label
set xlabel "{/=14 AEMET observed temperature ({/Symbol \260}C)}"
set ylabel "{/=14 ERA5 LAND temperature ({/Symbol \260}C)}"

set label at graph 0.66,0.35 "{/:Bold r_{Tmin} = 0.96}"
set label at graph 0.1,0.87 "{/:Bold 17.5 ({/Symbol \260}C)}"
set label at graph 0.73,0.1 "{/:Bold 18 ({/Symbol \260}C)}"

set arrow front from 18, graph 0 to 18, graph 1 nohead lw 2

ymin(x)=C+D*x

fit ymin(x) 'Tdata_PAMPLONA_AERO_sesgocorr.dat' u 3:4 via C,D

p 'Tdata_PAMPLONA_AERO_sesgocorr.dat' u 3:4 w p lt 7 ps 1 lc rgb "red" notitle,\
  ymin(x) w l lw 3 t "T_{ERA5} = 0.46 + 0.95T_{OBS} ({/Symbol \260}C)",17.54 lw 2 lc rgb "black" notitle


unset multiplot
