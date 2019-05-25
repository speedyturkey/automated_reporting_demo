select
    state as "State"
    , state_fips as "State FIPS"
    , county_fips as "County FIPS"
    , full_name as "County Name"
from public.fips_counties
order by "State FIPS", "County FIPS";
