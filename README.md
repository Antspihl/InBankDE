# InBankDE
Trial project for InBank Data Engineer internship

Data Engineer Intern – test assignment 
# Part 1: Aggregated Monthly Payments (SQL)
Using the following four tables (payments, currencies, exchange rates, blacklist), please write
a query to return the amounts in euros aggregated by transaction_date:
Be informed that:

-  The resulting table should provide the sum in EUR, use the exchange rate table if
payments are in other currencies
- Due to a data quality error payments table got some payments in discontinued
currencies (where currencies.end_date is not NULL), they should be excluded from
the final result
- Do pay attention to the blacklist table - as payments from blacklisted users should also
be excluded


# Part 2: Weekend Data Processing (Python)
**Disclaimer: All names, characters, and incidents portrayed in this assignment are fictitious, 
no identification with actual products, places, companies or individuals is intended.**

In order to fulfill regulatory requirements, I-bank is obliged to provide aggregated daily report to B-Authority. 
It’s been agreed that during workdays, reports should be provided daily by 5 pm at latest. However, the agreement
for weekends is different - due to regular scheduled maintenance of B-Authority servers, data for Saturday and Sunday 
should be aggregated and sent out in one file on Monday mornings.
Input: 2 csv files with aggregated data for Saturday and Sunday.
Output: 1 csv file with Saturday and Sunday data combined.
Task: please write a Python script that would combine data from 2 files (archive with files available in GitHub) into one.
Overall file structure could be preserved - but add information about combined file generation date (in additional column).

# Part 3: Questions
Please answer the following questions in up to a few sentences. It’s totally fine to use any support materials - however try not to just copy and paste but rather use your own words.
- What are the major differences between ETL and ELT approaches to data transformation?
- What are the major differences between data analytics and data engineering?
- Is there any specific software/tool/technology you are really interested in working with?