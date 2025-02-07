# palindrome is simply a text, word that written left-right and right-left is similar
# Time complexity: O(n)
def palindrome(txt: str):
    # it just compares text to backwards version of it if it's the same
    return txt == txt[::-1]

print(palindrome('mom'))