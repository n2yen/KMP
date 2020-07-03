#
# Implementation of Knuth-Morris-Pratt (KMP) Algorithm
# anontated.
#
# Algorithm creates a text table for use with searches.
#
# Running Time is O(n+m), where 'n' is length of the searched text (typically large)
# and 'm' is the length of pattern (or pattern, typically small).
#
# Assumptions: length of pattern <= length of text, e.g. m <= n, otherwise
# function will not find the pattern
#
import itertools

def kmp_match(text, pattern):
    # By checking the largest word suffix which matches the word prefix, we can
    # generate a 'prefix table' that can then be used as a state machine, where 0 is the
    # initial state and the last character in the table being the accpeting state.
    #
    # We generate the prefix table by maintaining a running count of character matches
    # starting from the 2nd character as we are walking the word character by character.
    #
    # The reason this works is because the prefix count reveals how many prefix
    # matches at any point in the string. The prefix matches will let us know where in
    # the word to jump to (state change) if we see a mismatch as we are actually
    # matching the word.
    #

    def init_prefix_table(word):
        prefix_table = [0] * (len(word) + 1)
        prefix_table[0] = -1
        i, j = 0, -1
        while i < len(word):
            if j == -1 or word[i] == word[j]:
                i += 1
                j += 1
                prefix_table[i] = j
            else:
                j = prefix_table[j]
        return prefix_table[1:]

    prefix_table = init_prefix_table(pattern)
    #print ('prefix table:', prefix_table)

    # now that we have the state_table (aka prefix table) created, we can do the string matching
    # using it as a guide for state transitions
    pattern_index = 0
    for text_index, text_ch in enumerate(text):
        # Check for failure; if failure, then transition to the correct
        # intermediate state. If no intermediate state is found, then we will go
        # to the initial state and thus exit the while loop
        # the state variable also informs the correct index into the pattern string
        while pattern_index > 0 and text_ch != pattern[pattern_index]:
            pattern_index = prefix_table[pattern_index-1]

        if text_ch == pattern[pattern_index]:
            if pattern_index == len(pattern)-1:
                return text_index-pattern_index
            # update the automaton pattern_index
            pattern_index+=1

    return -1


def main():
    print('Knuth Morris Pratt (KMP) string search algorithm')

    Input = 'y ababaca siifjae', 'ababaca'
    print(Input)
    res = kmp_match(Input[0], Input[1])
    print('len:', len(Input[1]))
    print('result:', res, "'{}'".format(Input[0][res:res+len(Input[1])]))
    assert Input[0][res:res+len(Input[1])] == Input[1]
    print('correct:', Input[0].find(Input[1]))
    assert res == Input[0].find(Input[1])

    Input = 'y ababac siifjae', 'ababac'
    print(Input)
    res = kmp_match(Input[0], Input[1])
    print('len:', len(Input[1]))
    print(res, "'{}'".format(Input[0][res:res+len(Input[1])]))
    assert Input[0][res:res+len(Input[1])] == Input[1]
    print('correct:', Input[0].find(Input[1]))
    assert res == Input[0].find(Input[1])

    Input = 'abababacsiifjae', 'ababac'
    print (Input)
    res = kmp_match(Input[0], Input[1])
    print ('len:', len(Input[1]))
    print (res, "'{}'".format(Input[0][res:res+len(Input[1])]))
    print ('correct:', Input[0].find(Input[1]))
    assert Input[0][res:res+len(Input[1])] == Input[1]
    assert res == Input[0].find(Input[1])

    Input = 'adfbec dsfoeifj asdfjww abyyabcdefg siifjae', 'aba'
    print (Input)
    res = kmp_match(Input[0], Input[1])
    print ('len:', len(Input[1]))
    print (res)
    print ('correct:', Input[0].find(Input[1]))
    assert res == Input[0].find(Input[1])

    Input = 'adfbec dsfoeifj asdfjww sifmyy abcdefg siifjae', 'ab'
    print (Input)
    res = kmp_match(Input[0], Input[1])
    print ('len:', len(Input[1]))
    print (res, "'{}'".format(Input[0][res:res+len(Input[1])]))
    print ('correct:', Input[0].find(Input[1]))
    assert res == Input[0].find(Input[1])

    Input = 'adfbec dsfoeifj asdfjww sifmyy abcdefg siifjae', 'a'
    print (Input)
    res = kmp_match(Input[0], Input[1])
    print ('len:', len(Input[1]))
    print (res, "'{}'".format(Input[0][res:res+len(Input[1])]))
    print ('correct:', Input[0].find(Input[1]))
    assert res == Input[0].find(Input[1])

    Input = 'adfbec dsfoeifj asdfjww sifmyy abcdefg siifjae', 'aa'
    print (Input)
    res = kmp_match(Input[0], Input[1])
    print ('len:', len(Input[1]))
    print (res, "'{}'".format(Input[0][res:res+len(Input[1])]))
    print ('correct:', Input[0].find(Input[1]))
    assert res == Input[0].find(Input[1])

    Input = "ababac", "ababac",
    print (Input)
    res = kmp_match(Input[0], Input[1])
    print ('len:', len(Input[1]))
    print (res, "'{}'".format(Input[0][res:res+len(Input[1])]))
    print ('correct:', Input[0].find(Input[1]))
    assert res == Input[0].find(Input[1])

    Input =  "aabaaabaaac", "aabaaac"
    print (Input)
    res = kmp_match(Input[0], Input[1])
    print ('len:', len(Input[1]))
    print (res, "'{}'".format(Input[0][res:res+len(Input[1])]))
    print ('correct:', Input[0].find(Input[1]))
    assert res == Input[0].find(Input[1])

    Input = 'bacbababaabcbab', 'ababababca'
    print (Input)
    res = kmp_match(Input[0], Input[1])
    print ('len:', len(Input[1]))
    print ('res:', res, "'{}'".format(Input[0][res:res+len(Input[1])]))
    print ('correct:', Input[0].find(Input[1]))
    assert res == Input[0].find(Input[1])
 

if __name__ == "__main__":
    main()
