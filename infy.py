#Task 1 - Confidence Interval
import pandas as pd
import scipy.stats as stats
import math
import numpy as np
import warnings

warnings.filterwarnings('ignore')
#Sample_Size
sample_size=2000
#Z_Critical Score
z_critical = stats.norm.ppf(q = 0.95)  
print('z-critical for 95% is:',z_critical)
print('============================================================================')
# path        [File location variable]
data = pd.read_csv(path)
#Code starts here
data_sample = data.sample(n=sample_size,random_state=0)
sample_mean = data_sample['installment'].mean()
print(' sampled data mean is:',sample_mean)
print('============================================================================')
sample_std= data_sample['installment'].std()
print('The the standard deviation of sampled data:',sample_std)
print('==============================================================================')
margin_of_error = z_critical*sample_std/math.sqrt(sample_size)
print('margin of error is:',margin_of_error)
confidence_interval = (sample_mean-margin_of_error,sample_mean+margin_of_error)
print('The confidence interval is:',confidence_interval)
print('===============================================================================')
true_mean=data['installment'].mean()
print(true_mean)


#Task 2 - CLT
import matplotlib.pyplot as plt
import numpy as np

#Different sample sizes to take
sample_size=np.array([20,50,100])
#Code starts here
fig,axes= plt.subplots(nrows=3, ncols=1)
for i in range (len(sample_size)):
    m=[]
    for j in range(1000):
        sampled_data = data['installment'].sample(n=sample_size[i])
        sample_mean=sampled_data.mean()
        m.append(sample_mean)
    mean_series=pd.Series(m)  
    axes[i].hist(mean_series)

 

#Task 3 - Small Business Interests
#Importing header files
from statsmodels.stats.weightstats import ztest
#Code starts here
data['int.rate'] = data['int.rate'].str.replace(r'%','')
data['int.rate']= pd.to_numeric(data['int.rate'])
data['int.rate']= data['int.rate']/100
A=data[data['purpose']=='small_business']['int.rate']
B=data['int.rate'].mean()
z_statistic,p_value = ztest(x1 = A ,value = B,alternative='larger')
print('z-statistic is:',z_statistic)
print('p-value is:',p_value)
if p_value > 0.05:
    print('Accept the null hypothesis')
else:
    print('Reject null hyphothesis')



#Task 4 -  Installment vs Loan Defaulting
#Importing header files
from statsmodels.stats.weightstats import ztest
#Code starts here
A=data[data['paid.back.loan']=='No']['installment']
B=data[data['paid.back.loan']=='Yes']['installment']
z_statistic,p_value=ztest(x1=A,x2=B)
print('z-statistic is:',z_statistic)
print('p-value',p_value)
if p_value > 0.05:
    print('Accept the null hypothesis')
else:
    print('Reject null hyphothesis')

#Task 5 - Purpose vs Loan Defaulting


Importing header files
from scipy.stats import chi2_contingency

#Critical value 
critical_value = stats.chi2.ppf(q = 0.95, # Find the critical value for 95% confidence*
                      df = 6)   # Df = number of variable categories(in purpose) - 1
print('critical value is:',critical_value)
#Code starts here
yes = data[data['paid.back.loan']=='Yes']['purpose'].value_counts()
no =data[data['paid.back.loan']=='No']['purpose'].value_counts()
observed=pd.concat([yes.transpose(),no.transpose()], 1,keys=['Yes','No'])
chi2, p, dof, ex = chi2_contingency(observed)
print('chi square:',chi2)
print('p-value:',p_value)
print('degree of freeedom:',dof)
print('expected value:',ex)
if chi2 > critical_value :
    print('Reject the null hypothesis')
else:
    print('Accept null hyphothesis')

