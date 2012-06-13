#!/bin/bash

# timestamp - A unix timestamp of when the update occured.
# username  - The name of the user who made the update.
# type      - Single character for the update type - (A)dded, (M)odified or (D)eleted.
# file      - Path of the file updated.
# colour    - A colour for the file in hex (FFFFFF) format. Optional.

cat ../datos/coops.csv | tr " " "-" | sed s/"--"/"-"/g | tr -d '"' | while read LINE
do
    DATE=$(echo "$LINE" | awk '{print $1}' FS=',' | tr "/" " " | awk '{print $3"-"$2"-"$1}')
    # echo $DATE
    TIME=$(date -d "$DATE 00:00:00" "+%s")
    #echo $TIME
    USER="coop"
    STATUS="A"
    PAGE=""
    PROV=$(echo $LINE | awk '{print $2}' FS=',' | tr A-Z a-z)
    LOCA=$(echo $LINE | awk '{print $3}' FS=',' | tr A-Z a-z)
    TIPO=$(echo $LINE | awk '{print $4}' FS=',')
    T=$(echo $TIPO | tr -d '"' | tr "-" " " | awk '{print $1}')
    COLOR=$(grep $T tipos-basicos | head -1 | awk '{print $1}')
    NRO=$(echo $LINE  | awk '{print $5}' FS=',')
    NOMBRE=$(echo $LINE  | awk '{print $6}' FS=',' | tr "-" " " | tr A-Z a-z | cut -c -20)
    echo $TIME"|"$TIPO"|"$STATUS"|"$PROV"/"$LOCA"/"$NRO"-"$NOMBRE"|"$COLOR
done | sort -n | tee gource.log


