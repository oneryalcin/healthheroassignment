import string
import sqlite3
import logging
from pathlib import Path
from datetime import datetime

from database import Base, Word, session, engine
from config import DB_FILE, WOWELS, LOGGING_FORMAT

# Setup some logging
logging.basicConfig(format=LOGGING_FORMAT, level=logging.DEBUG)
logger = logging.getLogger(__name__)


def commit_to_db(word_dict: dict) -> None:
    """Add the word to the database

    Args:
        word_dict: (dict): output of parse function
    Raises:
        ValueError if word exists in db raises value error
    Returns:
        None: This function only has side effect, no return,
              commits word to DB
    """
    # Create SQLAlchemy object
    word = Word(**word_dict)

    try:
        session.add(word)

        logger.debug('Adding %s to database' % word_dict)
        session.commit()
    except sqlite3.IntegrityError as e:
        logger.exception('Cannot add %s to DB' % word_dict)
        raise ValueError(f'Word {word_dict.get("word")} is already in the database')


def print_db_contents() -> None:
    """Print out last 5 items added to DB
    """
    words = session.query(Word).order_by(Word.createdOn.desc()).limit(5)

    # Printing headers
    print('Last added 5 items in the DB are\n')
    print('{:<20}  {:<10}  {:<15} {:<25}'.format('word', 'numVowels', 'numConsonants', 'createdOn'))

    # Printing rows
    for word in words:
        print('{:<20}  {:<10}  {:<15} {:<25}'.format(
            word.word,
            word.numVowels,
            word.numConsonants,
            str(word.createdOn)
        ))


def parse(word: str) -> dict:
    """Parses the word into numofVowels and Consonts
    and adds timestamp

    Args:
        word: (str) Input string
    Returns:
        (dict): Dictionary of num of vowels and consonants with timestamp
                for the input string `word`
    """

    # Normalize:
    # 1- Remove any punctuation
    # 2- Remove whitespace
    # 3- lowercase
    logger.debug('Normalizing input word of: %s' % word)
    word = word \
        .translate(str.maketrans('', '', string.punctuation)) \
        .replace(' ', '') \
        .lower()

    logger.debug('After normalization result is %s ' % word)

    # Initialize counters and count the number of vowels/consonants
    vowel_ctr, consonant_ctr = 0, 0
    for letter in word:
        if letter in WOWELS:
            vowel_ctr += 1
        else:
            consonant_ctr += 1

    return {
        'word': word,
        'numVowels': vowel_ctr,
        'numConsonants': consonant_ctr,
        'createdOn': datetime.now()
    }


def count_vowels_and_consonants(word: str) -> None:
    """Given word count vowels and consonants and add to DB

    Args:
        word (str): Input string
    """
    # Check if DB exists, if it doesn't create one new
    if Path(f'{DB_FILE}').is_file():
        logger.info('SQlite DB %s exists, skipping DB creation' % DB_FILE)
    else:
        logger.warning("SQlite DB %s doesn't exist, will create a new one" % DB_FILE)
        Base.metadata.create_all(engine)
        logger.info('Created a new SQlite DB: %s' % DB_FILE)

    # Parse the word into a dict
    parsed_word = parse(word)

    # Save to DB
    commit_to_db(parsed_word)

    # Print last 5 items added to DB
    print_db_contents()


if __name__ == "__main__":
    count_vowels_and_consonants('domates')
