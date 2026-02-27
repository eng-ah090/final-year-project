import numpy as np

from app.utils.ml_models import build_default_regressor
from app.utils.model_io import save_model
from app.utils.training import train_regressor


def main() -> None:
    x = np.random.rand(200, 3)
    y = 0.5 * x[:, 0] + 0.3 * x[:, 1] - 0.2 * x[:, 2]
    model = build_default_regressor()
    model = train_regressor(model, x, y)
    save_model(model, "models/default_regressor.joblib")
    print("Model trained and saved.")


if __name__ == "__main__":
    main()
