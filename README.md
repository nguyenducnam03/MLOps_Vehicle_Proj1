# 🚗 MLOps Vehicle Insurance Classification Project

This project demonstrates the end-to-end MLOps workflow for a Vehicle Insurance Classification use case. It includes data ingestion, model training, evaluation, and deployment using Docker, GitHub Actions, and AWS services (S3, EC2, ECR).

## 📁 Project Structure  
vehicle-mlops/  
│  
├── src/ # Source code modules  
├── templates/ # HTML templates for app  
├── static/ # Static files (CSS, JS)  
├── notebook/ # Jupyter notebooks and EDA  
├── .github/workflows/ # CI/CD pipeline  
├── app.py # FastAPI/Flask app for prediction  
├── Dockerfile # Docker setup  
├── setup.py, pyproject.toml # Package configuration  
├── requirements.txt  
└── README.md  
## ⚙️ Setup & Run Locally

1. Create and activate conda environment:
   ```bash
   conda create -n vehicle python=3.10 -y
   conda activate vehicle
2. Install dependencies:
    ```bash
     pip install -r requirements.txt
3. Build and run Docker container:
   ```bash
   docker build -t vehicleapp .
   docker run -p 5000:5000 vehicleapp
4. Access the app at http://localhost:5000 (Now only local is available)

If you want to access this website from anywhere, please refer to the CI/CD process and cloud setup (AWS).

For more details, you can follow this great tutorial:
https://www.youtube.com/watch?v=skr08dnWXC8&list=PLupK5DK91flV45dkPXyGViMLtHadRr6sp&index=20
