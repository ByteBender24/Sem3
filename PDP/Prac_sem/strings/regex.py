import re
pattern = re.compile(r'\d')
result = pattern.findall("This is a word in a sentence.")
print(result)

# -------------------------------------------------------------------------------------------------
print("\n\n")

'''
The re.DOTALL flag makes the dot (.) in a regex match all characters, including newline.
'''
pattern = re.compile(r'hello.world', re.DOTALL)
result = pattern.search("hello\nworld")
print(result)


# -------------------------------------------------------------------------------------------------
print("\n\n")

pattern = re.compile(r'''
                     \d+          # Match one or more digits
                     \s           # Match a whitespace character
                     [a-zA-Z]+    # Match one or more letters
                     ''', re.VERBOSE)
result = pattern.match("123 abc")

# -------------------------------------------------------------------------------------------------
print("\n\n")
'''
Non-Capturing Groups:
In regular expressions, groups are portions of the pattern enclosed in parentheses. Capturing groups ( ... ) capture the matched content, meaning you can access it later. However, there are cases where you want to group a pattern for the purpose of applying a quantifier or alternation but don't need to capture the result.

In the example you provided:

python
Copy code
import re
pattern = re.compile(r'(?:Mr|Mrs|Ms)\. (\w+)')
result = pattern.match("Mr. Smith")
(?:Mr|Mrs|Ms) is a non-capturing group that matches either "Mr," "Mrs," or "Ms" without capturing the matched prefix.
(\w+) captures one or more word characters (letters, digits, or underscores) after the title.
So, for the input "Mr. Smith," the entire match includes both the title and the name, but only the name is captured because of the non-capturing group.

Lookaheads and Lookbehinds:
Lookaheads ((?=...)) and lookbehinds ((?<=...)) are used to assert whether a certain pattern is ahead or behind the current position, without including that pattern in the actual match.

In the example:

python
Copy code
import re
pattern = re.compile(r'\d+(?=%)')
result = pattern.search("45%")
\d+ matches one or more digits.
(?=%) is a positive lookahead that asserts the presence of a "%" character without including it in the match.
So, for the input "45%," the pattern matches only the digits "45" because the lookahead ensures that the "%" is there but doesn't include it in the result.

In summary, non-capturing groups are used for grouping without capturing, and lookaheads/lookbehinds are used for asserting conditions without including the asserted part in the match. Let me know if you have more questions or need further clarification!'''
