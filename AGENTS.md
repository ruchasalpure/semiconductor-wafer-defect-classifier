# Multi-Agent Coordination Specification

## Assigned Roles
Maker:
wafer-pattern-recognizer

Checker:
fab-yield-checker

## Coordination Protocol
- **Primary Agent**: semiconductor-wafer-defect-classifier
- **Governance Standard**: OpenGAP Dual-Agent Control Framework v0.1.0
- **Consensus Threshold**: 100% agreement between Maker and Checker before state mutations.
- **Fail-safe Mode**: If verification fails, transaction rolls back and alerts human supervisor.
