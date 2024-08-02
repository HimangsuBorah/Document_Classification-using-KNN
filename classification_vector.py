from sklearn.neighbors import KNeighborsClassifier
from sklearn.feature_extraction.text import TfidfVectorizer


def vectorize_text(X_train,X_test):
    vectorizer=TfidfVectorizer()
    X_train_vec=vectorizer.fit_transform(X_train)
    X_test_vec=vectorizer.fit_transform(X_test)
    return X_train_vec,X_test_vec

def k_nearest_neighbour(X_train,y_train,X_test,k):
    knn_classifer = KNeighborsClassifier(n_neighbors=k)
    knn_classifer.fit(X_train,y_train)
    y_pred= knn_classifer(X_test)
    return y_pred