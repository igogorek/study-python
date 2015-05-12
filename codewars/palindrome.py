__author__ = 'igogor'
import test


def longest_palindrome(s):
    length = len(s)
    substrings = [s[i:j+1] for i in xrange(length) for j in xrange(i, length)]
    substrings.sort(key=len, reverse=True)
    for substring in substrings:
        if substring == substring[::-1]:
            return len(substring)

longest_palindrome("a")
# test.assert_equals(longest_palindrome("aa"), 2)
# test.assert_equals(longest_palindrome("baa"), 2)
# test.assert_equals(longest_palindrome("aab"), 2)
# test.assert_equals(longest_palindrome("abcdefghba"), 1)
# test.assert_equals(longest_palindrome("baablkj12345432133d"), 9)
