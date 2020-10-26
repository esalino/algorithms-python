# https://www.hackerrank.com/challenges/ctci-making-anagrams/problem
def make_anagrams(a, b):
    deletions = 0;
    dict_a = {}
    dict_b = {}

    # fill dict_a with character counts
    for c in a:
        count = dict_a[c] + 1 if c in dict_a else 1
        dict_a[c] = count;

    # fill dict_b with character counts as well as looking for characters
    # in 'b' that don't exist in 'a'
    for c in b:
        count = dict_b[c] + 1 if c in dict_b else 1
        dict_b[c] = count;
        # if dict_a does not have the char then we would need to delete
        # this char so increment deletions
        if c not in dict_a:
            deletions += 1
            continue
        # There is a match so decrement dict_a count
        dict_a[c] = dict_a[c] - 1;

    # Go back through dict_a to look for characters that don't exist in b
    for c in a:
        if c not in dict_b:
            deletions += 1
            continue
        dict_b[c] = dict_b[c] - 1;

    return deletions
