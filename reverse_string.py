def reverse_words(s: str) -> str:
    words = s.strip().split()
    return ' '.join(words[::-1])

input_str = "the sky is blue"
output_str = reverse_words(input_str)
print(output_str)
