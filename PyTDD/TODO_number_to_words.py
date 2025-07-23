def number_to_words(n):
    ones = ["", "one", "two", "three", "four", "five",  "six", "seven", "eight", "nine"]
    
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    # Define the lookup arrays FIRST
    # Now use them in your logic
    if n == 0:
        return "zero"
    
    # for 1-9
    if n < 10:
        return ones[n]
    
    # for 10-19
    if n < 20:
        return teens[n-10]