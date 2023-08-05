import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler, MaxAbsScaler, RobustScaler, Normalizer
#from rate import rate_scalers, create_scaler_charts


def preprocess (fpath: str):
    data_raw = pd.read_csv(fpath, index_col=[0])

    data_preprocessed_dict = {
        "data_preprocessed": pd.DataFrame,
        "X": pd.DataFrame,
        "Y": pd.DataFrame,
    }

    replacements = {
        "индивидуальное жилищное строительство": 1,
        "садоводство": 0,
        "кирпич": 1,
        "дерево": 2,
        "блок": 3,
        "монолит-кирпич": 4,
        "монолит": 5,
    }
    
    data_preprocessed = data_raw.replace(replacements)

    data_preprocessed_dict["data_preprocessed"] = data_preprocessed
    data_preprocessed_dict["Y"] = data_preprocessed["price"]

    # scalers = {
    # "MinMaxScaler": MinMaxScaler,
    # "StandardScaler": StandardScaler,
    # "MaxAbsScaler": MaxAbsScaler, 
    # "RobustScaler": RobustScaler,
    # "Normalizer": Normalizer
    # }

    # score_scalers = rate_scalers(scalers, X=X_raw)
    # create_scaler_charts(score_scalers, X_raw)

    X_raw = data_preprocessed.iloc[:, 1:]
    scaler = MinMaxScaler().fit(X_raw)
    X_preprocessed = pd.DataFrame(data=scaler.transform(X_raw), columns=X_raw.columns)
    
    data_preprocessed_dict["X"] = X_preprocessed

    return data_preprocessed_dict
    
    