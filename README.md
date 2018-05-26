# MagicDb
Work On Magic Database Project

MagicDb is intended to be a personal collection management tool for Magic:The Gathering. The tool will be an interface for an underlying database for the user's personal collection. Eventually analysis tools will be developed to provide the user with information such mana cost distribution, card type distribution, deck size, etc.

Current project layout is that each file has it's own independent branch for testing and development. This will later be adjusted to component branches once the architecture becomes more developed. Tests are checked in for a corresponding file branch and are expected to be run from that branch. Because files only exist on their corresponding branches, tests will run with mocks of the dependencies of the file (which are imported with the test case).
