# AI-CIA-2
# DONE BY: ANANTH SHYAM S, AI&DS-A, Reg No. 22011101012

This Python code prompts the user to enter a specified number of 4-letter prompts. It then processes these prompts to find common substrings in the end of the previous prompt and the start of the subsequent prompt and concatenate them to form a final result. 

The execution of this Problem is done in 2 ways:
1. WITHOUT IMPLMENTATION OF AI ALGORITHMS
2. WITH IMPLEMENTATION OF AI ALGORITHMS

# ALGORITHM FOR THE CODE WITHOUT IMPLMENTATION OF AI ALGORITHMS:
1. The code begins by asking the user to input how many 4-letter prompts they will enter.
2. It collects the entered prompts and stores them in a list called 'a'.
3. The code then proceeds to iterate through the prompts to find common substrings in the end of the previous prompt and the start of the subsequent prompt and build the final result.
4. It initializes two lists: 'f' to store common substrings and 'new' to store non-common segments of prompts.
5. The code iterates through the list of prompts (from the third to the second-to-last prompt) and compares adjacent prompts to find common substrings or non-common segments.
6. Common substrings are appended to the 'f' list, and non-common segments are appended to the 'new' list.
7. The code joins the common substrings in the 'f' list and adds them to the first prompt and the last prompt to create the final result.
8. The final result is printed.


# ALGORITHM FOR THE CODE WITH IMPLEMENTATION OF AI ALGORITHMS:
IDENTITY ALGORITHM
1. Create an empty list common_elements to store the common substrings.
2. terate through the prompts, comparing each pair of adjacent prompts.
3. For each pair, find the longest common substring between the end of the first prompt and the beginning of the second prompt.
4. If the Longest Common Substring is not empty, add it to the common_elements list.

CLASSICAL SEARCH ALGORITHM
1. Initialize an empty string.
2. Iterate through the common elements list in order.
3. For each common substring, check if it is already present in the final word list.
4. If it is not present, append the common substring to the final word list.
