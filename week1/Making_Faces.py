def convert(words): #defining convert function with parametr "words"
    return words.replace(":)", "🙂").replace(":(", "🙁") #returns a new string, which was modified by .replace 

def main(): #defining main function with no parameters 
    text = input() #creates variable "text" which is an input /stores the string typed by the user
    result = convert(text) #creates a variable "result" which is a call of function "convert" which uses the text string as the parametr for the function / calls convert with text as the argument and stores the returned string
    print(result) #prints the new text / "result"

main() #calls the main function