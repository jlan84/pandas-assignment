import pandas as pd




if __name__ == "__main__":

    df = pd.read_csv('../data/hospital-costs.csv')
    #1
    df['Total Charges'] = df['Discharges']*df['Mean Charge']
    #2
    df['Total Costs'] = df['Discharges']*df['Mean Cost']
    #3
    df['Markup Rate'] = df['Total Charges']/df['Total Costs'] 
    
    #Part 2 #1
    ailment_group = (df.groupby('APR DRG Description').sum().
                     sort_values('Discharges',ascending=False).reset_index())
    
    print(ailment_group.info())
    
    print(ailment_group[['APR DRG Description','Discharges']].head(10))

    albany = df[df['Facility Name'].str.contains('Albany')]
    print(albany)