Specification
Overview
The Reminder Agent converts natural language reminders into structured JSON output.

Output Schema
{ "intent": "create_reminder", "task": "string", "datetime": "string", "confidence": "number" }

Functional Requirements
FR-1 Intent Detection
Identify reminder requests.

FR-2 Task Extraction
Extract task description.

FR-3 Date Extraction
Extract date information.

FR-4 Time Extraction
Extract time information.

FR-5 Schema Validation
Output must match schema.
