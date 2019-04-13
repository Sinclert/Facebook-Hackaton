# Facebook backend

# API description: 


### get_data
- Host: localhost:3306
- Request: GET
- Endpoint: /get_data
- Arguments:
 - table_name: table name
 - table_columns: table columns, separated by commas.
 - table_confitions: where filters. If no one wanted, set it to `True`.
 
 
 ### get_tags_stats
- Host: localhost:3306
- Request: GET
- Endpoint: /get_tags_stats
- Description: aggregated statistics by campaign tag
	- avg(stats.STA_spent)
	- avg(stats.STA_CLICKS)
	- avg(stats.STA_CTR)
	- avg(stats.STA_AGV_CPM)
	- avg(stats.STA_AGV_CPC)
	- avg(stats.STA_CONVERSION)
	- avg(stats.STA_SOCIAL_IMPRESSIONS)
