# We will be defining our model params and random search CV params
# We have done hyperparameter tuning of random forest in Jupyter notebook
# We here are doing hyperparameter tuning of lightGBM 

from scipy.stats import randint, uniform

LIGHTGM_PARAMS = {
    'n_estimators': randint(100, 500),
    'max_depth': randint(5, 50),
    'learning_rate': uniform(0.01, 0.2),
    'num_leaves': randint(20, 100),
    'boosting_type': ['gbdt', 'dart', 'goss']
}

RANDOM_SEARCH_PARAMS = {
    'n_iter': 4, # 4 for faster training
    'cv': 2, # This has to be >1
    'n_jobs': -1,
    'verbose': 2,
    'random_state': 42,
    'scoring': 'accuracy'
}