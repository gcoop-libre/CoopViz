#!/bin/bash
#
# This script comes with ABSOLUTELY NO WARRANTY, use at own risk
# Copyright (C) 2012 Osiris Alejandro Gomez <osiris@gcoop.coop>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
# :Url: https://github.com/gcoop-libre/CoopViz
# :Author: Osiris Alejandro Gómez
# :Address: osiris@gcoop.coop
# :Copyright: 2012 gcoop.coop
# :License: GNU General Public License GPLv3
# :Version: 1.0

##--highlight-dirs \

cat gource.log | gource - --log-format custom \
--selection-colour FF0000 \
--stop-at-end \
-w -f  -b 000000 --camera-mode track -s 1 -1024x768 \
--date-format '%d %B %Y' \
--hide 'bloom,users' \
--max-files 0 --seconds-per-day 0.001 --file-idle-time 0 \
--dir-colour 4E90FE \
--title "Cooperativas de Argentina - SLyES2012@CCC - CC-BY-SA gcoop.coop" \
--font-size 16 --font-colour 4E90FE \
--logo puntitos.png --max-file-lag -1 \
--default-user-image '/home/osiris/data/dev/CoopViz/datos/colores/default.png' \
--user-image-dir '/home/osiris/data/dev/CoopViz/datos/colores/' \
--output-framerate 25 --output-ppm-stream - \
| ffmpeg -y -b 3000K -r 24 -f image2pipe -vcodec ppm \
-i - -vcodec libtheora SLyES-1024x768.ogg

