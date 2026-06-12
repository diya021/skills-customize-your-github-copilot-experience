# Assignment Guide

This reference document provides guidance for registering and managing assignments in the repository.

## Purpose

- Explain how to add a new assignment to `config.json`
- Describe how attachments should be registered
- Document the expected assignment metadata format

## Assignment metadata example

```json
{
  "id": "new-assignment",
  "title": "New Assignment",
  "description": "A short description of the assignment",
  "path": "assignments/new-assignment",
  "dueDate": "2026-07-01"
}
```

## Attachment example

```json
{
  "name": "Starter Code",
  "file": "starter-code.py",
  "type": "python"
}
```

## Scripts

- `scripts/update-config.js` registers new assignments in `config.json`
- `scripts/add-attachment.js` attaches files to existing assignments
