#!/bin/bash
run_all(){
  cd $1
  for i in $(seq 1 31);
  do
    i=$(printf %02d $i)

    filename="day$i.py"
    if test -f "$filename"; then
      PYTHONPATH=../..: python "$filename" &
    fi

    filename="day$i/day$i.py"
    if test -f "$filename"; then
      PYTHONPATH=../..: python "$filename" &
    fi

    filename="day$i/day$i.go"
    if test -f "$filename"; then
      go run "$filename" &
    fi
  done
  cd ..
}

if test -f "run_all.sh"; then
  # running from root directory
  for year in "solutions/20"*
  do
    run_all $year &
  done
  wait
else
  # running from solutions/{year} directory
  run_all .
  wait
fi
