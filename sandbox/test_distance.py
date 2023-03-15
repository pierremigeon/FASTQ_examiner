#!/usr/bin python3


from difflib import SequenceMatcher

def longest_common_substring(s1: str, s2: str) -> str:
    seq_matcher = SequenceMatcher(isjunk=None, a=s1, b=s2)
    match = seq_matcher.find_longest_match(0, len(s1), 0, len(s2))
    if match.size:
        return s1[match.a : match.a + match.size]
    else:
        return ""

def longest_common_substring_percentage(s1 : str, s2 : str) -> float:
	if min(len(s1), len(s2)) == 0:
		return 0
	return len(longest_common_substring(s1, s2)) / min(len(s1), len(s2))

print(longest_common_substring_percentage("+", "+defabcajdj+djdjfkff"))


