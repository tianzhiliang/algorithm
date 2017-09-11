import sys
import random

def load_dict():
    words = {}
    ids = []
    counts = []
    for line in sys.stdin:
        slot = line.strip().split()
        word, count = slot[7], slot[9]
        count = int(count)
        words[word] = count
        ids.append(word)
        counts.append(count)
    
    print >> sys.stderr, "load_dict done. lenwords:", len(words), "lenids:", len(ids), "lencounts:", len(counts)
    return words, ids, counts

def exchange(array, a, b):
    tmp = array[a]
    array[a] = array[b]
    array[b] = tmp
    
def random_noise(counts, pathlens):
    a = int(random.random() * len(pathlens))
    b = int(random.random() * len(pathlens))
    return a, b
    
def check(counts, pathlens):
    print "standard"
    result = weighted_path(counts, pathlens)

    print "\nnoise"
    noise_result = []
    for i in range(1000):
        a, b = random_noise(counts, pathlens)
        exchange(pathlens, a, b)
        result = weighted_path(counts, pathlens)
        exchange(pathlens, b, a)
        noise_result.append(result)

    print "\nnoise sorted"
    print "\n".join(map(str, sorted(noise_result)))

def weighted_path(counts, pathlens):
    sum = 0
    for count, pathlen in zip(counts, pathlens):
        sum += int(count) * int(pathlen)
    print sum
    return sum

if __name__ == "__main__":
    words, counts, pathlens = load_dict()
    check(counts, pathlens)
