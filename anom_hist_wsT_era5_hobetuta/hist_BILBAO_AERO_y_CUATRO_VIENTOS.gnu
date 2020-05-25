#! /usr/bin/gnuplot

set term pngcairo size 800,800 enhanced color font "Latin Modern Roman"

set key nobox at screen 0.85,0.85

set style histogram
set style data histogram
set boxwidth 1
set style fill solid 1.00 noborder

#####################
#Velocidad del viento
#####################

#
#Aeropuerto de Bilbao
#####################

se o "hist_ws_BILBAO_AERO.png"
se tit "{/:Bold {/=17 Velodidad media del viento} {\nAeropuerto de Bilbo (1986-2016)"

#set xrange [-0.5:14.5]
set xtics 1 font ", 12"
unset mxtics

set xlabel "Velocidad (m/s)" font ", 16"
set ylabel "Nº de ocurrencias" font ",16"
p 'hist_ws_BILBAO_AERO.dat' u 2 lw 1.8 lc rgb '#FF8C00' title "{/:Bold {/= 10 AEMET}}",\
  'hist_ws_BILBAO_AERO.dat' u 4 lw 1.8 lc rgb '#008B8B' title "{/:Bold {/= 10 ERA5}}"

#
#Madrid, Cuatro Vientos
#######################

se o "hist_ws_CUATRO_VIENTOS.png"
se tit "{/:Bold {/=17 Velodidad media del viento} {\nMadrid, Cuatro Vientos (1986-2016)"

#set xrange [-0.5:11.5]

set xlabel "Velocidad (m/s)" font ", 16"
set ylabel "Nº de ocurrencias" font ",16"
p 'hist_ws_CUATRO_VIENTOS.dat' u 2 lw 1.8 lc rgb '#FF8C00#' title "{/:Bold {/= 10 AEMET}}",\
  'hist_ws_CUATRO_VIENTOS.dat' u 4 lw 1.8 lc rgb '#008B8B' title "{/:Bold {/= 10 ERA5}}"

##################
#Temperatura media
##################

#
#Aeropuerto de Bilbao
#####################

se o "hist_T_BILBAO_AERO.png"
se tit "{/:Bold {/=17 Temperatura media} {\nAeropuerto de Bilbo (1986-2016)"

#set xrange [-0.5:14.5]
set xtics 1 font ", 10"
unset mxtics

set xlabel "Temperatura (ºC)" font ", 16"
set ylabel "Nº de ocurrencias" font ",16"
p 'hist_T_BILBAO_AERO.dat' u 2 lw 1.8 lc rgb '#FF8C00' title "{/:Bold {/= 10 AEMET}}",\
  'hist_T_BILBAO_AERO.dat' u 4 lw 1.8 lc rgb '#008B8B' title "{/:Bold {/= 10 ERA5}}"

#
#Madrid, Cuatro Vientos
#######################

se o "hist_T_CUATRO_VIENTOS.png"
se tit "{/:Bold {/=17 Temperatura media} {\nMadrid, Cuatro Vientos (1986-2016)"

#set xrange [-0.5:11.5]

set xlabel "Temperatura (ºC)" font ", 16"
set ylabel "Nº de ocurrencias" font ",16"
p 'hist_T_CUATRO_VIENTOS.dat' u 2 lw 1.8 lc rgb '#FF8C00#' title "{/:Bold {/= 10 AEMET}}",\
  'hist_T_CUATRO_VIENTOS.dat' u 4 lw 1.8 lc rgb '#008B8B' title "{/:Bold {/= 10 ERA5}}"

