#! /usr/bin/gnuplot

set term pngcairo size 800,800 enhanced color font "Latin Modern Roman"

set key nobox at screen 0.45,0.85

set style histogram
set style data histogram
set style fill solid 1.00 noborder
set boxwidth 1

#####################
#Velocidad del viento
#####################

#
#Aeropuerto de Bilbao
#####################

se o "hist_decil_ws_BILBAO_AERO.png"
se tit "{/:Bold {/=18 Velodidad media del viento por deciles} {\nAeropuerto de Bilbo (1986-2016)" font ", 13"

#unset mxtics

set ylabel "Nº de ocurrencias" font ",16"
p 'hist_decil_ws_BILBAO_AERO.dat' u 3:xtic(1) lw 1.8 lc rgb '#FF8C00' title "{/:Bold {/= 10 AEMET}}",\
 'hist_decil_ws_BILBAO_AERO.dat' u 4:xtic(1) lw 1.8 lc rgb '#008B8B' title "{/:Bold {/= 10 ERA5}}",

#
#Madrid, Cuatro Vientos
#######################

#set key nobox at screen 0.9,0.87

se o "hist_decil_ws_CUATRO_VIENTOS.png"
se tit "{/:Bold {/=18 Velodidad media del viento por deciles} {\nMadrid, Cuatro Vientos (1986-2016)" font ", 13"

set ylabel "Nº de ocurrencias" font ",16"
p 'hist_decil_ws_CUATRO_VIENTOS.dat' u 3:xtic(1) lw 1.8 lc rgb '#FF8C00' title "{/:Bold {/= 10 AEMET}}",\
  'hist_decil_ws_CUATRO_VIENTOS.dat'u 4:xtic(1) lw 1.8 lc rgb '#008B8B' title "{/:Bold {/= 10 ERA5}}"

##################
#Temperatura media
##################

#
#Aeropuerto de Bilbao
#####################

se o "hist_decil_T_BILBAO_AERO.png"
se tit "{/:Bold {/=18 Temperatura media por deciles} {\nAeropuerto de Bilbo (1986-2016)" font ", 13"

set ylabel "Nº de ocurrencias" font ",16"
p 'hist_decil_T_BILBAO_AERO.dat' u 3:xtic(1) lw 1.8 lc rgb '#FF8C00' title "{/:Bold {/= 10 AEMET}}",\
  'hist_decil_T_BILBAO_AERO.dat' u 4:xtic(1) lw 1.8 lc rgb '#008B8B' title "{/:Bold {/= 10 ERA5}}"

#
#Madrid, Cuatro Vientos
#######################

se o "hist_decil_T_CUATRO_VIENTOS.png"
se tit "{/:Bold {/=18 Temperatura media por deciles} {\nCuatro Vientos, Madrid (1986-2016)" font ", 13"

set ylabel "Nº de ocurrencias" font ",16"
p 'hist_decil_T_CUATRO_VIENTOS.dat' u 3:xtic(1) lw 1.8 lc rgb '#FF8C00' title "{/:Bold {/= 10 AEMET}}",\
  'hist_decil_T_CUATRO_VIENTOS.dat' u 4:xtic(1) lw 1.8 lc rgb '#008B8B' title "{/:Bold {/= 10 ERA5}}"
