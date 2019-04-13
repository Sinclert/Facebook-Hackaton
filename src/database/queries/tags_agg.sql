select
	tags.tag,
	round(avg(stats.STA_spent), 2),
    round(avg(stats.STA_IMPRESSIONS), 2),
	round(avg(stats.STA_CLICKS), 2),
	round(avg(stats.STA_CTR), 2),
	round(avg(stats.STA_AGV_CPM), 2),
	round(avg(stats.STA_AGV_CPC), 2),
	round(avg(stats.STA_CONVERSION), 2)
from
	facebookii_ht.tags tags
	left join facebookii_ht.campaigns_tags camp_tags on camp_tags.TAGS_ID_TAG=tags.ID_TAG
	left join facebookii_ht.campaigns camp on camp.CAM_ID_CAMPAIGN=camp_tags.CAMPAIGNS_CAM_ID_CAMPAIGN
	left join facebookii_ht.ads_api ads on ads.CAMPAIGNS_CAM_ID_CAMPAIGN=camp.CAM_ID_CAMPAIGN
	left join facebookii_ht.statistics stats on stats.ADS_ID_AD=ads.ADS_ID_AD
group by 1
