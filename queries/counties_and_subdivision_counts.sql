select states.state_name, counties.full_name, count(subdivisions.cousubfp) as subdivision_count
from public.fips_states as states
inner join public.fips_counties as counties
    on states.state_fips = counties.state_fips
left join public.fips_subdivisions as subdivisions
    on states.state_fips = subdivisions.state_fips
    and counties.county_fips = subdivisions.county_fips
group by states.state_name, counties.full_name
order by states.state_name, counties.full_name;
