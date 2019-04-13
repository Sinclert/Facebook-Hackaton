select
	ads.ADS_ID_AD,
	round(act_stats.POST_CLICK_28D / stats.STA_ACCUMULATED_CLICKS, 2),
	round(act_stats.POST_IMP_28D / stats.STA_ACCUMULATED_IMPRESSIONS, 2)
from
	facebookii_ht.ads_api ads
	left join facebookii_ht.actions_stats_creatives act_stats on act_stats.ADS_ID_AD=ads.ADS_ID_AD
	left join facebookii_ht.statistics stats on stats.ADS_ID_AD=ads.ADS_ID_AD
where
	stats.STA_ACCUMULATED_IMPRESSIONS > 0
	and stats.STA_ACCUMULATED_CLICKS > 0