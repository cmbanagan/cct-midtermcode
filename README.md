# Cultural Consensus Theory with PyMC

# Structure and Choices
This model defines two functions that do three tasks: one function for loading the data and running the CCT model, and the other function generates the results. The CCT analysis is performed using these functions in the main model block.
In the **run_model** function, I defined the prior for D as uniform and Z as bernoulli. This is because the most accurate way to represent the informants' knowledge/competence for D is by using a uniform prior. It ensures that the likelihood of the informant having no prior information, complete previous knowledge, or having any degree of prior knowledge anywhere in between is equal. Since a response's correctness is represented by a binary value, a bernoulli prior would be best for estimating consensuses (Z). The informant either gives a correct response (1) or an incorrect one (0).

# Results and Checks

# Majority Vote Comparison

