Models:

Bank: id, name
Rate: id, currency, amount

Relationships
Bank has multiple rates
A Rate belongs to a Bank

Access patterns                                             PK                              SK
Get bank by id                                              b#name                          b#name
Get rate by id                                              b#name                          r#currency#datetime
Get all banks                                               GSI(entity_type=bank)
Get all rates for a certain day and currency                GSI(entity_type=rate)           r#currency#datetime
Get all rates for a bank and currency                       b#name                          r#currency#datetime


Next steps for project:
- Add ci for running tests in pipeline