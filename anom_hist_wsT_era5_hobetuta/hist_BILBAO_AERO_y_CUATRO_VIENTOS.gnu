#! /usr/bin/gnuplot

set term pngcairo size 800,800 enhanced color font "Latin Modern Roman"

set key nobox at screen 0.85,0.85

set style histogram
set style data histograms
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

set xrange [-1:14]
set xtics font ", 12"
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

set xrange [-1:13]

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

set xrange [-1:31]
set xtics font ", 10"
unset mxtics

set xlabel "Temperatura (ºC)" font ", 16"
set ylabel "Nº de ocurrencias" font ",16"
p 'hist_T_BILBAO_AERO.dat' u 2 lw 1.8 lc rgb '#FF8C00' title "{/:Bold {/= 10 AEMET}}",\
  'hist_T_BILBAO_AERO.dat' u 4 lw 1.8 lc rgb '#008B8B' title "{/:Bold {/= 10 ERA5}}"

#
#Madrid, Cuatro Vientos
#######################

reset

set term pngcairo size 800,800 enhanced color font "Latin Modern Roman"

set key nobox at screen 0.85,0.85

se o "hist_T_CUATRO_VIENTOS.png"
se tit "{/:Bold {/=17 Temperatura media} {\nMadrid, Cuatro Vientos (1986-2016)"

#Zeroz azpiko balioak EZ DIRA behar bezala kokatzen x ardatzean!!
#GNUPlot-en bertsioaren funtzionamenduaren kontua da.
#Alternatiba erabili behar da horrelakoetan,
#edo bestela x ardatzeko balioak lekuz aldatu.


set grid
set boxwidth 0.35 relative
set style fill transparent solid 0.8 noborder

set xlabel "Temperatura (ºC)" font ", 16"
set ylabel "Nº de ocurrencias" font ",16"

p 'hist_T_CUATRO_VIENTOS.dat' u 1:2 w boxes lw 1.8 lc rgb '#FF8C00#' title "{/:Bold {/= 10 AEMET}}",\
  'hist_T_CUATRO_VIENTOS.dat' u ($1+0.4):4 w boxes lw 1.8 lc rgb '#008B8B' title "{/:Bold {/= 10 ERA5}}"

