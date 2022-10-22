import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn import tree
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import GradientBoostingClassifier

from sklearn.model_selection import train_test_split  # hold out
from sklearn.model_selection import cross_val_score  # cross-validation

from warnings import filterwarnings

filterwarnings('ignore')


def cross_validation(name, classifier, X, y, k):
	# cross-validation k-folds
	folds = k
	scoresAccuracy = cross_val_score(classifier, X, y, cv=folds, scoring='accuracy')
	scoresPrecision = cross_val_score(classifier, X, y, cv=folds, scoring='precision_macro')
	scoresRecall = cross_val_score(classifier, X, y, cv=folds, scoring='recall_macro')
	scoresF1 = cross_val_score(classifier, X, y, cv=folds, scoring='f1_macro')
	print('--Classificator--')
	print(f'The classificator is: {name}')
	print("%0.4f accuracy with a standard deviation of %0.4f" % (scoresAccuracy.mean(), scoresAccuracy.std()))
	print("%0.4f precision with a standard deviation of %0.4f" % (scoresPrecision.mean(), scoresPrecision.std()))
	print("%0.4f recall with a standard deviation of %0.4f" % (scoresRecall.mean(), scoresRecall.std()))
	print("%0.4f F1 with a standard deviation of %0.4f" % (scoresF1.mean(), scoresF1.std()))
	
	results = [[scoresAccuracy.mean(), scoresAccuracy.std()],
	           [scoresPrecision.mean(), scoresPrecision.std()],
	           [scoresRecall.mean(), scoresRecall.std()],
	           [scoresF1.mean(), scoresF1.std()]]
	filename = name + '_results.txt'
	
	np.savetxt(filename, results, fmt='%0.4f')


def mlpclassificator(X, y, folds):
	# ---------------------------------- MLP ------------------------------------------
	# solver{‘lbfgs’, ‘sgd’, ‘adam’}, default=’adam’
	# activation{‘identity’, ‘logistic’, ‘tanh’, ‘relu’}, default=’relu’
	mlp = MLPClassifier(solver='sgd', alpha=0.0001, hidden_layer_sizes=(128,), random_state=1,
	                    learning_rate='constant', learning_rate_init=0.1, max_iter=1000,
	                    activation='tanh', momentum=0.9, verbose=False,
	                    tol=0.0001)  # tol=0.0001  learning_rate='constant'
	
	# hold out with 30% of data for test
	X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size=0.4, random_state=1)
	
	# cross-validation
	cross_validation('MLP', mlp, X_treino, y_treino, folds)
	
	# train of MLP
	mlp.fit(X_treino, y_treino)
	# test of MLP
	saidas = mlp.predict(X_teste)
	print('-----------------------------------------------------------')
	print('Saída da rede:\t', saidas)
	print('Saída desejada:\t', y_teste)
	print('-----------------------------------------------------------')
	print('Score: ', (saidas == y_teste).sum() / len(X_teste))
	print('MLP, hold out: ', mlp.score(X_teste, y_teste))


def knnclassificator(X, y, folds):
	# -------------------- KNN -------------------------------------------------
	knn = KNeighborsClassifier(algorithm='auto', leaf_size=30, metric='euclidean',
	                           metric_params=None, n_jobs=1, n_neighbors=2, p=2,
	                           weights='uniform')
	
	X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size=0.3, random_state=1)
	cross_validation('KNN', knn, X_treino, y_treino, folds)
	knn.fit(X_treino, y_treino)
	knn.predict(X_teste)
	acuracia = knn.score(X_teste, y_teste)
	
	print('-----------------------------------------------------------')
	print('KNN, Hold out, Acc = ', acuracia)
	print('-----------------------------------------------------------')


def svmclassificator(X, y, folds):
	# ------------------- SVM ---------------------------------------------------
	# svm = SVC(gamma='auto') # https://scikit-learn.org/stable/auto_examples/svm/plot_rbf_parameters.html
	# svm.fit(X, y)
	# For choosing C we generally choose the value like 0.001, 0.01, 0.1, 1, 10, 100
	#  for Gamma 0.001, 0.01, 0.1, 1, 10, 100  #  https://medium.com/@myselfaman12345/c-and-gamma-in-svm-e6cee48626be
	
	svm = SVC(C=100.0, cache_size=200, class_weight=None, coef0=0.0,
	          decision_function_shape='ovr', degree=3, gamma=1.0, kernel='rbf',
	          max_iter=500, probability=False, random_state=1, shrinking=True,
	          tol=0.001, verbose=False)
	
	X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size=0.3, random_state=1)
	cross_validation('SVM', svm, X_treino, y_treino, folds)
	svm.fit(X_treino, y_treino)
	svm.predict(X_teste)
	acuracia = svm.score(X_teste, y_teste)
	
	print('-----------------------------------------------------------')
	print('SVM, Hold out, Acc = ', acuracia)
	print('-----------------------------------------------------------')


def ramdomForestClassificator(X, y, folds):
	# -------------------- Random Forest --------------------------------
	
	rf = RandomForestClassifier(n_estimators=256, max_depth=8, random_state=0)
	# RandomForestClassifier(bootstrap=True, class_weight=None, criterion='gini',
	#             max_depth=None, max_features='auto', max_leaf_nodes=None,
	#             min_impurity_decrease=0.0, min_impurity_split=None,
	#             min_samples_leaf=1, min_samples_split=2,
	#             min_weight_fraction_leaf=0.0, n_estimators=100, n_jobs=1,
	#             oob_score=False, random_state=None, verbose=0,
	#             warm_start=False)
	
	cross_validation('RF', rf, X, y, folds)
	X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size=0.3, random_state=1)
	rf.fit(X_treino, y_treino)
	rf.predict(X_teste)
	acuracia = rf.score(X_teste, y_teste)
	
	print('-----------------------------------------------------------')
	print('Random Forest, Hold out, Acc = ', acuracia)
	print('-----------------------------------------------------------')


def naivesBayesClassificator(X, y, folds):
	# --------------------- Gaussian Naive Bayes -------------------------
	X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size=0.3, random_state=1)
	gnb = GaussianNB()
	cross_validation('GNB', gnb, X, y, folds)
	y_pred = gnb.fit(X_treino, y_treino).predict(X_teste)
	
	acuracia = gnb.score(X, y)
	
	print('-----------------------------------------------------------')
	print('Gaussian Naive Bayes, Hold out, Acc = ', acuracia)
	print('-----------------------------------------------------------')


def dicisionTreeClassificator(X, y, folds):
	# --------------------- Decision Tree --------------------------------
	X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size=0.3, random_state=1)
	dt = tree.DecisionTreeClassifier()
	cross_validation('DT', dt, X, y, folds)
	dt_pred = dt.fit(X_treino, y_treino).predict(X_teste)
	
	acuracia = dt.score(X, y)
	
	print('-----------------------------------------------------------')
	print('Decision Tree, Hold out, Acc = ', acuracia)
	print('-----------------------------------------------------------')


def extraTreeClassificator(X, y, folds):
	# --------------------- Extra Tree --------------------------------
	et = ExtraTreesClassifier(n_estimators=10, max_depth=8, min_samples_split=2, random_state=0)
	cross_validation('ET', et, X, y, folds)
	X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size=0.3, random_state=1)
	et.fit(X_treino, y_treino)
	et.predict(X_teste)
	acuracia = et.score(X_teste, y_teste)
	
	print('-----------------------------------------------------------')
	print('Extra Tree, Hold out, Acc = ', acuracia)
	print('-----------------------------------------------------------')


def adaBoostClassificator(X, y, folds):
	# ----------------------- ADA Boost -------------------------------
	# ad = AdaBoostClassifier(n_estimators=10, algorithm="SAMME.R", random_state=1)  # binary
	ad = AdaBoostClassifier(tree.DecisionTreeClassifier(max_depth=8), n_estimators=256,
	                        learning_rate=0.01)  # multiclass
	cross_validation('AD', ad, X, y, folds)
	# scores = cross_val_score(clf, X, y, cv=5)
	# scores.mean()
	X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size=0.3, random_state=1)
	ad.fit(X_treino, y_treino)
	ad.predict(X_teste)
	acuracia = ad.score(X_teste, y_teste)
	
	print('-----------------------------------------------------------')
	print('ADA Boost, Hold out, Acc = ', acuracia)
	print('-----------------------------------------------------------')


def gradienteBooClassificator(X, y, folds):
	# ---------------------- Gradient Boosting -------------------------
	gb = GradientBoostingClassifier(n_estimators=10, learning_rate=0.1,
	                                max_depth=8, random_state=1)
	
	cross_validation('GB', gb, X, y, folds)
	X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size=0.3, random_state=1)
	gb.fit(X_treino, y_treino)
	
	acuracia = gb.score(X_teste, y_teste)
	
	print('-----------------------------------------------------------')
	print('Gradient Boosting, Hold out, Acc = ', acuracia)
	print('-----------------------------------------------------------')