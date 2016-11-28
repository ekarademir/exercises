from sklearn.datasets import fetch_20newsgroups

# load twenty newsgroups from the
# categories we want to fetch
categories = ['alt.atheism', 'soc.religion.christian', 'comp.graphics', 'sci.med']
twenty_train = fetch_20newsgroups(subset='train', categories=categories, shuffle = True, random_state=42)

############ PART ONE ###############################
# # returned dataset is a scikit-learn bunch. An object for datasets
#
# # target_names holds the list of requested category names
# print(twenty_train.target_names)
#
# # the files are loaded into data and filenames are available for reference
# print(len(twenty_train.data))
# print(len(twenty_train.filenames))
#
# # first three lines of the loaded file
# print("\n".join(twenty_train.data[0].split("\n")[:3]))
#
# print(twenty_train.target_names[twenty_train.target[0]])
#
# for t in twenty_train.target[:10]:
#     print(twenty_train.target_names[t])
############### PART TWO #################
# Tokenizing
from sklearn.feature_extraction.text import CountVectorizer

# CountVectorizer transforms words into ngrams
count_vect = CountVectorizer()

X_train_counts = count_vect.fit_transform(twenty_train.data)

print(X_train_counts.shape)

# now we have a feature index
print(count_vect.vocabulary_.get(u'algorithm'))

# term frequency (tf) normalized the ocurance of a word
# with respect to the document size.
# another normalization is to scale down the words that
# all documents have so that we have a set of words
# that can characterize the document. this is called
# Term Frequency times Inverse Document Frequency (tf-idf)
#
# tf and tf-idf are computed as follows
from sklearn.feature_extraction.text import TfidfTransformer
tf_transformer = TfidfTransformer(use_idf=False).fit(X_train_counts)
X_train_tfidf = tf_transformer.transform(X_train_counts)

print(X_train_tfidf.shape)

# Classifier training

from sklearn.naive_bayes import MultinomialNB
clf = MultinomialNB().fit(X_train_tfidf, twenty_train.target)

docs_new = ['GOd is love', 'OpenGL on the GPU is fast']
X_new_counts = count_vect.transform(docs_new)
X_new_tfidf = tf_transformer.transform(X_new_counts)

predicted = clf.predict(X_new_tfidf)

for doc,category in zip(docs_new, predicted):
    print('%r => %s' % (doc,twenty_train.target_names[category]))


#PIPELINE

from sklearn.pipeline import Pipeline

text_clf = Pipeline([('vect', CountVectorizer()),
                     ('tfidf', TfidfTransformer()),
                     ('clf', MultinomialNB())])

text_clf = text_clf.fit(twenty_train.data, twenty_train.target)

import numpy as np
twenty_test = fetch_20newsgroups(subset = 'test', \
    categories = categories, shuffle = True, random_state=42)

docs_test = twenty_test.data
predicted = text_clf.predict(docs_test)
print(np.mean(predicted == twenty_test.target))

from sklearn.linear_model import SGDClassifier
text_clf = Pipeline([('vect', CountVectorizer()),
                     ('tfidf', TfidfTransformer()),
                     ('clf', SGDClassifier(loss='hinge', penalty='l2',
                                           alpha=1e-3, n_iter=5, random_state=42)),
])
_ = text_clf.fit(twenty_train.data, twenty_train.target)
predicted = text_clf.predict(docs_test)
print(np.mean(predicted == twenty_test.target))

from sklearn import metrics
print(metrics.classification_report(twenty_test.target, predicted,
    target_names=twenty_test.target_names))

print(metrics.confusion_matrix(twenty_test.target, predicted))
