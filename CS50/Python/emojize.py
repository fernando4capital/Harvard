import emoji
sentence = input("Input: ")
with_emoji = emoji.emojize(sentence, language='alias')
print(with_emoji)