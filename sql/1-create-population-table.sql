CREATE TABLE [censusdatabase].[dbo].[population] (
    ProjectionID int IDENTITY PRIMARY KEY,
    Region varchar(255) NOT NULL,
    Scenario varchar(255) NOT NULL,  -- High, Medium, Low
    Year int NOT NULL,
    -- StartPopulation int,
    -- Births int,
    -- Deaths int,
    -- NaturalIncrease int,
    -- NetOverseasMigration int, optional
    -- NetInterstateMigration int, optional
    -- TotalMigration int,
    -- TotalGrowth int,
    -- EndPopulation int,
    -- TotalFertilityRate int,
    -- StandardisedDeathRate int,
    -- TotalMigrationRate int,
    -- AnnualPopulationGrowth int,
    -- MedianAgeMales int,
    -- MedianAgeFemales int,
    -- MedianAgePersons int,
    -- SexRatio int,
    -- Age_Under_15_YearsRate int,
    -- Age_15_64_YearsRate int,
    -- Age_65_Over_YearsRate int,
    -- Age_85_Over_YearsRate int,
    -- DependencyRatio int,
);