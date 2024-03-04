import sys

def ft_filter(function_to_apply, list_of_inputs):
    return [i for i in list_of_inputs if function_to_apply(i)]

def main():
    args = sys.argv[1:]
    if len(args) != 2:
        raise AssertionError("Exactly two arguments are required: a string and an integer")

    # The first argument is a string of words separated by spaces
    words = args[0].split(' ')
    # The second argument is an integer that specifies the minimum word length
    try:
        min_length = int(args[1])
    except ValueError:
        raise AssertionError("The second argument must be an integer")

    # Define a lambda function to check if the word length is greater than min_length
    filter_function = lambda word: len(word) > min_length

    # Apply the ft_filter function using the lambda function and the list of words
    filtered_words = ft_filter(filter_function, words)

    print(filtered_words)

if __name__ == "__main__":
    main()
