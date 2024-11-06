def rebuild_sentence(words, lengths):
    # Check if the lengths list is shorter than the words list
    if len(lengths) < len(words):
        missing_lengths = len(words) - len(lengths)

        if missing_lengths < 4:
            # If the number of missing lengths is less than 4, ask the user for each missing length
            for i in range(missing_lengths):
                word = words[len(lengths) + i]
                
                try:
                    # Ask the user for the length
                    user_length = int(input(f"Enter the length for '{word}': "))

                    # Validate the length input
                    if user_length < 0:
                        print(f"Invalid length: {user_length}. Same as in list of words {len(word)}.")
                        lengths.append(len(word))  # Word's actual length
                    elif user_length > len(word):
                        print(f"Invalid length: Same as in list of words {len(word)}.")
                        lengths.append(len(word))  #  Word's actual length
                    else:
                        lengths.append(user_length)  # Valid length
                except ValueError:
                    print("Enter a valid integer.")
                    lengths.append(len(word))  # Default to word length if input is invalid
        else:
            print("Filling with word lengths.")
            # Automatically fill missing lengths with the actual word lengths
            lengths.extend(len(word) for word in words[len(lengths):])

    elif len(lengths) > len(words):
        # Truncate the lengths list if it's longer than the words list
        print("The lengths list is longer than the words list.")
        lengths = lengths[:len(words)]
    
    # Rebuild the sentence using the specified lengths 
    result = ""
    for i in range(len(words)):
        result += words[i][:lengths[i]] + " "
    
    return result.strip()  
