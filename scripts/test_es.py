#!/Users/jiangyu/python3.6/bin/python
import elasticsearch

class ES(object):
	@classmethod
	def connect_host(cls):
		hosts=[{"host": "hz.zjcitybao.com","port": "30920"}]
		es = elasticsearch.Elasticsearch(
			hosts,
			sniff_on_start=True,
			sniff_on_connection_fail=True,
			sniffer_timeout=600
		)
		return es