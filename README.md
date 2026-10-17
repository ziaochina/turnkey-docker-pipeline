# Turnkey Docker Data Extraction Pipeline

A minimal, hardened Docker scaffold for production web scraping, schema validation, and structured streaming export.

[![Docker](https://img.shields.io/badge/Docker-Production%20Scaffold-2496ED?style=flat&logo=docker&logoColor=white)](https://www.docker.com/)
[![Pydantic](https://img.shields.io/badge/Pydantic-V2-E92063?style=flat&logo=pydantic&logoColor=white)](https://pydantic.dev/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

---

## 🎯 Purpose

Eliminates the "Works on my machine" problem when delivering freelance scraping scripts. Clients simply extract the folder and run `docker compose up`. Zero Python virtualenv headaches, zero system dependency conflicts.

---

## 🚀 Execution

```bash
docker compose up --build
```
Outputs are streamed to `./data/sample_data.csv` in UTF-8 with BOM for native Microsoft Excel compatibility.
