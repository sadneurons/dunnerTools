# Simple class to wrap a pubmed search
from Bio import Entrez
class Searchpubmed:
    '''
    This function is a wrapper around some biopython.Entrez methods to enable some
    useful defaults to be enabled, including prettier printing to the terminal
    and better display of the abstracts if necessary. This will eventually be
    enabled as a text-based search engine for Pubmed in the command line for
    UNIX/Linux users.
    '''
    def __init__(self, email, max, sort, retmode, query):
        self.email = email
        self.max = max
        self.retmode = retmode
        self.query = query
        self.sort = sort
        self.results = None
        self.summaries = None

    def __repr__(self):
        return f'{type(self).__name__!r}({self.email!r}, {self.max!r}, {self.retmode!r}, {self.query!r})'

    def runsearch(self):
        Entrez.email = self.email
        handle = Entrez.esearch(db='pubmed',
                                    sort=self.sort,
                                    retmax=self.max,
                                    retmode=self.retmode,
                                    term=self.query)
        self.results = Entrez.read(handle)

    def getsummary(self, id):
        assert self.results != None, f"{type(self).__name__!r}.results is empty"
        Entrez.email = self.email
        handle = Entrez.efetch(db='pubmed',
                                    retmode=self.retmode,
                                    id=id)
        return Entrez.read(handle)

    def printsummary(self, id):

    def getsummaries(self):
        assert self.results != None, f"{type(self).__name__!r}.results is empty"
        self.summaries = [self.getsummary(id) for id in self.results['IdList']]



    def rprint(self):
        assert self.results != None, f"{type(self).__name__}.results is empty"
        print(self.results)



