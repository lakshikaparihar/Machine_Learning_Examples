FROM nishkarshraj/mlops-ubuntu
COPY model_dir/ /opt/ml/model
                RUN python -c                 'from mlflow.models.container import _install_pyfunc_deps;                _install_pyfunc_deps("/opt/ml/model", install_mlflow=False)'
                ENV MLFLOW_DISABLE_ENV_CREATION="true"
ENTRYPOINT ["python", "-c", "from mlflow.models import container as C; C._serve()"]
