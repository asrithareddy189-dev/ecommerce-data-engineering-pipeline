# Azure DevOps variable group example

Create a variable group named for this project and map these names exactly. Mark all key/password/connection-string variables as secret. Do not commit the real values.

- `AZURE_SERVICE_CONNECTION` (non-secret name of the ARM service connection)
- `AZURE_SUBSCRIPTION_ID`
- `STORAGE_ACCOUNT_NAME`
- `AZURE_SQL_SERVER`
- `AZURE_SQL_DATABASE`
- `AZURE_SQL_USERNAME`
- `LS_ADLS_GEN2_ACCOUNT_KEY` (secret)
- `LS_AZURESQL_METADATA_PASSWORD` (secret)
- `AZURESQLDATABASE1_PASSWORD` (secret; legacy linked service)
- `AZUREBLOBSTORAGE1_CONNECTIONSTRING` (secret; legacy linked service)
- `AZUREBLOBSTORAGE2_CONNECTIONSTRING` (secret; legacy linked service)
- `AZUREBLOBSTORAGE3_CONNECTIONSTRING` (secret; legacy linked service)
- `AZUREBLOBSTORAGE4_CONNECTIONSTRING` (secret; legacy linked service)
