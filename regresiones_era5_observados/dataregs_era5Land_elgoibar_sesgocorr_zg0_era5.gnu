#! /usr/bin/gnuplot

set term pngcairo size 900,900 font "Latin Modern Roman"

set out "regs_era5Land_elgoibar_sesgocorr_zg0_era5.png"

set multiplot layout 2,1 rowsfirst

#
#Temperatura maxima
#

set title "{/:Bold {/=16 Linear regression of maximum temperature. Elgoibar (1997-2016) \n{/=14 Normalized to mean sea level by ERA5 geopotential}"

set key at graph 0.36,0.75

set xlabel "{/=14 AEMET observed temperature ({/Symbol \260}C)}"
set ylabel "{/=14 ERA5 LAND temperature ({/Symbol \260}C)}"

set label at graph 0.6,0.35 "{/:Bold r_{Tmax} = 0.96}"
set label at graph 0.1,0.87 "{/:Bold 29.9 ({/Symbol \260}C)}"
set label at graph 0.79,0.1 "{/:Bold 35 ({/Symbol \260}C)}"

set arrow front from 35, graph 0 to 35, graph 1 nohead lw 2


ymax(x)=A+B*x

fit ymax(x) 'Tdata_ELGOIBAR_sesgocorr_zg0_era5.dat' u 1:2 via A,B

p 'Tdata_ELGOIBAR_sesgocorr_zg0_era5.dat' u 1:2 w p lt 7 ps 1 lc rgb "red" notitle,\
  ymax(x) w l lw 3 t "T_{ERA5} = -6.43 + 1.04T_{OBS} ({/Symbol \260}C)",29.87 lw 2 lc rgb "black" notitle

#
#Temperatura minima
#

set title "{/:Bold {/=16 Linear regression of minimum temperature. Elgoibar (1997-2016) \n{/=14 Normalized to mean sea level by ERA5 geopotential}"

set key at graph 0.37,0.61

unset label
set xlabel "{/=14 AEMET observed temperature ({/Symbol \260}C)}"
set ylabel "{/=14 ERA5 LAND temperature ({/Symbol \260}C)}"

set label at graph 0.77,0.35 "{/:Bold r_{Tmin} = 0.95}"
set label at graph 0.1,0.72 "{/:Bold 11.9 ({/Symbol \260}C)}"
set label at graph 0.64,0.1 "{/:Bold 17 ({/Symbol \260}C)}"

set arrow front from 17, graph 0 to 17, graph 1 nohead lw 2

ymin(x)=C+D*x

fit ymin(x) 'Tdata_ELGOIBAR_sesgocorr_zg0_era5.dat' u 3:4 via C,D

p 'Tdata_ELGOIBAR_sesgocorr_zg0_era5.dat' u 3:4 w p lt 7 ps 1 lc rgb "red" notitle,\
  ymin(x) w l lw 3 t "T_{ERA5} = -5.07 + 1.00T_{OBS} ({/Symbol \260}C)",11.93 lw 2 lc rgb "black" notitle


unset multiplot
