'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    n = len(word)
    if n < 2:
      return 0
    if n == 2:
        if word == 'th':
            return 1
        else:
            return 0
    sub_string = word[-2:]
    if sub_string == 'th':
        return 1 + count_th(word[:n-1])
    else:
        return 0 + count_th(word[:n-1])