# Cultural Consensus Theory with PyMC

## Structure and Choices
This model defines two functions that do three tasks: one function for loading the data and running the CCT model, and the other function generates the results. The CCT analysis is performed using these functions in the main model block.
In the **cct_model** function, I defined the prior for D as uniform and Z as bernoulli. This is because the most accurate way to represent the informants' knowledge/competence for D is by using a uniform prior. It ensures that the likelihood of the informant having no prior information, complete previous knowledge, or being anywhere in between the two is equal. Additionally, since a response's correctness is represented by a binary value (1 for correct and 0 for incorrect), a bernoulli prior would be best for estimating consensuses (Z).


## Results and Checks
The results of the informants' competency (D) are that 5 of them have low competency and 5 of them have higher competency, splitting the competency results directly in half. Informant 6 had the highest competency mean of 0.877, while Informant 3 had the lowest competency mean of 0.559. The results indicate that while informant 3 is less likely to provide a correct response, Informant 6 is more likely to do so. This increases the probability that informant 3 will give an incorrect response, but it does not guarantee it. More competent informants are given more weight in the CCT model because they are more likely to agree with and comprehend the common cultural consensus within the culture of "plant knowledge."

For the consensus (Z) results, a mean that is closer to 0 indicates that the cultural consensus about the response is false, and a mean that is closer to 1 indcates that the response is true. Consensus responses that fall closer to the middle (~0.5) demonstrate that there is disagreement even among knowledgeable informants over the consensus response. Item 5, which has a mean of 0.554, illustrates this phenomenon.

In the Diagnostics Summary, all of the **r_hat** values are 1.00, implying that the model converged. Convergence indicates that the sample selected in the **cct_model** block are reliable for estimating consensus (Z) and competence (D).


## Majority Vote Comparison
The raw data is used to determine the simple majority vote. This is because the model calculates the majority response without taking competence level into account. Thus, the simple majority vote is not in agreement with the consensus. For instance, the model estimated that the consensus for questions 2, 6, 8, and 10 would give the correct response, but the majority vote attributed the incorrect response for those questions. This example illustrates the influence of competence on consensus as demonstrated in the CCT model.
