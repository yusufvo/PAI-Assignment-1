
allPosts = [
  {'id': 1, 'text': 'I LOVE the new #GulPhone! Battery life is amazing.'},
  {'id': 2, 'text': 'My #GulPhone is a total disaster. The screen is already broken!'},
  {'id': 3, 'text': 'Worst customer service ever from @GulPhoneSupport. Avoid this.'},
  {'id': 4, 'text': 'The @GulPhoneSupport team was helpful and resolved my issue. Great service!'},
]

PUNCTUATION_CHARS = '!"#$&\'()*+,-./:;<=>?@[\\]^_`{|}~'
STOPWORDS_SET = {
    'i', 'me', 'my', 'a', 'an', 'the', 'is', 'am', 'was', 'and', 
    'but', 'if', 'or', 'to', 'of', 'at', 'by', 'for', 'with', 'this', 'that'
}
POSITIVE_WORDS_SET = {'love', 'amazing', 'great', 'helpful', 'resolved'}
NEGATIVE_WORDS_SET = {'disaster', 'broken', 'worst', 'avoid', 'bad'}

def preProcessText(text, punctuations, stopWords):
    normalizedText = text.lower()
    without_punctuation = "".join(char for char in normalizedText if char not in punctuations)
    preCleanedWords = without_punctuation.split()
    CleanedWords = [word for word in preCleanedWords if word not in stopWords]
    return CleanedWords

def analyzePosts(postsList, punctuation, stopwords, positive, negative):
    analyzed_posts = []
    cleaned_texts = map(lambda post: preProcessText(post['text'],punctuation,stopwords),postsList)
    for post, cleaned_words in zip(postsList, cleaned_texts):
        score = 0
        for word in cleaned_words:
            if word in positive:
                score += 1
            elif word in negative:
                score -= 1
        analyzed_posts.append({
            'id': post['id'],
            'text': post['text'],
            'processedText': cleaned_words,
            'score': score
        })
    return analyzed_posts

def getFlaggedPosts(scoredPosts, threshold =-1):
    return [post for post in scoredPosts if post['score'] <= threshold]
def findNegativeTopics(flaggedPosts):
    topic_counts = {}
    for post in flaggedPosts:
        words = post['text'].split()
        for word in words:
            if word.startswith('#') or word.startswith('@'):
                cleanedTopic = "".join(char for char in word if char not in PUNCTUATION_CHARS).lower()
                
                count= [cleanedTopic] = topic_counts.get(cleanedTopic, 0) + 1

    return count

scored_posts = analyzePosts(allPosts,PUNCTUATION_CHARS,STOPWORDS_SET,POSITIVE_WORDS_SET,NEGATIVE_WORDS_SET)

print("*Scored Posts*\n")
print(scored_posts)
print("\n")
flaggedposts = getFlaggedPosts(scored_posts, sentimentThreshold=-1)
print("*Flagged Posts*\n")
print(flaggedposts)
print("\n")
negativetopics = findNegativeTopics(flaggedposts)
print("*Negative Topics*\n")
print(negativetopics)