
import re

# what would be output:

def get_matching_words(regex):
	results = []
	words = [
         "baby",
         "baseball",
         "denver",
         "facetious",
         "issue",
         "mattress",
         "obsessive",
         "paranoia",
         "rabble",
         "union",
         "volleyball",
     ]
	for word in words:
		if re.search(regex, word):
			results.append(word)
	return results

# my_expression = r"v"
# my_expression = r"^[aeiou]"
# my_expression = r"(ss)"
# my_expression = r"(b.b)"
# my_expression = r"(b.+b)"
# my_expression = r"(a.*e.*i.*o.*u)"
# my_expression = r"([aeiou]{2}$)"
# my_expression = r"^[regular expression]*$"
# my_expression = r"\b[regulaxpsion]+\b"
# my_expression = r"^[^regex]*$"
# my_expression = r"^[^<regex>]+$"
# my_expression = r"b.*b"
# my_expression = r"b.?b"
# my_expression = r"io"
# my_expression = r"(\w)\1.+e$"
# my_expression = r"(\w)\1.*(\w)\2$"
print get_matching_words(my_expression)




