# solving squaredle puzzle
# detect this word is english word or not
# squarle puzzle is a puzzle that you have to find a word longer then 4 letters in a square of letters
# every english letter can connect to another letter besde it (up, down, left, right,diaognal)
# the word can be connected in any direction
# every letter can be used only once
# find all the legal words in the square


import enchant
size = 5
str = "bpherlasmecohaynatwlsfrts"
letters = []
for i in range(size):
    letters.append(str[i*size:(i+1)*size])
print(letters)
# cnt = [[1,7,4,1],[5,8,4,1],[]]
dct = enchant.Dict("en_US")
words = set()

vis = [[0 for i in range(size)] for j in range(size)]


def dfs():
    for i in range(size):
        for j in range(size):
            dfs2(i, j, "")


def dfs2(i, j, word):
    # print(i, j)
    # print(word)
    if len(word) > 12:
        return
    if i < 0 or i >= size or j < 0 or j >= size:
        return
    if vis[i][j] == 1:
        return
    word += letters[i][j]
    if len(word) >= 4 and dct.check(word):
        # print(word)
        words.add(word)
    vis[i][j] = 1

    dfs2(i + 1, j, word)
    dfs2(i - 1, j, word)
    dfs2(i, j + 1, word)
    dfs2(i, j - 1, word)
    dfs2(i + 1, j + 1, word)
    dfs2(i + 1, j - 1, word)
    dfs2(i - 1, j + 1, word)
    dfs2(i - 1, j - 1, word)
    vis[i][j] = 0


dfs()


print(words)
