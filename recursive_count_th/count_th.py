'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    if len(word) < 2:
      return 0
    elif len(word) == 2:
      return 1 if word == 'th' else 0
    else:
      return 1 + count_th(word[:n-1]) if word[-2:] == 'th' else 0 + count_th(word[:n-1])
