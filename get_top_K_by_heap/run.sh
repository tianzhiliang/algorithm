input=input.txt
output=output.txt
errlog=errlog
K=30

cat $input | ./get_top_K_by_heap $K > $output 2> $errlog
