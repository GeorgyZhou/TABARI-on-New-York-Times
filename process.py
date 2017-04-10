import glob
import os
import re

def fullJustify(words, maxWidth):
    """
    :type words: List[str]
    :type maxWidth: int
    :rtype: List[str]
    """
    if len(words) == 0 or maxWidth == 0:
        return [""]
    line = []
    count = 0
    lines = []
    for word in words:
        n = len(line)
        if count + n + len(word) <= maxWidth:
            count += len(word)
            line.append(word)
        elif n > 1:
            realline = []
            margin = (maxWidth - count) / (n - 1)
            residue = (maxWidth - count) % (n - 1)
            for w in line:
                split = (' ' * margin) if residue == 0 else  (' ' * (margin + 1))
                if residue > 0:
                    residue -= 1
                realline.append(w)
                realline.append(split)
            del realline[-1]
            lines.append(''.join(realline))
            line = [word]
            count = len(word)
        elif n == 1:
            realline = []
            realline.append(line[0])
            realline.append(' ' * (maxWidth - count))
            lines.append(''.join(realline))
            line = [word]
            count = len(word)
    realline = []
    for word in line:
        realline.append(word)
        realline.append(' ')
    if count + len(line) > maxWidth:
        del realline[-1]
    else:
        realline.append(' ' * (maxWidth - count - len(line)))
    lines.append(''.join(realline))
    return lines

def clean_data():
    """
    clean the input reports data
    return
    """
    split_string = "/*_______________________________________________________________*/\n"
    fns = glob.glob("Abstract/*.txt")
    for fn in fns:
        content = []
        with open(fn, 'r') as f:
            abstract = []
            for line in f:
                if line == split_string:
                    # print line
                    abstract[0] += '\n'
                    article = ''.join(abstract).rstrip(' ')
                    article = article.rstrip(',')
                    content.append(article)
                    del abstract[:]
                else:
                    abstract.append(re.sub(r"[^A-Za-z0-9,.'\-:]+", ' ', line))
        new_fn = fn.lstrip('Absttract/').rstrip('.txt') + '.text'
        with open(new_fn, 'w') as f:
            for article in content:
                title = article.split('\n')[0] + '\n'
                article = '\n'.join(fullJustify(article.split('\n')[1].split(' '), 100))
                f.write(title)
                f.write(article)
                f.write('\n\n')
    fns = glob.glob("FullText/*.txt")
    for fn in fns:
        content = []
        with open(fn, 'r') as f:
            full_text = []
            for line in f:
                if line == split_string:
                    full_text[0] += '\n'
                    article = ''.join(full_text).rstrip(' ')
                    article = article.rstrip(',')
                    content.append(article)
                    del full_text[:]
                else:
                    full_text.append(re.sub(r"[^A-Za-z0-9,.'\-:]+",' ', line))
        new_fn = fn.lstrip('FullText/').rstrip('.txt') + '.text'
        with open(new_fn, 'w') as f:
            for article in content:
                title = article.split('\n')[0] + '\n'
                article = '\n'.join(fullJustify(article.split('\n')[1].split(' '), 100))
                f.write(title)
                f.write(article)
                f.write('\n\n')


if __name__ == "__main__":
    clean_data()
