select
    state_fips as "State FIPS"
    , stusab as "State Abbreviation"
    , state_name as "State Name"
from public.fips_states
order by "State FIPS";
