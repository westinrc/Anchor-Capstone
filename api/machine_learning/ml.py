# Derived from http://scikit-learn.org/stable/tutorial/text_analytics/working_with_text_data.html#exercise-2-sentiment-analysis-on-movie-reviews

import sys
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.datasets import load_files
from sklearn.model_selection import train_test_split
from sklearn import metrics


if __name__ == "__main__":
    # NOTE: we put the following in a 'if __name__ == "__main__"' protected
    # block to be able to use a multi-core grid search that also works under
    # Windows, see: http://docs.python.org/library/multiprocessing.html#windows
    # The multiprocessing module is used as the backend of joblib.Parallel
    # that is used when n_jobs != 1 in GridSearchCV

    # the training data folder must be passed as first argument
    patient_data_folder = sys.argv[1]
    test_data_folder = sys.argv[2]
    train_set = load_files(patient_data_folder, shuffle=False)
    print "n_samples: %d" % len(train_set.data)

    # load test data
    test_set = load_files(test_data_folder, shuffle=False)

    # split the dataset in training and test set:
    #docs_train, docs_test, y_train, y_test = train_test_split(
    #    train_set.data, train_set.target, test_size=0.25, random_state=None)

    # vectorizer / classifier pipeline that filters out tokens
    # that are too rare or too frequent
    pipeline = Pipeline([
        ('vect', TfidfVectorizer(min_df=3, max_df=0.95)),
        ('clf', LinearSVC(C=1000)),
    ])

    # grid search to find out whether unigrams or bigrams are
    # more useful.
    # Fit the pipeline on the training set using grid search for the parameters
    parameters = {
        'vect__ngram_range': [(1, 1), (1, 2)],
    }
    grid_search = GridSearchCV(pipeline, parameters, n_jobs=-1)
    grid_search.fit(train_set.data, train_set.target)

    # print the mean and std for each candidate along with the parameter
    # settings for all the candidates explored by grid search.
    n_candidates = len(grid_search.cv_results_['params'])
    for i in range(n_candidates):
        print(i, 'params - %s; mean - %0.2f; std - %0.2f'
              % (grid_search.cv_results_['params'][i],
                 grid_search.cv_results_['mean_test_score'][i],
                 grid_search.cv_results_['std_test_score'][i]))

    # Predict the outcome on the testing set and store it in a variable
    # named y_predicted
    y_predicted = grid_search.predict(test_set.data)

    # Print the classification report
    print(metrics.classification_report(test_set.target, y_predicted,
                                        target_names=train_set.target_names))

    # Print and plot the confusion matrix
    cm = metrics.confusion_matrix(test_set.target, y_predicted)
    print(cm)
