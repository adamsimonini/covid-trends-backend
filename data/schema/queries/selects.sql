-- TABLE JOIN COMMANDS

-- join health regions and provinces
SELECT * FROM health_regions hr
LEFT JOIN provinces p
ON p.province_code = hr.fk_province_code;

-- join health regions, provinces, and regions
WITH hr_province AS (
	SELECT * FROM health_region hr
	LEFT JOIN province p
	ON p.id = hr.fk_province_id
)
SELECT * FROM hr_province hp
LEFT JOIN region r
ON hp.fk_region_id = r.id;

-- join 

select hr_uid, health_region.name_en, health_region.name_fr, geo_code, alpha_code, province.name_en, province.name_fr from health_region
inner join province on fk_province_id=province.id
where health_region.name_en::text like '%Ot%'
or health_region.name_fr::text like '%Ot%'
or province.name_en::text like '%Ot%' or province.name_fr::text like '%Ot%'
or alpha_code::text like '%Ot%' or geo_code::text like '%Ot%' ;