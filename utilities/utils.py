import pandas as pd
import numpy as np

class Util:

    class NaN:
        # dict['Feature'] = % of samples containing NaN for feature
        def get_nan_features_dict(dataframe: pd.DataFrame) -> dict:
            samples_ct = len(dataframe)
            NaN_features = {}
            for feature in dataframe.columns:
                samples_NaNs = dataframe[feature].isna()
                if True in samples_NaNs.unique():
                    percentage = np.round(samples_NaNs.sum() / samples_ct,4)
                    NaN_features[feature] = percentage
            return NaN_features

        def contains_NaN(dataframe, column) -> bool:
            dataframe.dropna(eaf)
            try:
                return dataframe[column].isnull().values.any()
            except:
                raise KeyError(f"Likely {column} not in dataframe.")


    class Normalize:
        def get_min_max(x: float, min_x: float, max_x: float) -> float:
            normalized_x = (x - min_x) / (max_x - min_x)
            return normalized_x
