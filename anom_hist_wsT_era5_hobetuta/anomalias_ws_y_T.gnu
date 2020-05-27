#! /usr/bin/gnuplot

set term pngcairo size 1000,800 enhanced color font 'Latin Modern Roman'

###########################
#Velocidad media del viento
###########################

set out 'anom_ws.png'

set multiplot layout 2,1 rowsfirst
set nokey

set xzeroaxis ls -1 lw 2 lc rgb "black"

#
#Aeropuerto de Bilbo
####################

unset mxtics
set xdata time
set grid xtics ytics mytics back lt 0 lw 1.5
set timefmt '%Y-%m-%d'
set xrange ["1986-01-01":"2016-12-31"]
set format x '%Y'

set xtics "1986-01-01",2.05*365*24*3600,"2016-12-31" font ", 12"
set ytics font ", 12"

set title "{/:Bold {/=15 Anomalías de velocidad del viento. Aeropuerto de Bilbo (1986-2016)"

set ylabel "{/=14 Velocidad (m/s)}"
p 'anom_ws_BILBAO_AERO.dat' u 1:2 w l lc rgb "blue"

#
#Madrid, Cuatro Vientos
#######################

set title "{/:Bold {/=15 Anomalías de velocidad del viento. Cuatro Vientos, Madrid (1986-2016)"

p 'anom_ws_CUATRO_VIENTOS.dat' u 1:2 w l lc rgb "#FF8C00"

unset multiplot

##################
#Temperatura media
##################

set out 'anom_T.png'

set title "{/:Bold {/=17 Anomalias de la temperatura media"

set multiplot layout 2,1 rowsfirst
set nokey

set xzeroaxis ls -1 lw 2 lc rgb "black"

#
#Aeropuerto de Bilbo
####################

set title "{/:Bold {/=15 Anomalías de temperatura media. Aeropuerto de Bilbo (1986-2016)

set ylabel "{/=14 Temperatura (ºC)}"
p 'anom_T_BILBAO_AERO.dat' u 1:2 w l title '{/:Bold Aeropuerto de Bilbao}'

#
#Madrid, Cuatro Vientos
#######################

set title "{/:Bold {/=15 Anomalías de temperatura media. Cuatro Vientos, Madrid (1986-2016)"

set ylabel "{/=14 Anomalía de temperatura (ºC)}"
p 'anom_T_CUATRO_VIENTOS.dat' u 1:2 w l lc rgb "#008B8B" title '{/:Bold Madrid, Cuatro Vientos}'

unset multiplot
