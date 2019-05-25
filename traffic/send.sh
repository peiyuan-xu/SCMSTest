#!/bin/bash
echo "Hello World !"

ts=$[$(date +%s%N)/1000000]
curl http://localhost:8080/servicegw/user_buy
te=$[$(date +%s%N)/1000000]
val=`expr $te - $ts`
echo $val
