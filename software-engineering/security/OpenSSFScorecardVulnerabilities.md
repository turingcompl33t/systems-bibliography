## Do OpenSSF Scorecard Practices Contribute to Fewer Vulnerabilities (2023)

Nusrat Zahan, Shohanuzzaman Shohan, Dan Harris and Laurie Williams

Available [here](todo).

### Big Idea

Conduct an analysis of the relationship between OpenSSF security practices and the number of vulnerabilities reported for open source projects. The analysis indicates the security practices that are most important for reducing vulnerabilities, but finds that higher scorecard values are associated with higher numbers of vulnerabilities. Several confounding variables may account for this phenomenon. 

### Summary

The open source security foundation (OpenSSF) is the organization referred to in the title. The scorecard project computes an analysis of an open source project's vulnerabilities automatically. The objective of this paper is to empirically determine whether OpenSSF scorecard results actually reflect security status for particular packages. This is intended to help practitioners determine the most important measures to take when implementing security (in the event that they can only implement a subset of all available mitigations).

In short: which security practices have the most impact? Do particular practices have positive security outcomes?

The study collects scorecard information for open source packages from a previous study that aggregated this information. They compare the scorecard information with information from a collection of vulnerability databases.

The authors applied several predictive models to help practitioners understand important security practices.

The most important security practices are:

- The project is actively maintained
- The project utilizes code review prior to merging code with the master branch
- Github branch protection is employed
- The package has a published security policy

Overall, the study finds that projects with a greater number of implemented security practices (higher scorecard value) also have a greater number of security vulnerabilities. This is a confounding result. The authors list a number of limitations of their study that may account for this outcome. 

### Commentary

This is a very cool idea for a study, but the confounding variables listed in the study's limitations make it difficult to put in stock in the conclusions. 

### Questions

N/A

### Further Reading

- Open Source Insights 
- Can the OpenSSF Scorecard be Used to Measure the Security Posture of NPM and PyPI? (2022)