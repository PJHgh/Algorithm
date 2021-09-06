SELECT
    ANIMAL_ID,
    NAME,
    case
        when SEX_UPON_INTAKE like '%Neutered%' or SEX_UPON_INTAKE like '%Spayed%' then 'O'
        else 'X'
    end
from ANIMAL_INS
order by ANIMAL_ID