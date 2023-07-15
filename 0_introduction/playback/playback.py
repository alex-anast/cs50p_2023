'''
In a file called playback.py, implement a program in Python
that prompts the user for input and then outputs that same input,
replacing each space with ... (i.e., three periods).
'''

def main():
    user_input = input("Type your input: ")
    print(replace_space(user_input))

    
def replace_space(input: str) -> str:
    return input.replace(" ", "...")
    

if __name__ == '__main__':
    main()
