select
	stats.STA_DATE,
	stats.STA_IMPRESSIONS,
	stats.STA_CLICKS,
	round(stats.STA_SPENT, 2),
	round(stats.STA_CTR, 2)
from
	facebookii_ht.statistics stats
where
	stats.STA_IMPRESSIONS > 0
	and ADS_ID_AD={ad_id}