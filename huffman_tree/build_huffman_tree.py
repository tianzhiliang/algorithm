import sys
import math

DEBUG = 0

class Node():
    def __init__(self):
        self.r = -1
        self.l = -1
        self.c = -1
        self.c_ori = -1
        self.wid = -1
        self.wstr = ""
        self.printed = False
        self.in_tree = False
        self.codelen = -1
        self.point = []
        self.code = []

    def set(self, word, id, count):
        self.wstr = word
        self.wid = id
        self.c = count

    def set_point_array(self, size):
        for i in range(size):
            self.point.append(-1)

def load_dict_v2():
    words = {}
    ids = []
    counts = []
    for i, line in enumerate(sys.stdin):
        slot = line.strip()
        count = int(slot)
        word = i
        words[word] = count
        ids.append(word)
        counts.append(count)
    
    print >> sys.stderr, "load_dict done. lenwords:", len(words), "lenids:", len(ids), "lencounts:", len(counts)
    return words, ids, counts

def load_dict():
    words = {}
    ids = []
    counts = []
    for line in sys.stdin:
        slot = line.strip().split("\t")
        word, count = slot
        count = int(count)
        words[word] = count
        ids.append(word)
        counts.append(count)
    
    print >> sys.stderr, "load_dict done. lenwords:", len(words), "lenids:", len(ids), "lencounts:", len(counts)
    return words, ids, counts

def build(words, ids, counts, path_outputfile, label_outputfile):
    # init
    wordlist = []
    for word, id, count in zip(words, ids, counts):
        node = Node()
        node.set(word, id, count)
        wordlist.append(node)

    wordlist = sorted(wordlist, key = lambda x:x.c, reverse = True)
    #wordlist = sorted(wordlist, key = lambda x:x.c)
    len_words = len(wordlist)
    for i in range(len_words + 1):
        node = Node()
        node.set("", -1, int(1e8))
        wordlist.append(node)

    # build
    parent_node = [-1 for i in range(len_words * 2 + 1)]
    binary = [0 for i in range(len_words * 2 + 1)]
    pos1 = len_words - 1
    pos2 = len_words
    min1 = -1
    min2 = -1
    for i in range(len_words - 1):
        if pos1 >= 0:
            if wordlist[pos1].c < wordlist[pos2].c:
                min1 = pos1
                pos1 -= 1
            else:
                min1 = pos2
                pos2 += 1
        else:
            min1 = pos2
            pos2 += 1

        if pos1 >= 0:
            if wordlist[pos1].c < wordlist[pos2].c:
                min2 = pos1
                pos1 -= 1
            else:
                min2 = pos2
                pos2 += 1
        else:
            min2 = pos2 
            pos2 += 1 

        wordlist[len_words + i].c = wordlist[min1].c + wordlist[min2].c
        parent_node[min1] = len_words + i
        parent_node[min2] = len_words + i
        binary[min2] = 1
        if DEBUG >= 1:
            print >> sys.stderr, "min1:", min1, "min2:", min2, "merged count:", wordlist[len_words + i].c, "min1count:", wordlist[min1].c, "min2count:", wordlist[min2].c, "parent_node:", len_words + i
    
    code = [0 for i in range(len_words * 2 + 1)]
    point = [-1 for i in range(len_words * 2 + 1)]
    for a in range(len_words):
        b = a
        i = 0
        if DEBUG >= 2:
            print >> sys.stderr, "i,a,b:",i,a,b
        while True:
            if DEBUG >= 2:
                print >> sys.stderr, "i:",i,"b:",b
            code[i] = binary[b]
            point[i] = b
            i += 1
            b = parent_node[b]
            if b == len_words * 2 - 2:
                break

        wordlist[a].codelen = i
        wordlist[a].set_point_array(i + 1)
        if DEBUG >= 2:
            print >> sys.stderr, "wordlist[a].point:", wordlist[a].point, "i:", i
        wordlist[a].code = [-1 for ii in range(i)]
        wordlist[a].point[0] = len_words - 2
        for b in range(i):
            wordlist[a].code[i - b - 1] = code[b]
            if DEBUG >= 3:
                print >> sys.stderr, "b:",b,"i:",i,"point[b]:", point[b], "wordlist[a].point[i - b]:", wordlist[a].point[i - b]
            wordlist[a].point[i - b] = point[b] - len_words
    
    for i in range(len_words):
        print "i:", i, "wid:", wordlist[i].wid, "wstr:", wordlist[i].wstr, "wcnt:", wordlist[i].c, "pathlen:", wordlist[i].codelen , "path:", " ".join(map(str, wordlist[i].point[:wordlist[i].codelen])), "code:", " ".join(map(str, wordlist[i].code))
        if DEBUG >= 1:
            print >> sys.stderr, "i:", i, "wid:", wordlist[i].wid, "wstr:", wordlist[i].wstr, "wcnt:", wordlist[i].c, "pathlen:", wordlist[i].codelen , "code:", " ".join(map(str, wordlist[i].point[:wordlist[i].codelen])), "code:", " ".join(map(str, wordlist[i].code))
            
    fp = open(path_outputfile, "w")
    fl = open(label_outputfile, "w")
    wordlist_word = wordlist[:len_words]
    wordlist_word = sorted(wordlist_word, key = lambda x:x.wid)
    for word in wordlist_word:
        outpath = str(word.wid) + "\t" + " ".join(map(str, word.point[:word.codelen])) + "\n"
        outlabel = str(word.wid) + "\t" + " ".join(map(str, word.code)) + "\n"
        fp.write(outpath)
        fl.write(outlabel)
    fp.close()
    fl.close()
    
if __name__ == "__main__":
    path_outputfile = sys.argv[1]
    label_outputfile = sys.argv[2]
    words, ids, counts = load_dict_v2()
    build(words, ids, counts, path_outputfile, label_outputfile)
