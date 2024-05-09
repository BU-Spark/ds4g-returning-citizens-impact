# TEMPLATE-base-repo

Create a new branch from dev, add changes on the new branch you just created.

Open a Pull Request to dev. Add your PM and TPM as reviewers. 

At the end of the semester during project wrap up open a final Pull Request to main from dev branch.


# Project overview
This project aims to analyze the impact of the Mayor's Office of Returning Citizens (ORC) on formerly incarcerated individuals re-entering society (returning citizens) in Boston. Helping returning citizens is not just a matter of social responsibility; it is also crucial for building stronger and more resilient communities. When individuals are supported in their transition back into society after incarceration, they are more likely to become productive members of their communities, positively contributing to the economy, reducing crime rates, and fostering social cohesion. By providing assistance and resources to returning citizens, we can help break the cycle of recidivism, promote rehabilitation, and ensure that everyone has the opportunity to rebuild their lives and pursue their full potential.

The analysis will be used for the annual impact report submitted to the Mayor's office, informing budget allocation for the upcoming fiscal year.

Key Objectives:

● Evaluate the impact of the ORC's services on returning citizens in terms of
housing, employment, legal assistance, social services, and more.

● Identify service disparities to improve equitable access and effectiveness of the
programs offered.

● Inform budgeting decisions for the upcoming fiscal year based on demonstrated
impact and needs.

# Technical architecture
Program "keyword_searcher.py" and "searcher_2.0.py" are the main searcher codes. Instructions on how to use them can be found in "keyword_searcher.py". Basically we iterate over all the text files provided by ORC and look for appearances of keywords. Count them for statistics, and elimating any potential wrong counts by excluding some keywords, this function can be achieved in "searcher_2.0.py". To use the python files, pull the branch and run the folder vis VSCode, and follow instructions inside.

# Bugs or Issues
Currently we do not have bugs. But if in the future one will pick up our project, please design more powerful searching programs that can deal with more context matching problems. We did not achieve that due to time limit.
