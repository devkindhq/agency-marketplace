# Agency Marketplace

A domain-based Claude Code plugin marketplace. Each domain is a plugin, each skill lives inside it.

## Structure

```
plugins/
└── seo/
    └── skills/
        └── google-qrg/   ← Google Quality Rater Guidelines
```

---

## Install

### Option 1 — From GitHub (recommended)

```bash
claude plugin marketplace add devkindhq/agency-marketplace
claude plugin install seo@agency-marketplace
```

### Option 2 — Local clone

```bash
git clone git@github.com:devkindhq/agency-marketplace.git
cd agency-marketplace
./install.sh
```

---

## Update

Pull the latest skills and refresh:

```bash
claude plugin marketplace update agency-marketplace
```

---

## Domains & Skills

| Domain | Skill | Description |
|--------|-------|-------------|
| `seo` | `google-qrg` | Evaluate content against Google's Search Quality Rater Guidelines (E-E-A-T, PQ, NM) |
