# Functions go here 
def num_check(question, low): 

    valid = False 
    while not valid: 

        error = "please choose a number that is more than (or equal to) {}".format(low)

        try: 
            # asks user for number
            response = int(input(question)) 

            # checks the number is more than 0
            if response >= low : 
                return response 

            else : 
                print(error) 
                print()

        except ValueError:
            print()
            print(error) 
            print()

def statement_generator(text, decoration, lines) :
    middle = "{} {} {}".format(decoration*3, text, decoration*3)
    top_bottom = decoration * len(middle)

    if lines == 3:
        print(top_bottom)
        print(middle)
        print(top_bottom)
    elif lines == 2:
        print(middle)
        print(top_bottom)
    else:
        print(middle)

    return None

    
    statement_generator("Bits Calculator", "-")

# needs to be changed
def instructions(): 

    statement_generator("Instructions / Information", "=", 3) 
    print() 
    print("please choose a data type (image / text / integer)") 
    print() 
    print("this program assumes that the images that are being represented in 24 bit colour (ie: 24 bits per pixel). For text, we assume that ascii encoding is being used (8 bits per character).") 
    print() 
    print("Complete as many calculations as necessary, pressing <enter> at the end of each calculation or any key to quit.") 
    print() 
    return""

def get_factors(): 
    
# Main routine goes here