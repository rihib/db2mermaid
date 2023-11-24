# DB2mermaid

**NOTE: This package is not full. It cannot generate table relation, can only generate table definition.**
[DB2mermaid](https://pypi.org/project/DB2mermaid/) is a tool to generate [mermaid](https://mermaid-js.github.io/mermaid/#/) diagrams from a database schema.

## Requirements

- Python3.10
- sqlalchemy
- [mysqlclient](https://pypi.org/project/mysqlclient/)
- your MySQL database

## Installation

Create a `.env` file with a copy of `.env.example` and replace the constant values with appropriate ones.

```bash
% brew install mysql pkg-config
% python3 -m venv .venv
% source .venv/bin/activate
% python3 -m pip install -r requirements.txt
```

## Usage

`er.md` will be generated.

```bash
% python3 main.py
```
