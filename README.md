# Facebook backend

# API description: 



### get_ad_stats
- Host: 0.0.0.0:5000
- Request: GET
- Endpoint: /get_ad_stats
- Arguments:
 - ad_id:


### get_data
- Host: 0.0.0.0:5000
- Request: GET
- Endpoint: /get_data
- Arguments:
 - table_name: table name
 - table_columns: table columns, separated by commas.
 - table_conditions: where filters. If no one wanted, set it to `True`.
 
 
### get_tags_stats
- Host: 0.0.0.0:5000
- Request: GET
- Endpoint: /get_tags_stats
- Description: aggregated statistics by campaign tag
	- avg(stats.STA_spent)
	- avg(stats.STA_IMPRESSIONS)
	- avg(stats.STA_CLICKS)
	- avg(stats.STA_CTR)
	- avg(stats.STA_AGV_CPM)
	- avg(stats.STA_AGV_CPC)
	- avg(stats.STA_CONVERSION)
