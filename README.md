# **Sentence Rebuilder** 📝

## Description 💡

This Python function `rebuild_sentence(words, lengths)` is designed to reconstruct a sentence based on a list of words and corresponding lengths. If the length of the words list doesn't match the lengths list, it will handle the discrepancies by either prompting the user to input missing lengths or filling them automatically with word lengths. Once the lengths are set, it rebuilds the sentence by truncating each word to the specified length.

For example:
- **Input**: 
  - `words`: `["Hello", "world", "this", "is", "Python"]`
  - `lengths`: `[3, 5, 4, 2]`
- **Output**: `"Hel world this is"`

### Why is it Useful? 🤔
This function is helpful in scenarios where you need to truncate or manipulate words based on specified lengths. It's flexible, allowing users to correct or complete the lengths interactively and ensures that the final sentence is rebuilt accordingly. This is useful for text processing, formatting, or any use case where the length of words needs to be controlled.

---

## **Features** ✨

- **User Input for Missing Lengths**: When the lengths list is shorter than the words list, the function asks the user for the missing lengths.
- **Automatic Length Assignment**: If the number of missing lengths is large, the function automatically uses the actual lengths of the words.
- **Error Handling**: The function includes input validation to ensure the user provides valid integers for lengths, and defaults to the word's actual length in case of invalid input.

---


