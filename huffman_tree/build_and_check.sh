mark=v2
cat label.freq | python huffman_v2.py outp$mark outl$mark > log$mark 2>err$mark
sort -n -k 4,4 log$mark >logs$mark
cat log$mark | python check.py > logc$mark 2>errc$mark
