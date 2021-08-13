# Input
# 1. Project Name or Project ID
# 2. Experiment Name
# 3. Experiment Run
# 4. Serialization - Which file to pick from Experiment Run
#	* Example: Pickle - model.pkl
# 5. Library - sklearn - mlflow.log_sklearn()	
# 6. Registered Model Name

from verta import Client
import pickle
import mlflow
import mlflow.sklearn
from mlflow.tracking import MlflowClient
import os

def downloadArtifact(proj,exp_name,exp_run, serialization):
    client = Client("http://localhost:3000")
    proj = client.set_project(proj)
    expt = client.set_experiment(exp_name) 
    run = client.set_experiment_run(exp_run)
    if serialization.lower() == 'pickle':
        run.download_model('model.pkl')
    
def logModel(library, modelName):
    infile = open('./model.pkl','rb')
    model = pickle.load(infile)
    print ('Loaded Model')
    infile.close()
    mlflow.set_tracking_uri("sqlite:///mlruns.db")
    if library.lower() == 'sklearn':
        mlflow.sklearn.log_model (model, "logistic-regression",registered_model_name=modelName)
    client = MlflowClient()
    client.transition_model_version_stage(
    name=modelName,
    version=1,
    stage="Production"
    )
    print ('Logged model')
    
def serveModel(modelName):
    os.environ["MLFLOW_TRACKING_URI"]="sqlite:///mlruns.db"
    os.system("mlflow models serve -m models:/LogisticRegression/production -p 2000 --no-conda")

# Function Calls
downloadArtifact("StatusNeo","Experiment","Test Phase 1","PickLe")
logModel("sklearn","LogisticRegression")
serveModel("LogisticRegression")

