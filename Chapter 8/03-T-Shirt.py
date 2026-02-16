# 8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the
# text of a message that should be printed on the shirt. The function should
# print a sentence summarizing the size of the shirt and the message printed
# on it.
# Call the function once using positional arguments to make a shirt. Call the
# function a second time using keyword arguments.

def make_shirt(size , text):
    """Display shirt size"""
    print(f"this shirt size is : {size}")
    print(f"and the text on the shirt is {text}\n")

make_shirt('XL' , 'Ramadan Kareem')
make_shirt(size='XL' , text='Ramadan Kareem')