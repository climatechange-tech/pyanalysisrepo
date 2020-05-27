#! /usr/bin/gnuplot

set term pngcairo size 1500,1500 enhanced color font 'Latin Modern Roman'

set style line 1 lw 1 lc rgb "blue"
set style line 2 lw 1 lc rgb "#FF8C00"
set style line 3 lw 1 lc rgb "#008B8B"
set style line 4 lw 1 lc rgb "red"

set xdata time
set grid xtics ytics mytics back lt 0 lw 1.5
set timefmt '%Y-%m-%d'
set xrange ["1986-01-01":"2016-12-31"]
set format x '%Y'

set xtics "1986-01-01",2.05*365*24*3600,"2016-12-31" font ", 14"
set ytics font ", 14"

####################
#Aeropuerto de Bilbo
####################

set out 'sesgocorr_wsT_BILBAO_AERO.png'

set multiplot layout 4,1 rowsfirst
set key nobox right top font "Latin Modern Roman:Bold, 14"

set title "{/:Bold {/=23 Aeropuerto de Bilbo"

#
#Velocidad media del viento
###########################

unset mxtics

set ylabel "{/=18 Velocidad (m/s)}"
p 'ws_era5_sesgocorr_BILBAO_AERO.dat' u 1:2 w l ls 1 title '{/:Bold ERA5 WS original}'

unset title

p 'ws_era5_sesgocorr_BILBAO_AERO.dat' u 1:3 w l ls 2 title '{/:Bold ERA5 WS corregido por sesgo}'

#
#Temperatura media
##################

set ylabel "{/=18 Temperatura (ºC)}"
p 'T_era5_sesgocorr_BILBAO_AERO.dat' u 1:2 w l lw 1 title '{/:Bold ERA5 T original}'

p 'T_era5_sesgocorr_BILBAO_AERO.dat' u 1:3 w l ls 3 title '{/:Bold ERA5 T corregido por sesgo}'

unset multiplot

#######################
#Madrid, Cuatro Vientos
#######################

set out 'sesgocorr_wsT_CUATRO_VIENTOS.png'

set title "{/:Bold {/=23 Madrid, Cuatro Vientos"

set multiplot layout 4,1 rowsfirst

#
#Velocidad media del viento
###########################

set ylabel "{/=18 Velocidad (m/s)}"
p 'ws_era5_sesgocorr_CUATRO_VIENTOS.dat' u 1:2 w l ls 1 title '{/:Bold ERA5 WS original}'

unset title

p 'ws_era5_sesgocorr_CUATRO_VIENTOS.dat' u 1:3 w l ls 2 title '{/:Bold ERA5 WS corregido por sesgo}'

#
#Temperatura media
##################

set ylabel "{/=18 Temperatura (ºC)}"
p 'T_era5_sesgocorr_CUATRO_VIENTOS.dat' u 1:2 w l ls 1 title '{/:Bold ERA5 T original}'

p 'T_era5_sesgocorr_CUATRO_VIENTOS.dat' u 1:3 w l ls 3 title '{/:Bold ERA5 T corregido por sesgo}'

unset multiplot
