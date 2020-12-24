"""Constants and Configs"""

DB_FILE = 'mydb.sqlite'

LOGGING_FORMAT = '%(asctime)s %(process)d %(name)s %(levelname)s: %(message)s'

# Instead of list (WOWELS = 'aeiou') use set for lookup.
# Set is O(1) rather than O(n).
# see https://wiki.python.org/moin/TimeComplexity
WOWELS = {'a', 'e', 'i', 'o', 'u'}
