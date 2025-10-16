# Safety Manual <!-- omit in toc -->

- [Introduction](#1-introduction)
  - [Purpose of this Document](#11-purpose-of-this-document)
  - [Product Identification](#12-product-identification)
  - [Product Goals and Usage](#13-product-goals-and-usage)
  - [Tool Usage according to ISO 26262](#14-tool-usage-according-to-iso-26262)
  - [Classification Hints](#15-classification-hints)
    - [Further Considerations](#151-further-considerations)
  - [Qualification Hints](#16-qualification-hints)
  - [Evaluation of the Tool Develpment Process](#17-evaluation-of-the-tool-development-process)
  - [Validation of the Software Tool](#18-validation-of-the-software-tool)
- [Example Use Cases](#2-example-use-cases)
  - [Generate Lobster File from Doxygen XML Files for **non-safety-relevant** Requirements](#21-generate-lobster-file-from-doxygen-xml-files-for-non-safety-relevant-requirements)
  - [Generate Lobster File from Doxygen XML Files for **safety-relevant** Requirements](#22-generate-lobster-file-from-doxygen-xml-files-for-safety-relevant-requirements)
- [Summary](#3-summary)
  - [Summary: Generate Lobster File from Doxygen XML Files for **non-safety-relevant** Requirements](31-generate-lobster-file-from-doxygen-xml-files-for-non-safety-relevant-requirements)
  - [Summary: Generate Lobster File from Doxygen XML Files for **safety-relevant** Requirements](32-generate-lobster-file-from-doxygen-xml-files-for-safety-relevant-requirements)
  
## 1 Introduction

### 1.1 Purpose of this Document

This document summarizes the qualification requirements on the ***lobster-doxygen*** software tool according to the methodology described in ISO 26262-8. Use cases relevant for the development of safety related systems are analyzed. For each use case, a classification of the Tool Confidence Level (TCL) is made with recommendations for the qualification methods to be used. Wherever relevant, requirements and assumptions regarding the context in which the tools are used that have an impact on the TCL are stated. This document may also serve as a Safety Manual, since hints for the qualification procedures are given.

### 1.2 Product Identification

The tool classification examples and all statements within this document apply to the latest released version of the ***lobster-doxygen*** software tool.

### 1.3 Product Goals and Usage

The ***lobster-doxygen*** software tool is a conversion tool which generates a LOBSTER common interchange format file from a Doxygen XML file. This interchange file contains references (LOBSTER traces) to implementations of TRLC-style software requirements extracted from the Doxygen file. The output file generated is intended for subsequent use by a separate tool (lobster-report) which generates a report detailing the coverage of TRLC-style software requirements by their respective software implementations.

### 1.4 Tool Usage according to ISO 26262

In accordance with ISO 26262, any tool can be used in the development of safety-related ECUs. The tool user needs to ensure that, based on his use case, a tool classification was conducted, and that a qualification of the tool has been executed on the basis of this classification.

Tool classification and qualification must be carried out by the user of the tool, who knows his use case in detail. Example use cases and their corresponding hints for classification and qualification are provided in chapter 2 of this document.

### 1.5 Classification Hints

For every planned use case of the tool, the tool confidence level TCL needs to be assessed according to ISO 26262. The TCL result largely depends on the additional process constraints which apply for this use case.

The primary purpose of classification is to identify the extent to which errors resulting from the ***lobster-doxygen*** tool can cause violations of a safety goal. In the case of the ***lobster-doxygen*** tool and in a typical use case, errors may take one of 3 general forms:

- Ommission of an implementation reference
- Corruption of an implementation reference
- Phantom occurrence of an implementation reference

Ommission errors will appear as a requirement with no implementation in the generated coverage report; the developer will necessarily detect these errors upon review of the coverage report. Therefore, ommission errors are highly unlikely to result in a violation of a safety goal under even minimal process constraint conditions.

A corruption error is, in essence, a composition of an ommission error and a phantom occurrence.

Corruption errors and phantom occurrences have shared implications: in either case, there are 2 possible results:

- The implementation reference now references a non-existent requirement
- The implementation reference now references an incorrect but existing requirement

To detect cases where a reference to an non-existent requirement is erroneously created, the user shall use a report generator which can identify and warn the user about references to non-existent requirements.

Cases where a reference to an incorrect but existing requirement is erroneously created cannot be detected by the report generator. To detect these cases, it would be necessary for the user of the software tool to validate the end product against its requirements. However, because the requirement identifiers for TRLC-style requirements are string-based rather than consecutive-numerical, it is considered highly unlikely that an error in the ***lobster-doxygen*** tool could cause an implementation reference to reference an incorrect but existing requirement. Therefore, ***lobster-doxygen*** may be classified with a confidence level of **TCL1** in cases where the process constraints require product validation (typical of safety-relevant systems).

#### 1.5.1 Further Considerations

To avoid cases where both the ***lobster-doxygen*** conversion tool ***and*** the lobster-trlc/lobster-report tools erroneously omit the same requirement, these tools should be developed independently of one another.

### 1.6 Qualification Hints

Each main release of ***lobster-doxygen*** needs to be qualified individually, covering all planned use cases classified as TCL2 or TCL3. Qualification methods for each use case need to be chosen according to the ASIL of the product under development. For the qualification of ***lobster-doxygen***, only the qualification methods

- 1b (Evaluation of the tool development process)

- 1c (Validation of the software tool)

mentioned in ISO 26262-8 can be considered. Justification against other methods:

- The qualification method **1a** (increased confidence from use) cannot be considered, since the ***lobster-doxygen*** tool has limited use in existing development projects.

- The qualification method **1d** (development in accordance with a safety standard) cannot be considered, since ***lobster-doxygen*** was not developed in accordance with any safety standard.

NewTec GmbH recommends the qualification method **1c** for the ***lobster-doxygen*** software tool.

### 1.7 Evaluation of the Tool Development Process

The qualification method "evaluation of the tool development process" requires that the developer assess the tool development process and provide evidence that the tool was developed in compliance with an appropriate national or international standard (or a development process based on such a standard). The ***lobster-doxygen*** tool was developed according to the NewTec standard for Python development. This standard includes documentation of tool requirements and architecture, coding guidelines, full trace and test coverage, and the PEP 8 style guide. If the developer decides to use this qualification method, the developer must provide evidence that the development process was sufficiently similar to a process defined in an existing national or international standard for tool development. Due to the relative complexity of this method and the relative simplicity of this software tool, NewTec GmbH recommends against this qualification method in favor of the method "validation of the software tool".

### 1.8 Validation of the Software Tool

The qualification method "validation of the software tool" requires that the developer provide evidence that the software tool fulfills the tool requirements as they relate to its purpose in the development context. This is accomplished by testing the tool against the relevant requirements. The ***lobster-doxygen*** GitHub repository includes example test scripts which may be used or adapted for this qualification method.

It is good practice to use a test configuration with known input data and check the corresponding output of the tool for correctness e.g. by a formal review. The test configuration and test data should be determined based on the planned use case. Where a newer version of the software is being qualified, it may be qualified in an automated way against the output of an older, previously qualified version of the software. Another good practice is to stimulate an error and check whether the tool can detect it as expected.

## 2 Example Use Cases

### 2.1 Generate Lobster File from Doxygen XML Files for non-safety-relevant Requirements

The following table is an example of a use case where the ***lobster-doxygen*** tool is used for non-safety-relevant requirements:

|||
|---|---|
|**Intended Purpose**|Generate a LOBSTER common interchange format (.json) file from a Doxygen XML file which contains references to non-safety-relevant features implemented by the source software. Each feature represents the implementation (in part or in whole) of the respective requirement(s) from the software requirements specification.|
|**Environmental, Functional and Process Constraints**|Operating system: Windows 10 (version 20H2, 64bit)<br><mark>***lobster-doxygen*** version: 1.0.0</mark><br><mark>[lobster-doxygen configuration, if applicable]</mark>|
|**Description**|Run the **lobster-doxygen** python tool, using the paths of the input and output files as arguments.|
|**Output**|LOBSTER common interchange format file which links implemented features with their respective non-safety-relevant source requirements.|
|**Tool Impact**|**TI1 (No possibility of impact on a safety requirement)**<br>Rationale:<br><ul><li>Since the features which are converted to a lobster file are not safety-relevant, ***lobster-doxygen*** does not have an impact on the safety requirements.</li></ul>|
|**Tool Error Detection**|**TD2 (Medium degree of confidence of prevention or detection)**<br>Rationale:<br><ul><li>Omission of an implemented feature is quickly detected by checking the implementation report generated from this output to identify missing implementations.</li><li>Corruption or phantom occurrences of an implemented feature may occur in one of two ways: either the implemented feature is references an incorrect but existing requirement or a non-existent requirement.<ul><li>Incorrect but existing requirement: must be detected during product validation</li><li>Non-existent requirement: will inevitably be discovered by the report generation tool or by developer which views said report.</li></ul></li><li>Overlooked errors in the generated LOBSTER file are likely since the file is an intermediate file in a toolchain and is not typically viewed by the developer(s).</li></ul>|
|**Tool Confidence Level**|**TCL1**|
|**Recommended Method of Qualification**|Not required|

### 2.2 Generate Lobster File from Doxygen XML Files for safety-relevant Requirements

The following table is an example of a use case where the ***lobster-doxygen*** tool is used for safety-relevant requirements:

|||
|---|---|
|**Intended Purpose**|Generate a LOBSTER common interchange format (.json) file from a Doxygen XML file which contains references to safety-relevant features implemented by the source software. Each feature represents the implementation (in part or in whole) of the respective requirement(s) from the software requirements specification.|
|**Environmental, Functional and Process Constraints**|Operating system: Windows 10 (version 20H2, 64bit)<br><mark>***lobster-doxygen*** version: 1.0.0</mark><br><mark>[lobster-doxygen configuration, if applicable]</mark>|
|**Description**|Run the ***lobster-doxygen*** python tool, using the paths of the input and output files as arguments.|
|**Output**|LOBSTER common interchange format file which links implemented features with their respective safety-relevant source requirements.|
|**Tool Impact**|**TI2 (Possibility of impact on a safety requirement)**<br>Rationale:<br><ul><li>Since the features which are converted to a lobster file are safety-relevant, it is possible that ***lobster-doxygen*** may omit, corrupt, or create phantom occurrences of implemented features and thereby lead to the violation of a safety goal.</li></ul>|
|**Tool Error Detection**|**In case of no additional process constraints:**<br>**TD2 (Medium degree of confidence of prevention or detection)**<br>Rationale:<br><ul><li>Omission of an implemented feature is quickly detected by checking the implementation report generated from this output to identify missing implementations.</li><li>Corruption or phantom occurrences of an implemented feature may occur in one of two ways: either the implemented feature is references an incorrect but existing requirement or a non-existent requirement.<ul><li>Incorrect but existing requirement: must be detected during product validation</li><li>Non-existent requirement: will inevitably be discovered by the report generation tool or by developer which views said report.</li></ul></li><li>Overlooked errors in the generated LOBSTER file are likely since the file is an intermediate file in a toolchain and is not typically viewed by the developer(s).</li></ul>**In case of rigid additional process constraints:**<br>**TD1 (High degree of confidence of prevention or detection)**<br>Necessary additional process constraints:<br><ul><li>Validation testing (typical of safety systems)</li></ul>|
|**Tool Confidence Level**|**In case of no additional process constraints:**<br>**TCL2**<br>**In case of rigid additional process constraints:**<br>**TCL1**|
|**Recommended Method of Qualification**|Validation of the software tool|

## 3 Summary

The user of the software tool must determine the appropriate tool classification for their use case and the appropriate qualification method. The following use case summaries are only examples.

### 3.1 Summary: Generate Lobster File from Doxygen XML Files for non-safety-relevant Requirements

If the ***lobster-doxygen*** tool is used solely for conversion of non-safety-relevant requirements, the tool can be classified with a confidence level of **TCL1** and requires no qualification for use.

### 3.2 Summary: Generate Lobster File from Doxygen XML Files for safety-relevant Requirements

If the ***lobster-doxygen*** tool is used for conversion of safety-relevant requirements, the tool's classification depends on the additional process requirements which apply for the project. If the process requirements demand validation of the end product against the product's requirements, ***lobster-doxygen*** may be classified with a confidence level of **TCL1** and requires no qualification for use. In cases where the process requirements are less rigid, the user of the software tool must determine the increased tool confidence level and perform qualification via validation of the software tool.
