import pandas as pd
import matplotlib.pyplot as plt

if __name__ == "__main__":

    #Part 3
    df = pd.read_csv('../data/hospital-costs.csv')

    df['Total Charges'] = df['Discharges']*df['Mean Charge']
    df['Total Costs'] = df['Discharges']*df['Mean Cost']
    df['Markup Rate'] = df['Total Charges']/df['Total Costs'] 

    net = df[['Facility Name', 'Total Charges', 'Total Costs']]
    
    facility_group = net.groupby('Facility Name').sum().reset_index()
    facility_group['Net Income'] = (facility_group['Total Charges'] - 
                                    facility_group['Total Costs'])
    
    
    #Part 4

    # print(df.info())
    vm_df = df[df['APR DRG Description'] == 'Viral Meningitis']
    
    vm_df = vm_df[['Facility Name', 'APR DRG Description', 
                   'APR Severity of Illness Description', 'Discharges', 
                   'Mean Charge', 'Median Charge', 'Mean Cost']]
    
    moderate = vm_df[vm_df['APR Severity of Illness Description'] == 'Moderate']
    print(moderate[['Facility Name', 'Mean Charge']].sort_values('Mean Charge', ascending=True))
    
    more_than_3_vm = moderate[moderate['Discharges'] > 3]
    print(more_than_3_vm[['Facility Name','Discharges','Mean Charge']].
                          sort_values('Mean Charge'))
    
    discharges = (vm_df.groupby('Facility Name').sum().sort_values('Discharges',
                                ascending=False).reset_index())
    print(discharges.head())

    
    vm_df.boxplot('Mean Charge', by='APR Severity of Illness Description')
    
    severities = ['Minor','Moderate', 'Major', 'Extreme']

    severity_df = pd.DataFrame({severity: vm_df[
                               vm_df['APR Severity of Illness Description'] == severity]
                               ['Mean Charge'] for severity in severities},
                               columns = severities).boxplot(return_type='axes')
    
    severity = (vm_df[['APR Severity of Illness Description', 'Mean Charge']].
                groupby('APR Severity of Illness Description').mean().reset_index())
    
    severity['APR Severity of Illness Description'] = (
                                severity['APR Severity of Illness Description'].
                                map({'Minor': 0, 'Moderate': 1, 'Major': 2,
                                     'Extreme': 3}))
    print(severity.corr())

    illnesses = (df.groupby(['APR DRG Description','APR Severity of Illness Description']).
                            sum().reset_index())
    print(illnesses[['APR DRG Description','APR Severity of Illness Description',
                     'Discharges']].sort_values('Discharges', ascending=False))