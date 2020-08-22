#! /usr/bin/gnuplot

set term pngcairo size 900,900 font "Latin Modern Roman"

set out "regs_era5Land_elgoibar_sesgocorr.png"

set multiplot layout 2,1 rowsfirst

#
#Temperatura maxima
#

set title "{/:Bold {/=16 Linear regression of maximum temperature. Elgoibar (1997-2016) \n{/=14 ERA5Land data normalized to actual station level}"

set key at graph 0.4,0.74

set xlabel "{/=14 AEMET observed temperature ({/Symbol \260}C)}"
set ylabel "{/=14 ERA5 LAND temperature ({/Symbol \260}C)}"

set label at graph 0.6,0.35 "{/:Bold r_{Tmax} = 0.96}"
set label at graph 0.1,0.85 "{/:Bold 30.5 ({/Symbol \260}C)}"
set label at graph 0.79,0.1 "{/:Bold 35 ({/Symbol \260}C)}"

set arrow front from 35, graph 0 to 35, graph 1 nohead lw 2


ymax(x)=A+B*x

fit ymax(x) 'Tdata_ELGOIBAR_sesgocorr.dat' u 1:2 via A,B

p 'Tdata_ELGOIBAR_sesgocorr.dat' u 1:2 w p lt 7 ps 1 lc rgb "red" notitle,\
  ymax(x) w l lw 3 t "T_{ERA5} = -0.89 + 1.04T_{OBS} ({/Symbol \260}C)",35.41 lw 2 lc rgb "black" notitle

#
#Temperatura minima
#

set title "{/:Bold {/=16 Linear regression of minimum temperature. Elgoibar (1997-2016) \n{/=14 ERA5Land data normalized to actual station level}"

set key at graph 0.4,0.68

unset label
set xlabel "{/=14 AEMET observed temperature ({/Symbol \260}C)}"
set ylabel "{/=14 ERA5 LAND temperature ({/Symbol \260}C)}"

set label at graph 0.59,0.27 "{/:Bold r_{Tmin} = 0.95}"
set label at graph 0.1,0.83 "{/:Bold 17.3 ({/Symbol \260}C)}"
set label at graph 0.67,0.1 "{/:Bold 17 ({/Symbol \260}C)}"

set arrow front from 17, graph 0 to 17, graph 1 nohead lw 2

ymin(x)=C+D*x

fit ymin(x) 'Tdata_ELGOIBAR_sesgocorr.dat' u 3:4 via C,D

p 'Tdata_ELGOIBAR_sesgocorr.dat' u 3:4 w p lt 7 ps 1 lc rgb "red" notitle,\
  ymin(x) w l lw 3 t "T_{ERA5} = 0.32 + 1.00T_{OBS} ({/Symbol \260}C)",17.31 lw 2 lc rgb "black" notitle


unset multiplot
