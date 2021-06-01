from verta import Client
client = Client("http://localhost:3000")

def uploadSerializedObject(proj,exp_name,exp_run,objName,serialization,library):
    proj = client.set_project(proj) 
    expt = client.set_experiment(exp_name) 
    run = client.set_experiment_run(exp_run) 
    run.log_model('./' + objName ,overwrite=True)
    print("Username:", proj)
    print("Experiment:",exp_name)
    print("Experiment Run:", exp_run)
    print("Serialization:", serialization)
    print("Library:",library)


# Input for final-log
# 1. proj
# 2. exp_name
# 3. exp_run
# 4. serialization
# 5. library

uploadSerializedObject("StatusNeo","Experiment","Test Phase 1","finalized_model.pkl","pickle","sklearn")
