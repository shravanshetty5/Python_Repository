from pythonds.graphs import Graph

def buildGraph(wordDoc):
    d = {}
    g = Graph()
    wfile = open(wordFile, 'r')
    #create bucket of words that differ by one letter and add the word to the bucket.
    for line in wordFile:
        #Assuming word file has 1 word per line
        word = line.strip()
        for i in range(len(word)):
            bucket = word[:i] + '_' + word[i+1:]
            if bucket in d:
                d[bucket].append[word]
            else:
                d[bucket] = [word]
    #Connect words in same bucket with edges.
    for bucket in d:
        for word1 in bucket:
            for word2 in bucket:
                if word1 != word2:
                    g.addEdge(word1,word2)
    return g
