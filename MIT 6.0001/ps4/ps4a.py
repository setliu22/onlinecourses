# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):

    if len(sequence) == 1:
        return [sequence]
    biglist = []
    for i in sequence:
        
        last = sequence.replace(i,"")
        
        perms = get_permutations(last)
        
        for iii in perms:
            biglist.append(i + iii)
        
    return biglist
            
            
            
            


if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)


    print(get_permutations("abc"))

