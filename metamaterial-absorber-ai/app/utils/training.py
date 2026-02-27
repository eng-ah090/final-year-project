def train_regressor(model, x_train, y_train):
    model.fit(x_train, y_train)
    return model
