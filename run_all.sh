#!/bin/bash
run_all(){
  cd $1
  for i in $(seq 1 31);
  do
    i=$(printf %02d $i)
    filename="day$i.py"
    if test -f "$filename"; then
      PYTHONPATH=..: python "$filename"
    fi
  done
  cd ..
}

if test -f "run_all.sh"; then
  for year in "20"*
  do
    run_all $year
  done
else
  run_all
fi
