# anagram is two words that have the same amount of letters and type of letters
# like dusty study: has d, yup, u too, s also, t also, and y as well, all match
# Time complexity: O(n log n)
def anagram(txt: str, txt_two: str):
    # sorts through all letters and if they're the same then it's an anagram
    return sorted(txt) == sorted(txt_two)

print(anagram('night', 'thing'))