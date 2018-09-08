'''
Purpose: Obscures lower case characters of a string using ROT13
Parameters: string - a string that the user wants encrypted
Returns: new_string - the encrypted string
'''
def rot13(string):
        
        list_of_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        new_string = ''
        
        #the runs through each character in a string
        for char in string:
                num_of_letter = 0
                if char.isalpha() == True:
                        if ord(char) >= 97:
                                #this gets the length of the alphabet (which in python is to 25, but is 26 long)
                                for item in range(len(list_of_letters)):
                                        if list_of_letters[item] == char:
                                                num_of_letter = 0
                                                num_of_letter = item + 13
                                                if num_of_letter > 25:
                                                        num_of_letter = num_of_letter - 26
                                                        new_string += list_of_letters[num_of_letter]
                                                else:
                                                        new_string += list_of_letters[num_of_letter]
                        else:
                                new_string += char
                else:
                        new_string += char
        return new_string