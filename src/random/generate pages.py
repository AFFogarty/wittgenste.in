import re

head = open("template/head.html", "r").read()
foot = open("template/foot.html", "r").read()

single = open("./single_output/index.html", 'w')

single.write(head)

for i in range(10000):
    prop_file = open("./output_stripped/{0}.txt".format(i), 'r')
    prop = re.sub(r'^\d\.\d*', '', prop_file.read())
    prop_file.close()

    # Strip numbers from left of string

    # page = open("./pages/{0}.html".format(i), 'w')
    # page.write("{0}\n<li>{1}</li>\n{2}".format(head, prop, foot))
    single.write("\n\n<li>{0}</li>\n\n".format(prop))
    # page.close()


single.write(foot)

single.close()