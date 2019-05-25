select
    pop.name as "City Name"
    , pop.stname as "State"
    , pop.popestimate2017 as "Est. Population (2017)"
from public.subcounty_pop_est_2017 as pop
where
    pop.sumlev = 162
    and pop.popestimate2017 > 500000
order by pop.popestimate2017 desc;
