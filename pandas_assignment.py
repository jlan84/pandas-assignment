import pandas as pd
import matplotlib.pyplot as plt

##Part 1
df = pd.read_csv('data/hospital-costs.csv')



df['Total Charges'] = df['Discharges']*df['Mean Charge']
df['Total Costs'] =  df['Discharges']*df['Mean Cost']

df['Markup Rate'] = df['Total Charges']/df['Total Costs']


markup = df[['Facility Name','Total Charges', 'Total Costs', 'Markup Rate']]


#Part 2
ailments_group = (df[['APR DRG Description','Discharges']]
                  .groupby('APR DRG Description').sum())


#Part 3

net = df[['Facility Name', 'Total Charges', 'Total Costs']]
hospital_charge_group = net.groupby('Facility Name').sum()
hospital_charge_group['Net Income'] = (hospital_charge_group['Total Charges'] -
                                       hospital_charge_group['Total Costs'])


#Part 4

VM_df = df[df['APR DRG Description']=='Viral Meningitis']
VM_df = VM_df[["Facility Name", "APR DRG Description",
               "APR Severity of Illness Description","Discharges", "Mean Charge",
                "Median Charge", "Mean Cost"]]

VM_df_moderate = VM_df[VM_df['APR Severity of Illness Description']== 'Moderate']
VM_df_moderate = VM_df_moderate[['Facility Name','Mean Charge']]

# print(VM_df_moderate.sort_values(by="Mean Charge", ascending=True).head(1))
VM_df_moderate_3discharges = VM_df[(VM_df['APR Severity of Illness Description']
                                    == 'Moderate') & (VM_df['Discharges'] > 3)]
# print(VM_df_moderate_3discharges.sort_values(by='Mean Charge').head(1))

VM_most_discharges = VM_df.groupby('Facility Name').sum()
# print(VM_most_discharges.sort_values(by='Discharges', ascending=False))

#7
charge_severity_df = (df[['APR Severity of Illness Description', 'Mean Charge']].
                      groupby('APR Severity of Illness Description').mean().reset_index())

severity_dic = {'Minor': 1, 'Moderate': 2, 'Major': 3, 'Extreme': 4}
charge_severity_df['APR Severity of Illness Description'] = (charge_severity_df[
                                                            'APR Severity of Illness Description'].
                                                            map(severity_dic))
illness_df = (df[['APR DRG Description','APR Severity of Illness Description','Discharges','Total Charges']]
              .groupby(['APR DRG Description','APR Severity of Illness Description'])
              .sum().reset_index())
print(illness_df.sort_values(by='Total Charges', ascending=False))
                






# print(charge_severity_df.info())



# if __name__ =='__main__':
#     print(df.info())
#     print(markup.info())
#     print(markup.sort_values(by="Markup Rate"))
#     print(ailments_group.sort_values(by='Discharges', ascending=False))
#     print(hospital_charge_group.sort_values(by='Net Income', ascending=False))