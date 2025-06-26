from strategy import run_strategy
from ml_model import run_ml_model

def job():
    print("Running strategy...")
    run_strategy()
    print("Running ML model...")
    run_ml_model()
    print("Job completed.")

if __name__ == "__main__":
    print("🚀 Starting one-time run...")
    job()  # Run once for testing/demo
