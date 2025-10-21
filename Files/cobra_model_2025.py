"""
Author:       Eva Nieuwenhuis 
Group:        Maastricht Centre for Systems Biology and Bioinformatics
Course:       Master's project Bioinformatics and systems biology; UvA, VU and UM 

Description:  To explore changes in the excretion of signaling peptides by the heart the metabolic model 
              had to be expanded. This code adds the signaling peptides, reactions needed for their 
              production and the genes that where not already present in the human genome scale model. At 
              the end the new model is saved.  

"""
# Import the needed packages 
import sys
import os 
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from cobrapy import io
#from src.cobrapy_fork import io
import pandas as pd
from cobrapy import Reaction, Metabolite, Gene
#from src.cobrapy_fork import Reaction, Metabolite, Gene



def main():
    # Load lastest version model 
    model = io.load_json_model(r"data\cobra_model_expansion\model_inhouse_v7.json")

    # Inspect the model
    print(len(model.reactions))
    print(len(model.metabolites))
    print(len(model.genes))

    # Add metabolites 
    df_new_met = pd.read_excel(r"data\cobra_model_expansion\metabolites_additions_v8.xlsx")
    model =add_metabolites(df_new_met, model)

    # Add genes 
    df_new_genes = pd.read_excel(r"data\cobra_model_expansion\new_genes.xlsx")
    model = add_genes(df_new_genes, model)

    # Add reactions 
    df_new_rxn = pd.read_excel(r"data\cobra_model_expansion\reactions_new_additions_v8.xlsx")
    model = add_reactions(df_new_rxn, model)

    # Save the model
    io.save_json_model(model, r"data\cobra_model_expansion\model_inhouse_v8.json")

    # Get information of a metabolite
    met_info = model.metabolites.get_by_id("angiotensin_I[e]")
    print("ID met:", met_info.id)
    print("Name met:", met_info.name)
    print("Formula met:", met_info.formula)
    print("Charge met:", met_info.charge)
    print("Compartment met:", met_info.compartment)
    print("Notes met:", met_info.notes)
    print("Number of reactions met:", len(met_info.reactions))

    # Get information on a reaction 
    rxn_info = model.reactions.get_by_id("MAR31050")
    print("ID rxn:", rxn_info.id)
    print("Name rxn:", rxn_info.name)
    print("Reaction string rxn:", rxn_info.reaction) 
    print("Lower bound rxn:", rxn_info.lower_bound)
    print("Upper bound rxn:", rxn_info.upper_bound)
    print("Subsystem rxn:", rxn_info.subsystem)
    print("Gene reaction  rxn:", rxn_info.gene_reaction_rule)
    print("Notes rxn:", rxn_info.notes)

    # Explore gene catalysing the reaction
    gene_info = model.genes.get_by_id("ENSG00000097021")
    print("ID gene:", gene_info.id)
    print("Name gene:", gene_info.name)
    print("Notes gene:", gene_info.notes)


def add_metabolites(df_met, model): 
    """
    This function adds new metabolites to a given model.

    Parameters
    ----------
    df_met: pd.DataFrame
        Dataframe contianing the metabolites that need to be added 
    model: cobra.Model 
        The metabolic model 
        
    Returns
    -------
    model: cobra.Model 
        The metabolic model with the new metabolites included  
    """
    # Identify the rows that contain a ID 
    df_with_id = df_met[df_met['after_metabolite_ID'].astype(str).str.strip() != ""]

    # Create a list to store the new metabolites 
    new_metabolites = []

    # Loop over the rows with ID 
    for i, row in df_with_id.iterrows():

        # Remove all space around the ID
        stripped_id = str(row["after_metabolite_ID"]).strip()

        # Extract the metabolite information
        met = Metabolite(
            id=stripped_id,
            name=row.get("after_metabolite_name", ""),
            formula=row.get("after_metabolite_formula", ""),
            charge=row.get("after_metabolite_charge", ""),
            compartment=row.get("after_metabolite_compartment", "c"),)

        # Add notes if present 
        if pd.notna(row.get("project_notes", None)):
            met.notes["project_notes"] = str(row["project_notes"]).strip()

        # Add new metabolite to the list 
        new_metabolites.append(met)

    # Add all new metabolites to the model
    model.add_metabolites(new_metabolites)

    return(model)

def cobra_format(side_str, sign, model):
    """
    This function creates a dictionary representing the reaction in terms of their substrates' or products' 
    stoichiometries. This format is needed to add the reactions to the model. 

    Parameters
    ----------
    side_str: str
        A string representing one side of a reaction 
    sign: int 
        Indicates whether the metabolites are consumed or produced
    model: cobra.Model 
        The metabolic model 
        
    Returns
    -------
    stoich_dict: dict
        A dictionary of the stoichiometry of the products or substrates 
    """
    # Create a dictionary 
    stoich_dict = {}

    # Split all terms 
    parts = side_str.split('+')
    
    #From each term determine the name and coefficient 
    for part in parts:
        # Remove white spaces around coefficient and metabolite 
        part = part.strip()

        # Split part into coefficient and white space 
        coeff_name = part.split(' ')
        
        # If there is no coefficient and thus len(tokes) = 1, the coefficeint is 1
        if len(coeff_name) == 1:
            coeff = 1

            # Only thing in token is metabolite name 
            name = coeff_name[0]
        else:
            try:
                # Try to convert the first token in a float
                coeff = float(coeff_name[0])

                # All other tokes are metabolite name 
                name = ' '.join(coeff_name[1:])

            # No conversion possible then 1 as coefficient 
            except ValueError:
                coeff = 1
                name = part

        # Make sure the metabolite excist in the model 
        try:
            met = model.metabolites.get_by_id(name)
        except KeyError:
            raise ValueError(f"Metabolite '{name}' not found in the existing model.")
        
        # Add coefficient with correct sign to dictionary
        stoich_dict[met] = sign * coeff
    
    return stoich_dict

def add_reactions(df_rxn, model): 
    """
    This function adds new reactions to a given cobra model.

    Parameters
    ----------
    df_rxn: pd.DataFrame
        Dataframe contianing the reactions that need to be added 
    model: cobra.Model 
        The metabolic model 
        
    Returns
    -------
    model: cobra.Model 
        The metabolic model with the new reactions included  
    """

    # Loop over all reactions
    for i, row in df_rxn.iterrows():

        # Obtain information about the reaction 
        reaction_formula = row.get('after_reaction_formula_readable', '')
        reaction_name = row.get('after_reaction_name', '')
        reaction_id = row.get('after_reaction_ID', '')
        reaction_subsystem = row.get('after_reaction_subsystem', '')
        gpr = row.get('after_reaction_GPR_readable', '')
        gpr = row.get('after_reaction_GPR_readable', '')

        # If there is no gene rule ensure the space is empty 
        if gpr.lower() == 'no gene rule':  
            gpr = ' '
    
        # Ensure notes do not become Na or NaN
        notes = "" if pd.isna(row.get('project_notes')) else str(row['project_notes']).strip()

        # Make a reaction and add all obtained information 
        reaction = Reaction(reaction_id)
        reaction.name = reaction_name
        reaction.subsystem = reaction_subsystem
        reaction.gene_reaction_rule = gpr
        reaction.notes = {'project_notes': notes} if notes != "" else {}

        # Split the reaction in reactants and products 
        substrates_str, products_str = reaction_formula.split('-->')

        # Create dictionary and add stoichiometry of inputs and outputs 
        stoich = {}
        stoich.update(cobra_format(substrates_str, -1, model))
        stoich.update(cobra_format(products_str, 1, model))

        # Add reaction to the model 
        reaction.add_metabolites(stoich)
        model.add_reactions([reaction])

    return(model)



def add_genes(df_genes, model): 
    """
    This function adds new genes to a given cobara model.

    Parameters
    ----------
    df_genes: pd.DataFrame
        Dataframe contianing the genes that need to be added 
    model: cobra.Model 
        The metabolic model 
        
    Returns
    -------
    model: cobra.Model 
        The metabolic model with the new genes included  
    """

    # Loop over all genes 
    for i, row in df_genes.iterrows():
        gene_id = row['name']
        gene_name = row['short_name']

        # Ensure to only add genes not yet present in the model 
        try:
            gene = model.genes.get_by_id(gene_id)
        except KeyError:
            gene = Gene(gene_id)
            model.genes.append(gene)
            gene.name = gene_name
    
    return(model)

if __name__ == "__main__":
    main()
