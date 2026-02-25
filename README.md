# Credit Risk Prediction API (MLOps)

This project is a machine learning microservice that predicts credit risk based on user financial data.

##  Features
- **Machine Learning**: Scikit-Learn RandomForest model.
- **API**: FastAPI for high-performance inference.
- **Containerisation**: Fully Dockerised for "Zero-Configuration" deployment.

##  How to Run
Ensure you have Docker installed, then run:

```bash
# Build the image
docker build -t credit-risk .

# Run the container
docker run -p 8000:8000 credit-risk