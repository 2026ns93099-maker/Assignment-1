Reflection:
1. How did Spec-Driven Development help?
Spec-Driven Development helped by defining requirements before implementation. Creating the constitution, specification, clarification, plan and task artifacts reduced ambiguity and provided a structured development approach.

2. What issues were identified through harness validation?
For Part-1A, validation identified that empty task titles were accepted without validation. For Part-1B, evaluation identified that the reminder agent did not request clarification when date and time information were missing.

3. How were the issues resolved?
For Part-1A, input validation was added to reject empty task titles. For Part-1B, reminder handling rules were updated to require clarification for incomplete scheduling requests.

4. What was learned about deterministic and non-deterministic validation?
Deterministic systems can be verified through unit tests and expected outputs, while non-deterministic systems require schema validation, property checks and semantic evaluation because outputs may vary.

5. What would be improved in future iterations?
Future improvements would include additional automated tests, expanded evaluation datasets, integration with external services and stronger validation coverage for edge cases.
