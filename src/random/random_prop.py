from pymarkovchain import MarkovChain

mc = MarkovChain("./markov")

tractatus = open("../api/static/tractatus_stripped.txt", 'r')

tractatus_string = tractatus.read()

mc.generateDatabase(tractatus_string, '\n')

print(mc.generateString())

for i in range(10000):
    f = open("./output_stripped/{0}.txt".format(i), 'w')
    f.write(mc.generateString())
    f.close()