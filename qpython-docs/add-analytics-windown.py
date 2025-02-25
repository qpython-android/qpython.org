import sys, os

with open(sys.argv[1], 'r', encoding='gbk') as f, \
     open('./qpydoc.tmp', 'w', encoding='gbk') as g, \
     open(os.path.dirname(os.path.abspath(__file__)) + '/extra.txt', 'r', encoding='gbk') as e:
    pth = sys.argv[1][1:]
    extra = "".join(e.readlines()).replace("{{PTH}}", pth)
    g.write('\n'.join(
        filter(lambda s: len(s),
               map(lambda s:
                   ('', extra + "<hr/>")[s == '<div role="contentinfo">'] + s,
                   map(str.strip, f.readlines())))))
os.rename('./qpydoc.tmp', sys.argv[1])