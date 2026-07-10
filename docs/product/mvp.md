# MVP — Opportunity Tailoring Engine

## Problem

A professional has a large amount of relevant history but must manually select, rewrite and format it for each opportunity.

Generic résumés fail to emphasize the evidence most relevant to a specific role.

## MVP hypothesis

Given:

1. a structured professional profile;
2. a specific opportunity description;
3. user-approved evidence;

CareerOS can generate a more relevant and consistent application package while preserving truthfulness and traceability.

## Initial real-world use case

The first validated use case is tailoring a professional résumé for an international Subject Matter Expert opportunity involving Microsoft Fabric, Power BI, SQL Server, Azure data technologies and technical content review.

## Inputs

- profile metadata;
- professional summary;
- work experiences;
- projects;
- measurable results;
- technologies and skills;
- certifications;
- education;
- languages;
- publications and content;
- opportunity description;
- output language and country;
- user preferences.

## Outputs

Required:

- tailored résumé in Markdown;
- tailored résumé in PDF;
- match analysis;
- keyword coverage report;
- evidence map connecting résumé claims to source records.

Optional:

- cover letter;
- application-form responses;
- interview preparation notes.

## MVP boundaries

The MVP will not initially include:

- automatic LinkedIn scraping;
- automatic Upwork authentication;
- Neo4j;
- autonomous multi-agent orchestration;
- salary negotiation;
- automatic submission of applications;
- a full web interface;
- integration with FreireAI.

## Success criteria

The MVP is successful when:

- the generated résumé contains no unsupported claims;
- every selected claim can be traced to evidence;
- the user can edit the source profile without changing code;
- the opportunity can be replaced without restructuring the profile;
- automated tests validate the core tailoring workflow;
- the generated package is useful for a real application.
