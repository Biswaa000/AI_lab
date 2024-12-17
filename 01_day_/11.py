
def   function():
    sentence=input("Enter the sentence:-")
    char_dict=dict()
    for i in sentence:
        if i not in char_dict:
            char_dict[i]=1
        else:
            char_dict[i] += 1

    print(char_dict)

function()