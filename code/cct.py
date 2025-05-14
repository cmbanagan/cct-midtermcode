import numpy as np
import pandas as pd
import pymc as pm
import arviz as az
import os
    

def cct_model(plant_know):
    draws = 2000
    tune = 1000
    chains = 4
    df = pd.read_csv(plant_know)
    data = df.drop(columns="Informant").to_numpy()
    N, M = data.shape
    with pm.Model() as model:
         D = pm.Uniform('D', lower=0.5, upper=1, shape=N) 
         Z = pm.Bernoulli('Z', p=0.5, shape=M)
         D_reshaped = D[:, None]
         p = Z * D_reshaped + (1 - Z) * (1 - D_reshaped)
         pm.Bernoulli('X', p=p, observed=data)
         trace = pm.sample(draws=draws, tune=tune, chains=chains)
    return trace



def show_results(trace, data):
    
    D_competence = trace.posterior['D'].mean(dim=['chain', 'draw']).values
    print("\n--- Posterior Mean Competence (D) ---")
    for i, competence in enumerate(D_competence):
        print(f"Informant {i+1}: {competence:.3f}")
    az.plot_posterior(trace, var_names=['D'])
    

    Z_consensus = trace.posterior['Z'].mean(dim=['chain', 'draw']).values
    print("\n--- Posterior Mean Consensus (Z) ---")
    for j, prob in enumerate(Z_consensus):
        print(f"Item {j+1}: Mean = {prob:.3f}, Estimated = {int(round(prob))}")
    az.plot_posterior(trace, var_names=['Z'])
              
                      
    majority_vote = np.round(data.mean(axis=0))
    for i, majority in enumerate(majority_vote):
            print(f"Item {i+1}: {int(majority)}")


    print("\n--- Convergence Diagnostics ---")
    summary = az.summary(trace, var_names=['D', 'Z'])
    print(summary)



if __name__ == '__main__':
    script_dir = os.path.dirname(os.path.realpath(__file__)) #Used AI to determine how to find CSV file
    data_path = os.path.join(script_dir, "..", "data", "plant_knowledge.csv")
    trace = cct_model(data_path)
    show_results(trace, pd.read_csv(data_path).drop(columns="Informant").to_numpy())