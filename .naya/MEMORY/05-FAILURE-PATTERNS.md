# FAILURE PATTERNS

This is the reusable failure library.

## RULE

Do not merely record that something failed. Record why it failed and what now prevents recurrence.

## ENTRY TEMPLATE

### FAILURE ID

### FAILURE CLASS

### WHAT FAILED

### ROOT CAUSE

### IMPACT

### IMMEDIATE FIX

### PERMANENT SAFEGUARD

### VERIFICATION

### REPEAT COUNT

### RELATED EXECUTIONS

### STATUS
OPEN / MITIGATED / CLOSED

---

## ACTIVE PATTERNS

### FP-001 — ZERO-CHANGE / FALSE COMPLETION

Known failure class: an AI can describe work as completed without a material change to the authoritative artifact.

Required safeguards:
- authoritative source lock;
- baseline before execution;
- actual artifact modification;
- re-fetch after modification;
- diff inspection;
- requested-delta verification;
- no false completion.

Escalation: four repetitions of the same failure class trigger ROOT-CAUSE LOCKDOWN.
