import langdetect

text_fr="Bonjour la famille comment allez vous?"
text_en="how are you?"
print(langdetect.detect(text_fr))
print(langdetect.detect_langs(text_en))