"""
Find TermSets by name
"""

from office365.sharepoint.client_context import ClientContext
from office365.sharepoint.taxonomy.sets.set import TermSet
from tests import test_team_site_url, test_client_credentials

ctx = ClientContext(test_team_site_url).with_credentials(test_client_credentials)
term_group = ctx.taxonomy.term_store.term_groups.get_by_name("Geography")
term_sets = term_group.get_term_sets_by_name("Countries").execute_query()
for ts in term_sets:  # type: TermSet
    print(ts.id)
