# E-commerce Data Engineering Pipeline (ADF + ADLS + Databricks + RAG)

This repository is the deployment starting point built from the ADF ARM export supplied for the existing `datafactorylearning2` factory. The export has been inspected and the metadata-driven pipeline's REST dataset parameter was corrected in the deployment copy to use `@item().RelativeUrl` rather than the exported literal `users`.

## Current scope represented here

- Azure Data Factory REST ingestion for customers (`users`), orders (`carts`), and products (`products`).
- Metadata-driven ingestion from `dbo.IngestionMetadata` into ADLS Gen2 landing paths.
- ADF ARM-template deployment through Azure DevOps YAML.
- ADF template structural validation.

Databricks transformation notebooks, SCD logic, the LLM/RAG application, and any Databricks job/API orchestration are not included in the ARM export that was provided. Add the actual existing source files to `databricks/` and `rag/` before claiming they are deployed from this repository. Empty directories are placeholders only.

## Repository layout

```text
adf/
  deploy/ARMTemplateForFactory.json
  deploy/ARMTemplateParametersForFactory.json
  validate_arm.py
azure-devops/azure-pipelines-adf.yml
sql/01_ingestion_metadata.sql
docs/ADF_EXPORT_REVIEW.md
docs/adf-resource-inventory.json
databricks/   # add the real saved notebooks/source here
rag/          # add the real LLM/RAG source here
```

## Before running CI/CD

1. Push this repository to GitHub and connect it to an Azure DevOps pipeline.
2. Create an Azure Resource Manager service connection named in the pipeline variable `AZURE_SERVICE_CONNECTION`, with permissions to deploy to the existing resource group.
3. Configure a secret variable group or pipeline variables for the required credentials. Never commit credentials to Git.
4. Provide these variables: `AZURE_SUBSCRIPTION_ID`, `AZURE_SERVICE_CONNECTION`, `STORAGE_ACCOUNT_NAME`, `AZURE_SQL_SERVER`, `AZURE_SQL_DATABASE`, `AZURE_SQL_USERNAME`, `LS_ADLS_GEN2_ACCOUNT_KEY`, `LS_AZURESQL_METADATA_PASSWORD`, plus the four `AZUREBLOBSTORAGE*_CONNECTIONSTRING` values and `AZURESQLDATABASE1_PASSWORD` needed by legacy resources that remain in the export.
5. Review the SQL usernames/server/database variables. This project export contains legacy linked services in addition to the three active metadata-ingestion linked services; the pipeline deploys the entire exported child-resource template, so all corresponding parameters must be valid.
6. Run `python adf/validate_arm.py` locally before pushing.
7. Run the pipeline only after the parameters are configured and you have reviewed the target environment. The YAML uses Incremental deployment to an **existing** resource group/factory; it does not create a Databricks workspace.

## Important limitations

- A successful ARM deployment is not proof the ADF pipeline can access every endpoint; run an ADF pipeline and inspect activity outputs after deployment.
- The public parameters file deliberately has blank secret values and placeholders for environment-specific settings. CI/CD provides them at deployment time.
- The supplied ARM export does not contain the Databricks notebooks, LLM/RAG code, or an end-to-end ADF-to-Databricks job trigger.
- The supplied ARM export has no ADF trigger resource. The metadata-driven pipeline is therefore not scheduled by a trigger in this export.
- The dataset parameter correction in this deploy copy is intentional. `docs/ADF_EXPORT_REVIEW.md` records the finding.
