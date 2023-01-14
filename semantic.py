import spacy
nlp =spacy.load ('en_core_web_md')

# its amazing to see that cat a moneky have the highies  similiraty because both are animails, monkey and banana have a higher similiraty than cat and banana.
word1 =nlp("cat")
word2 = nlp ("monkey")
word3 = nlp ("banana")
print (word1.text, word2.text, word1.similarity(word2))
print (word3.text, word2.text, word3.similarity(word2))
print (word3.text, word1.text, word3.similarity(word1))

""" its amazing to see that cat a moneky have the highies  similiraty because both are animails, monkey and banana have a higher similiraty than cat and banana. 
Also I have added human and car but in my opnion human should have higer similiraty with all these as human do eat apples, bananas, have cats as pets, drive cars and like monkeys"""
tokens =nlp ("human cat apple monkey banana car")
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

sentence_to_compare = "why is my cat on the car"
sentences = ["where did my dog go","Hello, there is my car", "I\'ve lost my car in my car", "I\'d like my boat back", "I will name my dog Diana"]
model_sentence = nlp (sentence_to_compare)
for sentence in sentences:
    similarity = nlp (sentence).similarity (model_sentence)
    print (sentence + " - ", similarity)

# when I have ran the example file with the 'en_core_web_sm' all the similiraty figure were much lower than using the 'en_core_web_md'
