# Deployment status

- [x] ADF ARM resource template and parameters extracted from the supplied ZIP.
- [x] Secret parameters blanked in the public parameters file.
- [x] Metadata-driven `relativeUrl` expression corrected in deployment template.
- [x] Azure DevOps pipeline YAML added.
- [x] Static ARM JSON validation script added.
- [ ] Configure Azure DevOps service connection and secret variable group.
- [ ] Run CI/CD against the intended Azure resource group.
- [ ] Run live ADF pipeline and inspect storage outputs/audit rows.
- [ ] Add actual Databricks notebooks and LLM/RAG code; they are not in the uploaded ADF export.
- [ ] Test complete ADF → ADLS → Databricks → Gold → RAG path.
