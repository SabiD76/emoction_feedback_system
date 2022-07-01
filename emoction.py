from textblob import TextBlob   //pip install TextBlob

feedback1="The boy is good"
feedback2="you are so bad"

blob=TextBlob(feedback1)

blob2= TextBlob(feedback2)

print(blob.sentiment) 
print(blob2.sentiment)
