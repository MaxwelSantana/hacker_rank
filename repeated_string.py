def repeatedString(s, n):
    len_s = len(s)

    qtd_letter_a_on_word = s.count("a")
    qtd_repeat_word = n // len_s

    missing_letters = s[:(n % len_s)]
    qtd_letter_a_on_missing_letters = missing_letters.count("a")

    count_letter_a = (qtd_repeat_word * qtd_letter_a_on_word) + qtd_letter_a_on_missing_letters

    return count_letter_a


print(repeatedString('aba', 10))
