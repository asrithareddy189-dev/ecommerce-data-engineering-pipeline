# ADF export review

Reviewed `ARMTemplateForFactory.json` and its matching parameter file from the uploaded export.

## Present in export

- 10 pipelines, including `PL_Metadata_Driven_Ingestion` and the three API-specific pipelines.
- Linked services include `LS_REST_DummyJSON`, `LS_ADLS_Gen2`, and `LS_AzureSQL_Metadata`, plus several legacy/example linked services.
- The metadata-driven pipeline queries `dbo.IngestionMetadata`, loops through rows, writes to `@item().DestinationPath`, performs a `Lookup_Watermark`, and invokes `dbo.usp_LogIngestion` after a successful copy.
- `DS_WatermarkControl` is present.

## Findings to address before claiming full end-to-end completion

1. **REST relative URL in exported pipeline:** the uploaded export wired `DS_REST_Generic.relativeUrl` to the literal `users`. The deployment copy fixes it to the metadata row expression `@item().RelativeUrl`. Verify the live pipeline is saved/published with the same expression.
2. **Watermark update is absent from this pipeline export:** the pipeline performs a watermark lookup, but no `usp_UpdateWatermark` activity is present in the exported activity graph. The query result also is not used to filter the DummyJSON source. Treat true incremental extraction as not implemented by this exported flow.
3. **Success logging only:** `Log_Success` runs after a successful copy, but the export contains no failure logging branch for the copy activity. The user previously reported `dbo.IngestionAudit` had zero rows; verify the stored procedure parameter mapping and database after deployment.
4. **Orchestration:** no trigger resource appears in the exported ADF template, and there is no Databricks activity/job invocation in the metadata pipeline. This export alone does not establish automated ADF → Databricks → Gold execution.
5. **SCD and RAG:** these are not represented in the ADF export; verify actual saved notebook/app source separately and include it in the Git repository before advertising it as deployed.
6. **Legacy resources:** the template contains pipelines such as `pipeline1`, `pipeline2`, `pipeline4`, `pipeline6`, `pipeline7`, and `pipeline8`, plus old linked services. Review whether they are required before deleting any of them.

Structural JSON validation does not validate live Azure credentials, permissions, stored procedure behavior, or the final deployment.
