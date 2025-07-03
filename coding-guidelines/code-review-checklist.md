# Python Code Review Checklist

## General

- Are the input files / documents released for review? When reviewing a Pull Request this is impicitly the case?
- If it is a review for release, are the version informations in pyproject.toml conf.py up to date?
- If applicable: Is pyproject.toml filled correctly and build process working?

## Code Quality

- Are there no pylint errors or warnings?

## Dcoumentation

- Are docstrings containing descriptions for all parameters and return value?
- Is there a README.MD that contains this minimum information:
  - Overview: description of the purpose?
  - Usage: details about the usage of the library or application?

## Command line tools

- Is there a help option that views details about usage?
- Is there a potion to view the version information?

## Additional review items for tools that needs to be qualified

This review items are mandatory only when developing a tool that is in the context of a safety or security project, but recommended for all
tools with higher quality standards.

- Are there requirements about the functionality of the tool?
- Is there a Software Architecture, describing the high level strucure and dynamic behavior.?
- Are there Unit Tests?
- Are all test cases passed?
- Is there a tracing between requirements and test cases?
- Is the documentation of the usage good enough to fulfill higher quality standards?

### Notes for tool validation according to standards

**Main requirements of ISO 26262-8 Chapter 11.4.9 - Validation of the software tool:**

- The validation shall provide evidence that the software tool complies with specified rquirements to its purpose.
E.g. the validation can be performed by using a customized test suite developed for the tool.
- The malfunctions and their corresponding erroneous outputs of the software tool occurring during
validation shall be analysed together with information on their possible consequences and with
measures to avoid or detect them.
- The reaction of the software tool to anomalous operating conditions shall be examined.

Conclusion: Together with a analysis of possible malfunctions and their possible consequences, the required measures in this chapter can fulfill the requiements for tool qualification according ISO 26262. For more details, doublecheck the corroponding chater in the standard.

**Main requirements of IEC 61508-3 Chapter 7.4.4 - Requirements for (offline) support tools:**

- All off-line support tools in classes T2 and T3 shall have a specification or product
documentation which clearly defines the behaviour of the tool and any instructions or
constraints on its use.
- An assessment shall be carried out for offline support tools in classes T2 and T3 to
determine the level of reliance placed on the tools, and the potential failure mechanisms of
the tools that may affect the executable software. Where such failure mechanisms are
identified, appropriate mitigation measures shall be takenv.
- For each tool in class T3, evidence shall be available that the tool conforms to its
specification or documentation.
- The results of tool validation shall be documented covering the following results:
  - a chronological record of the validation activities;
  - the version of the tool product manual being used;
  - the tool functions being validated;
  - tools and equipment used;
  - the results of the validation activity; the documented results of validation shall state either
that the software has passed the validation or the reasons for its failure;
  - test cases and their results for subsequent analysis;
  - discrepancies between expected and actual results.

Conclusion: Together with a analysis of possible failure mechanism of the tool and their possible consequences, the required measures in this chapter can fulfill the requiements for tool qualification according IEC 61508. For more details, doublecheck the corroponding chater in the standard.
