# Banking Inferences
Bank Of New York wants to expand its branches and for that it has certain hypothesis and statements it wants to verify. 
Using the inferential statistics method help the bank.

![Alt txt](https://embedwistia-a.akamaihd.net/deliveries/316e4529ab49ad42cbc31fb8491d4da27431489b.webp?image_crop_resized=960x540)









## About Dataset :
It has data of 9578 customers with the following 15 features:  <br/>
* ID of the customer  <br/>
* If the customer meets the credit underwriting criteria of LendingClub.com or not <br/>
* The purpose of the loan(takes values :"creditcard", "debtconsolidation", "educational", "majorpurchase", "smallbusiness", and "all_other"). <br/>
* The interest rate of the loan
* The monthly installments owed by the borrower if the loan is funded
* The natural log of the self-reported annual income of the borrower
* The debt-to-income ratio of the borrower (amount of debt divided by annual income)
* The FICO credit score of the borrower
* The number of days the borrower has had a credit line.
* The borrower's revolving balance (amount unpaid at the end of the credit card billing cycle)
* The borrower's revolving line utilization rate (the amount of the credit line used relative to total credit available)
* The borrower's number of derogatory public records (bankruptcy filings, tax liens, or judgments)
* The borrower's number of inquiries by creditors in the last 6 months
* The number of times the borrower had been 30+ days past due on a payment in the past 2 years
* Whether the user has paid back loan

## Things Done in Project:
* Calculate the confidence interval
* Central limit theorem on installment column of dataset
* Then i have tried to find out using hypothesis testing that is there any difference between small businees or big business for interest rate <br/>
* Installment vs Loan Defaulting <br/>
Hypothesis testing is done to see is there any difference in amount of installment paid by loan defaulters and loan non defaulters <br/>
Null Hypothesis: There is no difference in installments being paid by loan defaulters and loan non defaulters <br/>
Alternate Hypothesis : There is difference in installments being paid by loan defaulters and loan non defaulters <br/>
* Purpose vs Loan Defaulting <br/>
Another thing bank suspects is that there is a strong association between purpose of the loan(purpose column) of a person and whether that person has paid back loan (paid.back.loan column)  <br/>
Since both are categorical columns, we will do chi-square test to test the same. <br/>
Null Hypothesis : Distribution of purpose across all customers is same. <br/>
Alternative Hypothesis : Distribution of purpose for loan defaulters and non defaulters is different. <br/>
