from azureml.core import Workspace

ws = Workspace.from_config()


# from azureml.core import Workspace

# ws = Workspace.get(name='aml-workspace',
#                    subscription_id='1234567-abcde-890-fgh...',
#                    resource_group='aml-resources')