
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load sample data
X, y = load_iris(return_X_y=True)

# Train model
model = RandomForestClassifier().fit(X, y)

# Save the model
joblib.dump(model, "model.pkl")
print("model.pkl saved.")
