# Duties and Responsibilities for Semiconductor Wafer Defect Classifier Agent

## Dual-Control Architecture
Maker:
wafer-pattern-recognizer

Checker:
fab-yield-checker

## Operational Workflow
1. The Maker (wafer-pattern-recognizer) analyzes incoming telemetry, context, and requirements.
2. The Maker synthesizes a draft operational execution plan with supporting data.
3. The Checker (fab-yield-checker) independently verifies all assumptions and constraints.
4. If validation passes, the plan is signed, logged, and committed.
5. All actions are appended to the immutable governance audit trail.
