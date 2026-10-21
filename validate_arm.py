#!/usr/bin/env python3
"""Local structural checks for the exported Azure Data Factory ARM template."""
import json, pathlib, sys
base = pathlib.Path(__file__).resolve().parents[1]
template_path = base / "adf" / "deploy" / "ARMTemplateForFactory.json"
params_path = base / "adf" / "deploy" / "ARMTemplateParametersForFactory.json"
errors=[]
try:
    template=json.loads(template_path.read_text(encoding="utf-8"))
    params=json.loads(params_path.read_text(encoding="utf-8"))
except Exception as e:
    print(f"ERROR: Cannot parse deployment JSON: {e}")
    sys.exit(1)
resources=template.get("resources", [])
required=["PL_Metadata_Driven_Ingestion","PL_API_Customers_To_ADLS","PL_API_Orders_To_ADLS","PL_API_Products_To_ADLS"]
all_json=json.dumps(resources)
for name in required:
    if name not in all_json: errors.append(f"Required pipeline missing: {name}")
if "@item().RelativeUrl" not in all_json:
    errors.append("Metadata-driven copy is not using @item().RelativeUrl")
if "@item().DestinationPath" not in all_json:
    errors.append("Metadata-driven sink is not using @item().DestinationPath")
# Template parameters must exist in the parameter file.
expected=set(template.get("parameters",{}))
provided=set(params.get("parameters",{}))
for name in sorted(expected-provided): errors.append(f"Parameter missing in parameters file: {name}")
# The public template must not have committed secret literals.
for name in ["LS_ADLS_Gen2_accountKey","LS_AzureSQL_Metadata_password","AzureSqlDatabase1_password"]:
    if params.get("parameters",{}).get(name,{}).get("value") not in ("", None):
        errors.append(f"Secret parameter must remain blank in repo: {name}")
if errors:
    print("ADF template validation FAILED:")
    for err in errors: print(f" - {err}")
    sys.exit(1)
print("ADF template JSON validation passed.")
print(f"Resources in template: {len(resources)}")
print("Note: structural validation does not test Azure credentials or live deployment.")
