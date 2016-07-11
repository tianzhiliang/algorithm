input=input.txt
output=output.txt
errlog=errlog
K=30
#is_increasing_order=1
is_increasing_order=0

cat $input | ./get_top_K_by_heap $K $is_increasing_order > $output 2> $errlog
