# Revised Interview Protocol

*The interview data used for this study was obtained by conducting an interview study with a different goal in mind. Though the obtained data fit this research goal adequately, we propose a revised, more gaol-oriented interview protocol for future replications.*

## Definitions

Introducing relevant terminology for the study[^1].

![Activities in Software Engineering](./../../supplementary/figures/activities-in-se.png)

An **activity** is any SE-relevant process performed by a (human or software) agent that uses one or more input artifacts and produces one or more output artifacts.
For example, the *implementing* activity receives several input artifacts like a requirements specification and system architecture to produce output artifacts like source code.

An activity is **requirements-affected** if at least one of its input artifacts is a requirements specification (yellow activities in the figure above).
The aforementioned implementing activity is requirements-affected because it considers a requirements specification as an input.
An example of a non-requirements-affected activity would be *writing unit test* in case these are only derived from functional and not requirements specifications.

An **attribute** of an activity is a measurable property that informs about the performance of the activity.
For example, the implementing activity can be evaluated by measuring its *duration* (how long it takes), its *correctness* (the precision of covering requirements), and its *completeness* (the recall of covering requirements), among others.

## Questions

The following questions serve as a guideline for conducting a semi-structured interview with a practitioner at an organization developing software.

1. Which requirements artifacts are specified in your organizational context (e.g., use cases, user stories, etc.)?
2. In which software development-related activities are these artifacts used (e.g., during implementing, testing, etc.)?
3. How do you decide whether these activities were successful or not (e.g., measuring their duration, the number of failing test cases per developed code, etc.)?

Use these questions iteratively to determine all requirements-dependent activities and their attributes that the practitioner is aware of.

[^1]: Definitions are taken verbatim from the study.