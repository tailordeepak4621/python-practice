def create_character(first, second, third, fourth):

    if " " in first:
        return "The character name should not contain spaces."
    

    if type(second) is not int or type(third) is not int or type(fourth) is not int:
        return "All stats should be integers."
        

    if second < 1 or third < 1 or fourth < 1:
        return "All stats should be no less than 1"
        

    if second > 4 or third > 4 or fourth > 4:
        return "All stats should be no more than 4"
        
   
    if (second + third + fourth) != 7:
        return "The character should start with 7 points"
        

    full_dot = "●"
    empty_dot = "○"
    
    str_dots = (full_dot * second) + (empty_dot * (10 - second))
    int_dots = (full_dot * third) + (empty_dot * (10 - third))
    cha_dots = (full_dot * fourth) + (empty_dot * (10 - fourth))
    
    return f"{first}\nSTR {str_dots}\nINT {int_dots}\nCHA {cha_dots}"


print(create_character("Deepak",4,2,1))