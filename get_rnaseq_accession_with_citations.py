#!/usr/bin/python
#Functions to fetch citations, articles & SRA ids
from Bio import Entrez

#increase query limit to 10/s
Entrez.email = ""
Entrez.api_key=""

#Find the pmids from search result
def get_pmids(term,date):
	pmids = []
	handle=Entrez.esearch(db="pubmed", retmax=2, term=term, mindate=date)
	record = Entrez.read(handle)
	pmids.append(record["IdList"])
	return pmids
#Articles associated with a pmid
def get_citations(pmid):
	link_list = []
	links = Entrez.elink(dbfrom="pubmed", id=pmid, linkname="pubmed_pubmed")
	record = Entrez.read(links)
	records = record[0][u'LinkSetDb'][0][u'Link']
	for link in records:
		link_list.append(link[u'Id'])
	return len(link_list)
#SRA ids associated with a pmid
def get_sra_ids(pmid):
	sra_list = []
	links = Entrez.elink(dbfrom="pubmed", id=pmid, linkname="pubmed_sra")
	record = Entrez.read(links)
	records = record[0][u'LinkSetDb'][0][u'Link']
	for link in records:
		sra_list.append(link[u'Id'])
	return sra_list

#Usage demo
pmids=get_pmids("RNA-seq","2017/01/01")
for pmid in get_pmids("RNA-seq","2017/01/01"):
	if get_citations(pmid)>=2:
		print(get_sra_ids(pmid))
