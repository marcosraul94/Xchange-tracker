Models:

Bank: id, name
Rate: id, currency, amount

Relationships
Bank has multiple rates
A Rate belongs to a Bank

Access patterns                                             PK                              SK
Get bank by id                                              b#id                    
Get all banks                                               GSI on entity type = bank
Get all rates for a certain day                             GSI on entity type = rate       SK.begins(created_at)
Get all rates for a bank                                    b#id                            SK.begins(r#id)




Next steps for project:

- Create BankRate model
- Save and Create model
- Add create models script for local dev
- Add e2e tests, just delete all tables after
- Add linter and style guide to both projects
- Add ci for running tests in pipeline