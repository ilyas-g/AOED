select
    title,
    company,
    location
from {{ SOURCE('jobs', 'jobs_raw') }}