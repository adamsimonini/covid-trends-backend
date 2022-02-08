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