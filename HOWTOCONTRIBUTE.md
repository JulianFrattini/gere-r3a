# How to contribute

This guideline explains how to contribute to the initiative of creating and maintaining a model of requirements-affected activities and their attributes.

## Model Extension

Goals 1 (applicability) and 2 (suitability) of the model (see their definition in the [README.md](README.md)) require the model to be as complete as possible, i.e., contain sufficiently extensive activities and attributes to model any requirements-affected activity in any given software engineering context. Identifying missing activities and attributes will improve the applicability and suitability of the model.

### Generating Evidence

Currently, we support two types of generating new evidence but are open to [extending eligible methods](#further-contributions). Once new evidence was generated, [add it to the model](#adding-evidence-to-the-model) by continuing with the steps described there.

#### Contributing empirical Evidence

To contribute empirical evidence, consider the following workflow:

1. Review the proposed [revised protocol](./1-data-collection/interview-study/revised-interview-proposal.md) for structuring an interview with practitioners.
2. Conduct the interview and record the interview transcripts.

#### Contributing Evidence from Literature

To contribute evidence from literature, consider the following workflow:

1. Review the [literature review guideline](./1-data-collection/experimentation-literature/review-guideline.pdf), especially the inclusion and exclusion criteria, and generate a literature review protocol from it.
2. Conduct the literature review and record the eligible primary studies. Ensure the validity of the inclusion phase by [calculating the inter-rater agreement](./1-data-collection/experimentation-literature/validity_inclusion.ipynb) of multiple raters.

Two extension points of the existing literature review are considering (1) workshop papers, and (2) primary studies using other research methods than experiments (e.g., case studies or surveys). 

#### Further contributions

The two aforementioned techniques are valid approaches for extending the model with sound reasoning. However, if you devise additional methods for extending the model, please reach out to the [maintainers of the model](#maintainers) and propose the new method.

### Adding Evidence to the Model

Once you generated new evidence, conduct the following steps to add the evidence to the model:

1. Extract relevant mentions of requirements-affected activities and their attributes according to their definitions (stated both in the [protocol](./1-data-collection/interview-study/revised-interview-proposal.md) and study).
2. Code the extacted data using the [coding guidelines](./2-data-coding/meta-model-coding-guideline.pdf) and document the produced codes. You can extend the [data extraction sheet](./2-data-coding/r3a-data-extraction.xlsx) for this.
3. In case new codes emerged,
    1. rerun the [code consolidation](./3-model-construction/code-consolidation.ipynb) notebook to generate co-occurrence matrices of activities and attributes. From these,
    2. update the [model file](./3-model-construction/models/graphml/r3a-v2-minimized.graphml) to include the new activities and attributes, and
    3. update the [model consolidation](./3-model-construction/model-consolidation.md) documentation.
4. In case no new codes emerged, only rerun the [code consolidation](./3-model-construction/code-consolidation.ipynb) notebook to update the [activity-attribute study matrix](./3-model-construction/activity-attribute-studies.xlsx) which links pairs of activities and attributes to studies in which they are investigated.

## Model Maintenance

Goals 3 (extensibility) and 4 (usability) require maintenance of the model's structure and content in this repository. 

### Maintainers

The model is currently maintained by the following team:

| Name | Role | Since | Contact |
|---|---|---|---|
| Julian Frattini | Artifact Owner | 2024-01-29 | juf@bth.se |

Please reach out to the lead maintainers in case of questions.

### Rules for Maintenance

To ensure the extensibility and usability of the model, it is imperative to keep this repository well-documented and -organized. Consider standard guidelines for repository maintenance and be explicit in documenting any decision or contribution.

## Model Validation

The model requires validation, i.e., confirmation that the four goals mentioned in the [README](README.md) are met. Since the current, early version of the model should focus on [model extension](#model-extension) before attempting validation, the following sections are to be extended.

### Validating Applicability

We constitute that the model achieves goal 1 if we do not encounter any new requirements-affected activity that has no semantic equivalent in the model. Whenever [contributing empirical evidence](#contributing-empirical-evidence) does not produce any new activities, record this as a step towards the stability and applicability of the model.

### Validating Suitability

To validate suitability, we need to conduct empirical studies in a wide range of organizations and verify that characterizing the activities via the attributes associated with them ailgns with the organizations' perspectives of their performance. We envision two types of empirical studies:

1. Surveying the activities and generating an overview of attribute values for all affected activities.
This overview provides an absolute comparison of the activities and answers questions like "Which activity phase takes the longest time?" or "Which development activity is perceived as the least enjoyable?".
2. Conducting quasi-experiments at the case companies investigating whether certain properties of requirements artifacts or properties have an impact. For example, the subject of the experiments could be the comparison between two types of template systems for requirements specification or the avoidance of specific linguistic structures like passive voice. The subject of the experiments will be aligned with current questions and endeavors of the case companies to optimize their requirements engineering process in an evidence-based manner. The results of the quasi-experiments will be measured in terms of differences in attribute values of all affected activities.

### Validating Extensibility

By contributing to the [model extension](#model-extension), you also contribute to validating its exentisibility. Document any encountered challenges to allow continuous improvement of the model's extensibility.

### Validating Usability

By contributing the the validation of [applicability](#validating-applicability) and [suitability](#validating-suitability), you also contribute to validating its usability. Document any encountered challenges to allow continuous improvement of the model's usability.
