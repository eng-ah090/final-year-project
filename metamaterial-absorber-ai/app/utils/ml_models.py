def build_default_regressor(random_state: int = 42):
    from sklearn.ensemble import RandomForestRegressor

    return RandomForestRegressor(n_estimators=100, random_state=random_state)
