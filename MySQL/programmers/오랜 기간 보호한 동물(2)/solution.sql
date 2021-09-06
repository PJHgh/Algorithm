with init_table as (
    SELECT
        ANIMAL_INS.ANIMAL_ID,
        ANIMAL_INS.NAME,
        ANIMAL_OUTS.DATETIME - ANIMAL_INS.DATETIME as period
    from ANIMAL_INS inner join ANIMAL_OUTS
        on ANIMAL_INS.ANIMAL_ID = ANIMAL_OUTS.ANIMAL_ID
)

select ANIMAL_ID, NAME
from init_table
order by period desc
limit 2
