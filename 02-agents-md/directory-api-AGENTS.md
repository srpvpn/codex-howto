# API Module Standards

Use this as a directory-level `AGENTS.md` example for `src/api/`.

This file is intended to override broader repository instructions for everything in `/src/api/`.

## API-specific standards

### Request validation
- Use Zod for schema validation.
- Validate all external input before business logic.
- Return `400` for validation failures with field-level details.

### Authentication
- Require an `Authorization` header for protected endpoints.
- Validate token expiry and refresh behavior explicitly.

### Response format

All success responses should follow a stable envelope:

```json
{
  "success": true,
  "data": {},
  "timestamp": "2026-03-30T00:00:00Z",
  "version": "1.0"
}
```

### Pagination
- Prefer cursor pagination over offset pagination.
- Cap page size at `100`.
- Default page size to `20`.

### Rate limiting
- Return `429` when limits are exceeded.
- Include retry metadata when possible.
