# azureml-core of version 1.0.72 or higher is required
# azureml-dataprep[pandas] of version 1.1.34 or higher is required
from azureml.core import Workspace, Dataset

subscription_id = '16f263d1-840b-4414-8415-243b4662d595'
resource_group = 'packt-azureml-rg'
workspace_name = 'ml-demo3-ws'

workspace = Workspace(subscription_id, resource_group, workspace_name)

dataset = Dataset.get_by_name(workspace, name='survey-drift-target')
dataset.to_pandas_dataframe()
