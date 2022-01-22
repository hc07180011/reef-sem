import numpy as np
import pandas as pd


def _preprocessing(df: pd.DataFrame) -> pd.DataFrame:
    """Do the preprocessing of the input data

    Args:
        df (pd.DataFrame): input DataFrame

    Returns:
        pd.DataFrame: output DataFrame
    """

    # Replace all NAN to -1
    df.replace(np.NaN, -1, inplace=True)

    # One-hot encoding and to numeric
    for col in df.columns:
        if df[col].dtypes == object:
            # print(pd.get_dummies(df[col]))
            print(df[col])
            try:
                df[col] = df[col].astype(np.float64)
            except Exception as e:
                print("cannot convert: {}".format(repr(e)))

    return df


def _main() -> None:
    df = pd.read_csv("data.csv")
    
    df = _preprocessing(df)
    print(df.columns)
    print(df)


if __name__ == "__main__":
    _main()
